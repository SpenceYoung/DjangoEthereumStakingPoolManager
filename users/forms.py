# users/forms.py

from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from users.models import Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['discordName']