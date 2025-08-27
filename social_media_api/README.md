# Social Media Backend API

A feature-rich backend API for a social media platform, built with **Django REST Framework**. This project implements user authentication, posts, comments, likes, follows, notifications, and feed generation.

---

## 🚀 Key Features

- **User Authentication**
  - Register, login, and token-based authentication.
  - Custom user model with bio, profile picture, and followers.
- **Posts & Comments**
  - Full CRUD operations.
  - Users can only edit/delete their own posts and comments.
- **Follow System & Feed**
  - Follow/unfollow users.
  - View aggregated feed of posts from followed users.
- **Likes & Notifications**
  - Like/unlike posts.
  - Real-time notifications for likes, comments, and new followers.
- **Scalable API Architecture**
  - Modular Django apps: `accounts`, `posts`, and `notifications`.
  - DRF viewsets and serializers for maintainability.

---

## 🛠 Tech Stack

- **Backend:** Django, Django REST Framework  
- **Database:** MYSQL  
- **Authentication:** Token-based authentication (DRF Authtoken)

---



