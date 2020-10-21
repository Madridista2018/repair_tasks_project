from django import forms
from todolist_app.models import TaskList
#TaskForm 继承 ModelForm,
#如果我们在models里设计数据库时，已经设计好了一个类(就是数据库的表)之后想复用这个类的信息来作为表单的模型
class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ['task', 'done']