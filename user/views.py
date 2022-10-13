from django.shortcuts import render
from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib.auth.decorators import login_required


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name")


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("age", "identificacion", "especialidad")


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == "POST":
        pass
    else:
        user_form = UserForm(instance=request.user)
        user_profile_form = UserProfileForm(instance=request.user.userprofile)
    return render(request, "profile.html", {
        "u_form": user_form,
        "p_form": user_profile_form
    })
