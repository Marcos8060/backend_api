
from rest_framework.response import Response
from rest_framework import status,generics
from .models import *
from .serializers import BlogSerializer,CommentSerializer
from rest_framework.views import APIView
from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# --------------------------- BLOG VIEW -----------------------#

class BlogList(APIView):
    
    @swagger_auto_schema(
        operation_description="Retrieve all blog posts",
        responses={200: BlogSerializer(many=True)}
    )
    
    # create a function to get blogs
    def get(self,request,format=None):
        blog = Blog.objects.all()
        serializer = BlogSerializer(blog,many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        operation_description="Create a new blog post",
        request_body=BlogSerializer,
        responses={
            201: openapi.Response('Created', BlogSerializer),
            400: 'Bad Request'
        }
    )
    
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
        
        
    
    @swagger_auto_schema(
        operation_description="Retrieve a single blog post by ID",
        responses={200: BlogSerializer(), 404: 'Not Found'}
    )
    
    # create fuction to get a single blog
    def get(self,request,pk,format=None):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)
    
    
    @swagger_auto_schema(
        operation_description="Update a blog post by ID",
        request_body=BlogSerializer,
        responses={
            200: BlogSerializer,
            400: 'Bad Request',
            404: 'Not Found'
        }
    )
    
    # create a function to edit a single blog
    def put(self,request,pk,format=None):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    
    @swagger_auto_schema(
        operation_description="Delete a blog post by ID",
        responses={204: 'No Content', 404: 'Not Found'}
    )
    
    # create a function to delete a blog
    def delete(self,request,pk,format=None):
        blog = self.get_object(pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
# --------------------------- END OF BLOG VIEW -----------------------#

# --------------------------- COMMENT VIEW -----------------------#
class CommentList(APIView):
    
    
    # get all comments
    @swagger_auto_schema(
        operation_description="Retrieve all comments",
        responses={200: CommentSerializer(many=True)}
    )
    
    def get(self,request,format=None):
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment,many=True)
        return Response(serializer.data)
    
    
    # create a new comment
    @swagger_auto_schema(
        operation_description="Create a new comment",
        request_body=CommentSerializer,
        responses={
            201: openapi.Response('Created', CommentSerializer),
            400: 'Bad Request'
        }
    )
    
    def post(self,request,format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


class CommentDetail(APIView):
    
    def get_object(self,pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404
    
    
    @swagger_auto_schema(
        operation_description="Retrieve a single comment by ID",
        responses={200: CommentSerializer(), 404: 'Not Found'}
    )
    
    def get(self,request,pk,format=None):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
    
    # UPDATE A COMMENT
    @swagger_auto_schema(
        operation_description="Update a comment by ID",
        request_body=CommentSerializer,
        responses={
            200: CommentSerializer,
            400: 'Bad Request',
            404: 'Not Found'
        }
    )
    
    def put(self,request,pk,format=None):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    # DELETE A COMMENT
    
    @swagger_auto_schema(
        operation_description="Delete a comment by ID",
        responses={204: 'No Content', 404: 'Not Found'}
    )
    
    def delete(self,request,pk,format=None):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            
            
            
            
# --------------------------- END OF COMMENT VIEW -----------------------#

    
        
                    
    

