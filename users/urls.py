# users/urls.py

from django.conf.urls import url, include
from users.views import dashboard, homepage, register

urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^register/", register, name="register"),
    url(r"", homepage, name="homepage")
]
