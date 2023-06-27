from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=150)
    email=models.EmailField(unique=True)
    phone_regex=RegexValidator(
        regex=r'\d{10}$',
        message="phone no. is invalid"
    )
    phone=models.CharField(validators=[phone_regex],max_length=10,null=True,blank=True)
    createdAt=models.DateTimeField(auto_now=True)


class Blog(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blogs')
    headline=models.CharField(max_length=350)
    body=models.TextField()

