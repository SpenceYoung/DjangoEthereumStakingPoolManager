# users/urls.py

from django.conf.urls import url, include
from users.views import dashboard, register, about, base,poolstats

urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^register/", register, name="register"),
    url(r"^about/", about, name="about"),
    url(r"^poolstats/", poolstats, name="poolstats"),
    url(r"", base, name="base")
]
