from django.shortcuts import reverse, redirect, render
from .models import User
from .forms import UserForm
from django.http import HttpResponseRedirect

def profile(request):
    users = User.objects.all()
    return render(request, 'sbuddy/profile.html',{'users':users})

def user_upload(request):
    if request.method=='POST':
        user = UserForm(request.POST,request.FILES)
        if user.is_valid():
            user.save()
            return HttpResponseRedirect(reverse('sbuddy:profile'))
    else:
        user = UserForm()

    return render(request, 'sbuddy/form.html',{'user':user})