from django.contrib import admin

from django.contrib import admin
from django.contrib import auth
from django.contrib.auth import admin as auth_admin
from .models import Book

from.forms import UserChangeForm, UserCreationForm
from .models import User

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Campos Personalizados", {"fields": ("bio", "gender", "profile_pic",)}),
    )

admin.site.register(Book)
