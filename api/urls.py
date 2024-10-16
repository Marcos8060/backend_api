from django.urls import path
from .views import *

urlpatterns = [
    path('blogs/', BlogList.as_view()),
    path('blogs/<int:pk>/', BlogDetail.as_view()),
]