from rest_framework import serializers
from .models import Profile,Posts

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user','username','email','picture','user','bio')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model= Posts
        fields = ('profile','image','title','content','published','tag')
