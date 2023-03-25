

from django.urls import path
from .views import RegisterAPIView,CreateblogAPI,UpdateBlogAPI,ListBlogAPI,AddCommentAPI,CommentsAPI,UpdateCommentAPI
from .views import AdminListBlog,AdminDeleteBlogAPI,AdminListComment,AdminDeleteCommentAPI
 

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name ='register'),
    #Blog
    path('createblog/',CreateblogAPI.as_view(),name ='create_blog'),
    path('updateblog/<int:id>',UpdateBlogAPI.as_view(),name ='update_blog'),
    path('listblogs/',ListBlogAPI.as_view(),name ='listblog'),
    #comments
    path('addcomments/',AddCommentAPI.as_view(),name ='addcomment'),
    path('comments/<int:blog_post_id>',CommentsAPI.as_view(), name ='commentlist'),
    path('updatecomments/<int:id>',UpdateCommentAPI.as_view(), name ='updatecomment'),
    #admin blog
    path('adminlistblog/',AdminListBlog.as_view(),name = 'listblog'),
    path('admindelete/<int:id>',AdminDeleteBlogAPI.as_view(), name = 'delblogs'),
    #admin comment
    path('adminlistcomment/',AdminListComment.as_view(),name = 'listcomments'),
    path('admindeletecomment/<int:id>',AdminDeleteCommentAPI.as_view(), name = 'delcomments'),


]