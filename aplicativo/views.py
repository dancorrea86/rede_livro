from django.shortcuts import render
from .models import User, Book
from django.shortcuts import get_object_or_404, render

def home(request):
    return render(request,'pages/base.html')

def books(request):
    books = Book.objects.all()

    dados = {
        'books': books
    }

    return render(request, "pages/books.html", {'books': books})


def users(request):
    users = User.objects.all()
    print (users)
    dados = {
        'users': users
    }

    return render(request, "pages/users.html", {'users': users})



def book(request, book_id):
    return render(request, "pages/book_profile.html")

def user(request, user_id):
    return render(request, "pages/user_profile.html")

def register(request):
    return render(request, "pages/register.html")
    