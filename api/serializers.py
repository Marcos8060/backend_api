from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User



        
class CommentSerializer(serializers.ModelSerializer):
    
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Comment
        fields = ['author','blog','text','pub_date']
        
              
        
class BlogSerializer(serializers.ModelSerializer):
    
    author = serializers.ReadOnlyField(source='author.username')
    
    comments = CommentSerializer(many=True)
    
    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'category', 'image', 'pub_date','comments','author']



class UserSerializer(serializers.ModelSerializer):
    
    blogs = BlogSerializer(many=True,read_only=True)
    
    class Meta:
        model = User
        fields = ['id','username','blogs']
