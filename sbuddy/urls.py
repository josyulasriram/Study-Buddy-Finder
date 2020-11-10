"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

app_name = 'sbuddy'
urlpatterns = [
 path('', views.index, name='index'),
 path('user/',views.user_upload,name="user_upload"),
 path('profiles/',views.profile,name="profile"),
 path('matches/strengths/', views.match_users_by_strengths, name="match_strengths"),
 path('user_profile/', views.user_profile, name='user_profile'),
 path('matches/time/', views.match_users_by_availability, name='match_time'),
 path('matches/user/', views.get_user_matches, name='user_matches'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)