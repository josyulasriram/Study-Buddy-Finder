from django.shortcuts import reverse, redirect, render
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
    
# def user_upload(request):
#     if request.method == 'POST':
#         user_name = request.POST.get("name","")
#         user_strengths = request.POST.get("strengths","")
#         user_skills = request.POST.get("skills","")
#         user_schedule = request.POST.get("schedule","")
#         if(not(user_name or user_strengths or user_skills or user_schedule)):
#             return render(request, "mysite/form.html")
#         else:
#             user = User(name=user_name,strengths=user_strengths,skills=user_skills,schedule=user_schedule)
#             user.save()
#             User_context = User.objects.all()
#             return render(request, 'mysite/profile.html', {'profile': User_context})

def profile(request):
    users = User.objects.all()
    return render(request, 'mysite/profile.html',{'users':users})

def user_upload(request):
    if request.method=='POST':
        user = UserForm(request.POST,request.FILES)
        if user.is_valid():
            user.save();
            return redirect('profile')
    else:
        user = UserForm()

    return render(request, 'mysite/form.html',{'user':user})
            
