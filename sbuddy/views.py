from django.shortcuts import reverse, redirect, render
from .models import User
from .forms import UserForm
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage


def profile(request):
    users = User.objects.all()
    return render(request, 'sbuddy/profile.html', {'users': users})

def user_upload(request):
    if request.method == 'POST':
        user = UserForm(request.POST, request.FILES)
        if user.is_valid():
            user.save()
            return redirect('sbuddy:profile')
    else:
        user = UserForm()
    return render(request, 'sbuddy/form.html', {'user': user})

def match_users_by_strengths(request):
    users = User.objects.all()
    matches = []
    for userA in users:
        strengthsA = userA.strengths.split(',')
        for userB in users:
            if userB.name != userA.name:
                strengthsB = userB.strengths.split(',')
                if do_items_match(strengthsA, strengthsB):
                    match = (userA, userB)
                    matches.append(match)

    return render(request, 'sbuddy/matches.html', {'matches': matches})


def match_users_by_skills(request):
    users = User.objects.all()
    matches = []
    for userA in users:
        skillsA = userA.skills.split(',')
        for userB in users:
            if userB.name != userA.name:
                skillsB = userB.skills.split(',')
                if do_items_match(skillsA, skillsB):
                    match = (userA, userB)
                    matches.append(match)

    return render(request, 'sbuddy/matches_skill.html', {'matches': matches})

def do_items_match(a, b):
    for item in a:
        for itemB in b:
            if item.lower() == itemB.lower():
                return True
    return False


