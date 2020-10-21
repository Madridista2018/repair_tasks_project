from django.contrib import admin
from django.urls import path,include
from todolist_app import views as todolist_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('todolist_app.urls')),#后面接todolist_app的url
    path('account/',include('users_app.urls')),
    path('contact',todolist_view.contact, name = 'contact'),
    path('about-us',todolist_view.about, name = 'about'), #name= 后接view里被分发的函数,第一个是url路径
    path('index',todolist_view.index, name = 'index'),#每个网站的主页都命名为index
]
