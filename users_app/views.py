from django.shortcuts import render, redirect
from .form import CustomRegisterForm
from django.contrib import messages

def register(request):
    if request.method == "POST":
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()#(1)保存
            messages.success(request,("New User Account Created"))#（2）添加成功返回消息
        return redirect('register')#（3）返回页面
    else:
        register_form = CustomRegisterForm()#Django 已经内置了一个用户注册表单,它关联的是 django 内置的 User 模型
    return render(request, 'register.html', {'register_form' : register_form})
