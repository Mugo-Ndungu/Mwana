from django.shortcuts import render,redirect
from .models import Posts, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializer import PostSerializer,ProfileSerializer
from rest_framework.views import APIView
from rest_framework import status

def posts(request):
    posts = Posts.objects.all()
    return render(request,'home.html',{"posts":posts})

    
@login_required(login_url = '/accounts/login/')
def profile(request,username):
    profile = User.objects.get(username=username)
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details=Profile.filter_by_id(profile.id)

    posts = Posts.get_profile_posts(profile.id)

    context = {
        "profile":profile,
        "profile_details":profile_details,
        "posts":posts,
    }

    return render(request, 'profile.html',context)

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            posts = form.save(commit=False)
            posts.profile = current_user
            posts.save()
        return redirect('posts')
    else:
        form = NewPostForm()
    return render(request,'new_post.html',{"form":form})

def emergency(request):
    return render(request,'emergency.html')

def about(request):
    return render(request,'about.html')


@login_required(login_url = '/accounts/login/')
def update_profile(request,username):
    profile = User.objects.get(username = username)
    return render(request,'updateprofile.html',{"profile":profile})


def zerototwo(request,tag):
    zerototwo = Posts.objects.get(tag=tag)
    posts = Posts.get_zerototwo_posts(tag)
    return render(request, '0_2.html',{"zerototwo":zerototwo},{"posts":posts})

def twotofour(request,tag):
    twotofour = Posts.objects.get(tag='2-4')
    posts = Posts.get_twotofour_posts(tag)
    return render(request, '2_4.html',{"twotofour":twotofour},{"posts":posts})

def fourtosix(request,tag):
    fourtosix = Posts.objects.get(tag='4-6')
    posts = Posts.get_fourtosix_posts(tag)
    return render(request, '4_6.html',{"fourtosix":fourtosix},{"posts":posts})

def sixtoeight(request,tag):
    sixtoeight = Posts.objects.get(tag='6-8')
    posts = Posts.get_sixtoeight_posts(tag)
    return render(request, '6_8.html',{"sixtoeight":sixtoeight},{"posts":posts})

def eighttoten(request,tag):
    eighttoten = Posts.objects.get(tag='8-10')
    posts = Posts.get_eighttoten_posts(tag)
    return render(request, '8_10.html',{"eighttoten":eighttoten},{"posts":posts})

def tentotwelve(request,tag):
    tentotwelve = Posts.objects.get(tag='10-12')
    posts = Posts.get_tentotwelve_posts(tag)
    return render(request, '10_12.html',{"tentotwelve":tentotwelve},{"posts":posts})

def twelvetofourteen(request,tag):
    twelvetofourteen = Posts.objects.get(tag='12-14')
    posts = Posts.get_twelvetofourteen_posts(tag)
    return render(request, '12_14.html',{"twelvetofourteen":twelvetofourteen},{"posts":posts})

def fourteentosixteen(request,tag):
    fourteentosixteen = Posts.objects.get(tag='14-16')
    posts = Posts.get_fourteentosixteen_posts(tag)
    return render(request, '14_16.html',{"fourteentosixteen":fourteentosixteen},{"posts":posts})
    

class PostList(APIView):
    def get(self,request, format=None):
        all_posts = Posts.objects.all()
        serializers =PostSerializer(all_posts,many=True)
        return Response(serializers.data)

    def post(self,request, format=None):
        serializers = PostSerializer(data = request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileList(APIView):
    def get(self,request,format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles,many=True)
        return Response(serializers.data)

    def post(self,request, format=None):
        serializers = ProfileSerializer(data = request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

