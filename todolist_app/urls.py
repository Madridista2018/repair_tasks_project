from todolist_app import views
from django.urls import path

urlpatterns = [
    path('',views.todolist, name = 'todolist'),
    path('detail/<task_id>',views.detail, name = 'detail'),
    path('addtask',views.addtask, name = 'addtask'),
    path('delete/<task_id>',views.delete_task, name = 'delete_task'),#每个url分发给每个view,传入task。id
    path('edit/<task_id>',views.edit_task, name = 'edit_task'),
    path('complete/<task_id>',views.complete_task, name = 'complete_task'),
    path('pend/<task_id>',views.pend_task, name = 'pend_task'),

]
