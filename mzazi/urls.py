from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$',views.home,name='home'),
    # url('^$',views.posts,name='posts'),
    url(r'^profile/(?P<username>\w+)',views.profile,name='profile'),
    url(r'^zerototwo/',views.zerototwo, name='zerototwo'),
    url(r'^twotofour/',views.twotofour,name='twotofour'),
    url(r'^fourtosix/',views.fourtosix,name='fourtosix'),
    url(r'^sixtoeight/',views.sixtoeight,name='sixtoeight'),
    url(r'^eighttoten/',views.eighttoten,name='eighttoten'),
    url(r'^tentotwelve/',views.tentotwelve,name='tentotwelve'),
    url(r'^twelvetofourteen/',views.twelvetofourteen,name='twelvetofourteen'),
    url(r'fourteentosixteen/',views.fourteentosixteen,name='fourteentosixteen'),
    url(r'^update_profile/',views.update_profile,name='update_profile'),
    url(r'^new/',views.new_post,name='new_post'),
    url(r'^emergency/',views.emergency,name='emergency' ),
    url(r'^about/',views.about,name='about'),
    url(r'^posts/(\d+)',views.single_post,name='single'),
    url(r'^new/',views.new_post,name='new_post'),
    url(r'^api/posts/$',views.PostList.as_view()),
    url(r'^api/profile/$',views.ProfileList.as_view()),
    url(r'api/posts/post-id/(?P<pk>[0-9]+)/$', views.PostDescription.as_view()),
    url(r'api/profile/profile-id/(?P<pk>[0-9]+)/$', views.ProfileDescription.as_view()),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)