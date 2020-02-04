from django import forms
from user.models import Users


class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = "__all__"
