from django.urls import path, include
from django.views.generic import TemplateView
# from . import views

app_name = 'sbuddy'
urlpatterns = [
 path('', TemplateView.as_view(template_name="mysite/index.html")),
#  path('forms/', views.forms, name='forms')
]