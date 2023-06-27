from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer,BlogSerializer
from rest_framework.response import Response
from Base.models import User,Blog

# Create your views here.

class UserView(APIView):
    def post(self,request):
        userInfo=UserSerializer(data=request.data)
        if(userInfo.is_valid()):
            userInfo.save()
            return Response(userInfo.data)
        else:
            return Response(userInfo.errors)
    
    def get(self,request):
        userData=User.objects.all()
        serializer=UserSerializer(userData,many=True)
        return Response(serializer.data)

class BlogView(APIView):
    def post(self,request,id):
        user=User.objects.filter(id=id).first()
        if(not user):
            return Response({"msg":"user with id{} not exist".format(id)})
        else:
            body=request.data
            body['user_id']=id
            serializer=BlogSerializer(data=body)
            if(serializer.is_valid()):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
    
    def get(self,request,id):
        user=User.objects.filter(id=id).first()
        if(not user):
            return Response({"msg":"user with id {} not exist".format(id)})
        serializer=UserSerializer(user)
        return Response(serializer.data.get("blogs"))
    
    def patch(self,request,id):
        user=User.objects.filter(id=id).first()
        if(not user):
            return Response({"msg":"user with id {} not exist".format(id)})
        else:
            blog_id=request.data.get("blog_id")
            blog=Blog.objects.filter(id=blog_id).first()
            serializer=BlogSerializer(blog,request.data,partial=True)
            if(serializer.is_valid()):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
    
    def delete(self,request,id):
        user=User.objects.filter(id=id).first()
        if(not user):
            return Response({"msg":"user with id {} not exist".format(id)})
        else:
            blog_id=request.data.get("blog_id")
            blog=Blog.objects.filter(id=blog_id).first()
            if(blog):
                blog.delete()
                return Response({"msg":"blog of user {} with blog_id {} is deleted".format(id,blog_id)})
            else :
                return Response({"msg":"blog not present"})

        