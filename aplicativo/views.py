from django.shortcuts import render
from django.shortcuts import get_object_or_404, render

def home(request):
    return render(request,'pages/base.html')

def books(request):
    return render(request, "pages/books.html")

def users(request):
    return render(request, "pages/users.html")

def book(request, book_id):
    return render(request, "pages/book_profile.html")

def user(request, user_id):
    return render(request, "pages/user_profile.html")

def register(request):
    return render(request, "pages/register.html")
    