

from django.urls import path
from .views import RegisterAPIView,CreateblogAPI,UpdateBlogAPI,ListBlogAPI


urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name ='register'),
    path('createblog/',CreateblogAPI.as_view(),name ='create_blog'),
    path('updateblog/<int:id>',UpdateBlogAPI.as_view(),name ='update_blog'),
    path('listblogs/',ListBlogAPI.as_view(),name ='listblog'),

]