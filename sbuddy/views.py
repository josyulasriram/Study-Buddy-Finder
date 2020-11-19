from django.shortcuts import reverse, redirect, render
from .models import Profile
from .forms import UserForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    return render(request, 'sbuddy/index.html')


def profile(request):
    users = Profile.objects.all()
    return render(request, 'sbuddy/profile.html', {'users': users})


def logout(request):
    logout(request)


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
    users = Profile.objects.all()
    matches = []
    for user_a in users:
        strengths_a = user_a.strengths.split(',')
        for user_b in users:
            if user_b.name != user_a.name:
                weak_b = user_b.weaknesses.split(',')
                if do_items_match(strengths_a, weak_b):
                    match = (user_a, user_b)
                    matches.append(match)

    return render(request, 'sbuddy/matches.html', {'matches': matches})


def match_users_by_availability(request):
    users = Profile.objects.all()
    matches = []
    for user_a in users:
        for user_b in users:
            if user_b.name != user_a.name:
                if user_a.availability == user_b.availability:
                    match = (user_a, user_b)
                    matches.append(match)

    return render(request, 'sbuddy/matches_time.html', {'matches': matches})

def get_user_matches(request):
    current = request.user.profile
    profiles = Profile.objects.all()
    matches = []

    for profile in profiles:
        if profile.name != current.name:
            p_strengths = profile.strengths.split(',')
            c_weak = current.weaknesses.split(',')
            for strength in p_strengths:
                for weak in c_weak:
                    if strength == weak:
                        match = (0, weak, profile)
                        matches.append(match)

            p_weak = profile.weaknesses.split(',')
            c_strength = current.strengths.split(',')
            for strength2 in c_strength:
                for weak2 in p_weak:
                    if strength2 == weak2:
                        match = (1, weak2, profile)
                        matches.append(match)
    return render(request, 'sbuddy/user_matches.html', {'matches': matches})


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
            print('valid')
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('sbuddy:user_profile')

        print('not valid')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'sbuddy/user_profile.html', context)
