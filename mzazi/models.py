from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.dispatch import receiver 
from django.db.models.signals import post_save

class tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    username = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    picture = models.ImageField(upload_to = 'profiles/', default = 'default.png' )
    bio = models.CharField(max_length = 200, blank = True)
    

    @receiver(post_save, sender =User)
    def create_user_profile(sender, instance,created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_profile(sender,instance,**kwargs):
        instance.profile.save()

    @classmethod
    def get_by_id(cls,id):
        profile = Profile.objects.get(user=id)
        return profile

    @classmethod
    def filter_by_id(cls,id):
        profile = Profile.objects.filter(user=id).first()
        return profile

 

    def __str__(self):
        return self.username


class Posts(models.Model):
    profile = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    image=models.ImageField(upload_to = 'posts/', default = 'article.png')
    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(tag,blank=True)


    class Meta:
        ordering = ['published']

    @classmethod
    def get_profile_posts(cls,profile):
        posts = Posts.objects.filter(profile__pk=profile)
        return posts

    def __str__(self):
        return self.title