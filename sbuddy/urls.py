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
from django.views.generic import TemplateView

app_name = 'sbuddy'
urlpatterns = [
 path('', TemplateView.as_view(template_name="sbuddy/index.html")),
 path('accounts/', include('allauth.urls')),
 path('user/',views.user_upload,name="user_upload"),
 path('profiles/',views.profile,name="profile"),
 path('matches/strengths/', views.match_users_by_strengths, name="match_strengths"),
 path('matches/skills/', views.match_users_by_skills, name="match_skills"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)