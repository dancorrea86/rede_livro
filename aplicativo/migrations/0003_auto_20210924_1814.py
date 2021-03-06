# Generated by Django 3.2.7 on 2021-09-24 21:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicativo', '0002_auto_20210924_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='users/'),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('book_pic', models.ImageField(blank=True, default='book/book_profile.png', null=True, upload_to='books')),
                ('readers', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
