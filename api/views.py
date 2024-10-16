
from rest_framework.response import Response
from rest_framework import status,generics
from .models import *
from .serializers import BlogSerializer
from rest_framework.views import APIView
from django.http import Http404


class BlogList(APIView):
    
    # create a function to get blogs
    def get(self,request,format=None):
        blog = Blog.objects.all()
        serializer = BlogSerializer(blog,many=True)
        return Response(serializer.data)
    
    
    # create function to post blog
    def post(self,request,format=None):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class BlogDetail(APIView):
    
    # create instance of a single blog
    def get_object(self,pk):
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            raise Http404
        
    # create fuction to get a single blog
    def get(self,request,pk,format=None):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)
    
    # create a function to edit a single blog
    def patch(self,request,pk,format=None):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # create a function to delete a blog
    def delete(self,request,pk,format=None):
        blog = self.get_object(pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
        
                    
    

