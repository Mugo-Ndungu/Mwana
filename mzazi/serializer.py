from rest_framework import serializers
from .models import Profile,Posts

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','user','username','email','picture','user','bio')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model= Posts
        fields = ('id','profile','image','title','content','published','tag')
