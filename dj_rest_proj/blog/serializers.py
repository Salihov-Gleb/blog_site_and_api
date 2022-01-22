from django.contrib.auth.models import User
from rest_framework import serializers
from blog.models import BlogNote, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class BlogNoteSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True, many=True)
    author = UserSerializer(read_only=True)

    class Meta:
        model = BlogNote
        fields = ['id', 'title', 'img', 'category', 'author', 'txt', 'create_date', 'update_date']


class EditBlogNoteSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True, many=True)

    class Meta:
        model = BlogNote
        fields = ['title', 'img', 'category', 'txt']


class TitleBlogNoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogNote
        fields = ['title', 'txt']