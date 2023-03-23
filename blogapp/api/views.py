from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from blogapp.models import BlogPost,Comment
from django.contrib.auth.models import User
from .serializer import RegisterSerializer,BlogcreateSerializer,BlogListSerilaizer,BlogupdateSerializer,AddcommentsSerializer,ListcommentsSerializer,updatecommentsSerializer
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
                'Registeration Successful',
                'It is to inform that your blog account has been created successfully.Please, login to continue. ',
                'from@example.com',
                ['cargil.21pmc117@mariancollege.org'],
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

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

        return Response(serializer.data)

class CommentsAPI(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    print(queryset)
    serializer_class = ListcommentsSerializer
    lookup_field = 'id'

class UpdateCommentAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    lookup_field = 'id'
    serializer_class = updatecommentsSerializer

    #  def get(self, request):
    #     user = request.user
    #     serializer = self.get_serializer(user)
    #     quizzes = Quiz.objects.filter(created_by=user)    #filter quiz created by user
    #     quiz_serializer = QuizSerializer(quizzes, many=True)   
    #     data = {
    #         'user' : serializer.data,                      
    #     }

    #     return Response(data)







    

    





  

           