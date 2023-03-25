from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView,DestroyAPIView
from blogapp.models import BlogPost,Comment
from django.contrib.auth.models import User
from .serializer import RegisterSerializer,BlogcreateSerializer,BlogListSerilaizer,BlogupdateSerializer,AddcommentsSerializer,ListcommentsSerializer,updatecommentsSerializer
from .serializer import AdminlistblogSerializer,AdminlistCommentSerializer
from django.core.mail import send_mail
from django.conf import settings







#JWT token authentication

class ObtainTokenPairWithCookieView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = response.data['access']
        print(token)
        response.set_cookie('jwt', token, max_age=3600, httponly=True)
        return response

class TokenBlacklistView(APIView):
    def post(self, request):
        token = RefreshToken(request.data.get('refresh'))
        token.blacklist()
        return Response("Success")


 # User registeration

class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
         

        response_data = {
            "message": "User created successfully",
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }
        }
        send_mail(
                'Registration Successful',
                'It is to inform that your blog account has been created successfully.Please, login to continue. ',
                'from@example.com',
                [user.email],
                fail_silently=False,
            )
        return Response(response_data)


#Blog creation
class CreateblogAPI(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BlogcreateSerializer


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

        return Response(serializer.data)

#list blog

class ListBlogAPI(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BlogPost.objects.all()
    serializer_class =  BlogListSerilaizer
    


#Update blog

class UpdateBlogAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BlogPost.objects.all()
    lookup_field = 'id'
    serializer_class = BlogupdateSerializer

#comment

class AddCommentAPI(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AddcommentsSerializer
    lookup_field = 'id'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

        return Response(serializer.data)

class CommentsAPI(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    lookup_field = 'blog_post_id'
    # queryset = Comment.objects.filter(blog_post_id)
    #print(queryset)
    serializer_class = ListcommentsSerializer

    def get_queryset(self):
        blog_post_id = self.kwargs.get('blog_post_id')
        print(blog_post_id)
        return Comment.objects.filter(blog_post_id=blog_post_id)






    

class UpdateCommentAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    lookup_field = 'id'
    serializer_class = updatecommentsSerializer

   



#admin BlogPost

class AdminListBlog(ListAPIView):
    permission_classes  = [IsAdminUser]
    serializer_class = AdminlistblogSerializer
    queryset = BlogPost.objects.all()


class AdminDeleteBlogAPI(DestroyAPIView):
    permission_classes  = [IsAdminUser]
    serializer_class = AdminlistblogSerializer
    queryset = BlogPost.objects.all()
    lookup_field = 'id'


#Admin Comments

class AdminListComment(ListAPIView):
    permission_classes  = [IsAdminUser]
    serializer_class = AdminlistCommentSerializer
    queryset = Comment.objects.all()





class AdminDeleteCommentAPI(DestroyAPIView):
    permission_classes  = [IsAdminUser]
    serializer_class = AdminlistCommentSerializer
    queryset = Comment.objects.all()
    lookup_field = 'id'





    

    





  

           