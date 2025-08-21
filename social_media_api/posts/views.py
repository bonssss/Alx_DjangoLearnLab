from rest_framework import viewsets, permissions, filters
from rest_framework.pagination import PageNumberPagination
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status,generics

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit/delete it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the owner
        return obj.author == request.user


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
# class FeedView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         # Get all users that the current user follows + the user itself
#         followed_users = request.user.following.all()
#         users_to_include = list(followed_users) + [request.user]

#         # Get posts from those users, ordered by newest first
#         posts = Post.objects.filter(author__in=users_to_include).order_by('-created_at')

#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Get the current user
        user = self.request.user
        # Get users that the current user follows
        following_users = user.following.all()
        # Filter posts by followed users and order by creation date (newest first)
        return Post.objects.filter(author__in=following_users).order_by('-created_at')


from notifications.utils import create_notification

class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

        # Check if user already liked the post
        like, created = Like.objects.get_or_create(post=post, user=request.user)
        if not created:
            return Response({'message': 'You already liked this post'}, status=status.HTTP_400_BAD_REQUEST)

        # Create notification for post author
        if post.author != request.user:
            create_notification(actor=request.user, recipient=post.author, verb="liked your post", target=post)

        return Response({'message': 'Post liked successfully'}, status=status.HTTP_200_OK)


class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

        like = Like.objects.filter(post=post, user=request.user).first()
        if like:
            like.delete()
            return Response({'message': 'Post unliked successfully'}, status=status.HTTP_200_OK)
        return Response({'message': 'You have not liked this post'}, status=status.HTTP_400_BAD_REQUEST)