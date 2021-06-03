from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import CustomUserCreationForm, ProfileForm

# Create your views here.
def dashboard(request):
    return render(request, "users/dashboard.html")

def about(request):
	return render(request, "users/about.html")

def base(request):
    return render(request, "base.html")

def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm,
            "profileForm": ProfileForm}
        )
    elif request.method == "POST":#TODO Figure this out
        form = CustomUserCreationForm(request.POST)
        #profileForm = ProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))