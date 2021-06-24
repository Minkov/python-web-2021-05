from django.shortcuts import render, redirect

from expenses_tracker.core.profile_utils import get_profile
from expenses_tracker.expenses.models import Expense
from expenses_tracker.profiles.forms import CreateProfileForm, EditProfileForm


def profile_details(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }

    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'home-no-profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        profile.delete()
        Expense.objects.all().delete()
        return redirect('home')

    context = {
    }

    return render(request, 'profile-delete.html', context)
