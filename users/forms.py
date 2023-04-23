# from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        # model = get_user_model()
        model = CustomUser
        fields = ('email', 'username')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        # model = get_user_model()
        model = CustomUser
        fields = ('email', 'username')
