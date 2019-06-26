from django import forms
from . models import Posts

class NewPostForm(forms.ModelForm):


    class Meta:
        model=Posts
        fields=['image','title','content','tag',
        ]

# class CommentForm(forms.ModelForm):

#     class Meta:

#         model = Comments

#         fields = ('comment',)
