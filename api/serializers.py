from rest_framework import serializers
from .models import *



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        
        
        
class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True,source="blogs")
    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'category', 'image', 'pub_date','comments']


