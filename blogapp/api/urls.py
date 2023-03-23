

from django.urls import path
from .views import RegisterAPIView,CreateblogAPI


urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('createblog/',CreateblogAPI.as_view(),name='create_blog'),

]