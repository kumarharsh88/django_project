from rest_framework import serializers
from Base.models import User,Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    blogs=BlogSerializer(many=True,read_only=True)
    class Meta:
        model=User
        fields=['id','name','email','phone','blogs']


        