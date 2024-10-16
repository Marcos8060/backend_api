from django.urls import path
from .views import *



urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('blogs/', BlogList.as_view()),
    path('blogs/<int:pk>/', BlogDetail.as_view()),
    path('comments/', CommentList.as_view()),
    path('comments/<int:pk>/', CommentDetail.as_view()),
]