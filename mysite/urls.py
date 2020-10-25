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


from django.views.generic import TemplateView

app_name= 'mysite'
urlpatterns = [
 path('', include('sbuddy.urls')),
 path('admin/', admin.site.urls),
 path('accounts/', include('allauth.urls')),
 path('user/',views.user_upload,name="user_upload"),
 path('profiles/',views.profile,name="profile"),


 #path('user/', TemplateView.as_view(template_name="mysite/form.html")),
 #path('user/user_upload', views.user_upload, name = "user_upload"),
 

]
