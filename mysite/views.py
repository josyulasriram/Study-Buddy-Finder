from django.shortcuts import reverse, redirect, render
#from django_google.flow import DjangoFlow,CLIENT_SECRET_FILE, SCOPES
from django.http.response import JsonResponse
from django.contrib.auth import get_user_model
from django.conf import settings
from django_google.models import GoogleAuth
from .models import User
from .forms import UserForm
from django.http import HttpResponseRedirect

# def user_upload(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('mysite/index.html')
#     else:
#         form = UserForm()
#     return render(request, 'mysite/form.html', {
#         'form': form
#     })

#def profile(request):
    #User_context = User.objects.all()
    #return render(request, 'mysite/profile.html', {'profile': User_context})
    
def user_upload(request):
    if request.method == 'POST':
        user_name = request.POST.get("name","")
        user_strengths = request.POST.get("strengths","")
        user_skills = request.POST.get("skills","")
        if(not(user_name or user_strengths or user_skills)):
            return render(request, "mysite/form.html")
        else:
            user = User(name=user_name,strengths=user_strengths,skills=user_skills)
            user.save()
            User_context = User.objects.all()
            return render(request, 'mysite/profile.html', {'profile': User_context})
            
