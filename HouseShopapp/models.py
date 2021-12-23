from django.contrib.auth.models import User
from django.db import models

class Agent(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    image=models.ImageField(upload_to='AgentImg/',null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    phone=models.CharField(max_length=80,null=True,blank=True)
    mobile=models.CharField(max_length=80,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    facebook=models.CharField(max_length=150,null=True,blank=True)
    instagram=models.CharField(max_length=150,null=True,blank=True)

    def __str__(self):
        return self.user.username

class Ammenity(models.Model):
    name=models.CharField(max_length=80,null=True,blank=True)

    def __str__(self):
        return self.name

class House_single(models.Model):
    image=models.ImageField(upload_to='HouseImg/',null=True,blank=True)
    description=models.TextField(blank=True,null=True)
    price=models.IntegerField(blank=True,null=True)
    location = models.CharField(max_length=150, null=True, blank=True)
    type=models.CharField(max_length=100,choices=(
        ('hause','uy'),
        ('appartement','kvartira'),

    ))
    status=models.CharField(max_length=100,choices=(
        ('sotuvda','progress'),
        ('sotilgan','saled')
     ))

    area=models.IntegerField(null=True,blank=True)
    beds=models.IntegerField(null=True,blank=True)
    bath=models.IntegerField(null=True,blank=True)
    garage=models.IntegerField(null=True,blank=True)
    ammenities=models.ManyToManyField(Ammenity,null=True,blank=True)
    video=models.CharField(max_length=85,null=True,blank=True)
    architecture_image=models.ImageField(upload_to='archectureImg/', null=True,blank=True)
    created_data=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.agent.user.username}   {self.type}"


# class Blog(models.Model):
#     title=models.CharField(max_length=150,null=True,blank=True)
#     author=models.ForeignKey(max_length=150,null=True,blank=True)
#     category=models.CharField(max_length=150,null=True,blank=True)
#     created_data=models.TimeField(null=True,blank=True)
#     text=models.TextField(null=True,blank=True)

#
# class Messages(models.Model):
#     name=models.CharField(max_length=150,null=True,blank=True)
#     email=models.EmailField(null=True,blank=True)
#     subject=models.TextField(null=True,blank=True)
#     message=models.TextField(null=True,blank=True)
#     created_data=models.TimeField(null=True,blank=True)
#
#
# class Comemet(models.Model):
#     # user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
#     comment=models.TextField(null=True,blank=True)
#     blog=models.CharField(Blog,null=True,blank=True)


