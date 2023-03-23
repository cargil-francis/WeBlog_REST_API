

from django.urls import path
from .views import RegisterAPIView,CreateblogAPI,UpdateBlogAPI,ListBlogAPI,AddCommentAPI,CommentsAPI,UpdateCommentAPI


urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name ='register'),
    path('createblog/',CreateblogAPI.as_view(),name ='create_blog'),
    path('updateblog/<int:id>',UpdateBlogAPI.as_view(),name ='update_blog'),
    path('listblogs/',ListBlogAPI.as_view(),name ='listblog'),

    path('addcomments/',AddCommentAPI.as_view(),name ='addcomment'),
    path('comments/<int:id>',CommentsAPI.as_view(), name ='commentlist'),
    path('updatecomments/<int:id>',UpdateCommentAPI.as_view(), name ='updatecomment')


]