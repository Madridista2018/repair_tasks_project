from django.shortcuts import render,redirect
from todolist_app.models import TaskList
from todolist_app.form import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required#在登录状态下才能访问
def todolist(request):
    if request.method == "POST":#添加数据
        form = TaskForm(request.POST or None)#实例化表单
        
        if form.is_valid():
            #保存的manage 字段为请求的user
            form.save(commit= False).manage = request.user #form.save()方法中传递一个参数commit，赋值为False，代表不要提交到数据库
            form.save()#保存有效数据，提交给数据库
            messages.success(request,("添加成功"))#添加成功返回消息
        return redirect('todolist')
    else:
        all_tasks = TaskList.objects.all()#接收所有任务对象,一定要加（）
        #user_tasks = TaskList.objects.filter(manage = request.user)#当前显示的任务为登录用户所提交的
        paginator = Paginator(all_tasks, 5)#每页展示5个对象
        page = request.GET.get('pg')#接收request中变量名为pg的值,即request所请求的页数
        all_tasks = paginator.get_page(page)#获取特定page 的task对象，此时all——tasks包含对象个数为5个

        return render(request,'todolist.html',{'all_tasks' : all_tasks})
        #使用render方法将第三个参数中的值替换Template中的指定模板参数，最终返回一个正常的HTML页面。

@login_required
def addtask(request):
    if request.method == "POST":#添加数据
        form = TaskForm(data = request.POST or None)
        print(form)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            #保存的manage 字段为请求的user
            form.save(commit=  False).manage = request.user #form.save()方法中传递一个参数commit，赋值为False，代表不要提交到数据库
            form.save()#保存有效数据，提交给数据库
            messages.success(request,("添加成功"))#添加成功返回消息
            
        return redirect('todolist')
    else:
        all_tasks = TaskList.objects.all()#接收所有任务对象,一定要加（）
        
        return render(request,'addtask.html',{'all_tasks' : all_tasks})
        

@login_required
def delete_task(request, task_id):
    task = TaskList.objects.get(pk = task_id )#获取id为task——id的对象
    if task.manage == request.user:
        task.delete()
    else:
        messages.error(request,("该报修不允许非发起人修改"))
    return redirect('todolist')

@login_required
def detail(request,task_id):
    obj = TaskList.objects.get(pk = task_id)
    print(obj)
    return render(request,'detail.html',{'obj' : obj})#context:　添加到模板上下文的一个字典. 默认是一个空字典. 如果字典中的某个值是可调用的, 视图将在渲染模板之前调用它.

        

    
@login_required
def complete_task(request, task_id):
    task = TaskList.objects.get(pk = task_id )
    if task.manage == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request,("该报修不允许非发起人修改"))
    return redirect('todolist')
@login_required
def pend_task(request, task_id):
    task = TaskList.objects.get(pk = task_id )
    if task.manage == request.user:        
        task.done = False
        task.save()
    else:
        messages.error(request,("该报修不允许非发起人修改"))
    return redirect('todolist')#如何点击pend按钮后仍然留在当前页面而不是返回第一页

@login_required
def edit_task(request, task_id):
    if request.method == "POST":#添加数据
        task = TaskList.objects.get(pk = task_id)
        form = TaskForm(request.POST or None, instance = task)
        if form.is_valid():
            form.save()
        messages.success(request,("修改成功"))#添加成功返回消息
        return redirect('todolist')
    else:
        task_obj = TaskList.objects.get(pk = task_id)
        return render(request,'edit.html',{'task_obj' : task_obj})#context:　添加到模板上下文的一个字典. 默认是一个空字典. 如果字典中的某个值是可调用的, 视图将在渲染模板之前调用它.



def contact(request):
    context = {
        'contact_text' : "联系方式：",

    }
    return render(request,'contact.html',context)

def about(request):
    context = {
        'about_text' : "关于我们：",

    }
    return render(request,'about.html',context)

def index(request):
    context = {
        'index_text' : "主页",

    }
    return render(request,'index.html',context)
