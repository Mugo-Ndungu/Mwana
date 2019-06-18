from django.contrib import admin
from .models import Profile,Posts,tag

class PostAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)
    
admin.site.register(Profile)
admin.site.register(Posts)
admin.site.register(tag)

