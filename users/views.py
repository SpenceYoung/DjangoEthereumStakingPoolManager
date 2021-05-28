from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, "users/dashboard.html")

def homepage(request):
	return render(request, "home.html")