from django.shortcuts import reverse, redirect, render
from .models import Person
from .forms import UserForm, UserUpdateForm, ProfileUpdateForm
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    return render(request, 'sbuddy/index.html')

def profile(request):
    users = Person.objects.all()
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
    users = Person.objects.all()
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
    users = Person.objects.all()
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

@login_required
def user_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('sbuddy:user_profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'sbuddy/user_profile.html', context)
