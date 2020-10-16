from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
# from phone_field import PhoneField
from .models import Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields = ['id','username','password','email']
        extra_kwargs ={'password':{'write_only':True, 'required':True}}
        extra_kwargs ={'email':{'required':True}}
    
    def create(self,validated_data):
        user =User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','user_id','post_title','category','post_img','post_description','price','phone_number']