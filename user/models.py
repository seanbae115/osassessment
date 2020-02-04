from django.forms import ModelForm, Textarea
from django.db import models


class Users(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    login_id = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
