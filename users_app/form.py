from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#CustomRegisterForm 是继承UserCreationForm 再加上 Email 字段
class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        # 与models建立了依赖关系
        model = User
        # 字段
        fields = ['username', 'email', 'password1', 'password2']