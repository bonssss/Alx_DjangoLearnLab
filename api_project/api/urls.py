from django.urls import path
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from django.urls import include
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')
urlpatterns =[
    path('books/', BookList.as_view(), name='book-list'),
     path('token/', obtain_auth_token, name='api_token_auth'),
    path('', include(router.urls)),  # Include the router URLs
]