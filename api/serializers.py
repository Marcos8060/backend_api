from rest_framework import serializers
from .models import *


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'category', 'image', 'pub_date']