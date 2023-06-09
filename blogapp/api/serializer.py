from rest_framework import serializers
from ..models import User,BlogPost,Comment
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    is_superuser = serializers.BooleanField(default=False)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password','password2','first_name','last_name','is_superuser')
        
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_superuser=validated_data.get('is_superuser', False)
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user 


class BlogcreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['title','content','image','author']

class BlogListSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'

class BlogupdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['title','content','image','author','updated_at']



class AddcommentsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__' 

class ListcommentsSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Comment
        fields = ['content','blog_post']

class updatecommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['content','updated_at']
        




class AdminlistblogSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogPost
        fields = '__all__'



class AdminlistCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'



    
