from django import forms
from auth_jwt.models import *

class CreateUserForm(forms.ModelForm):

    class Meta:
        model=User
        exclude=['user_permissions','groups','superuser_status','is_active','is_staff','last_login']


class LoginUserForm():
    class Meta:
        model = User
        exclude = ['user_permissions', 'groups', 'superuser_status', 'is_active', 'is_staff', 'last_login']

