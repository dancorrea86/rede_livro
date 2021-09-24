from django.urls import path


from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('users', views.users, name='users'),
    path('books', views.books, name='books'),
    path('users/<int:user_id>', views.user, name='user'),
    path('books/<int:book_id>', views.book, name='book'),
]