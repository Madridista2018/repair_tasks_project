from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone as timezone



class TaskList(models.Model):
    #建立用户与所提交任务的联系，
    # on_delete=models.CASCADE表示用户消失，所有属于其的任务也消失
    manage = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
    task = models.CharField(max_length=50)
    mailNum = models.EmailField()
    phoneNum = models.IntegerField(default = 0)
    building = models.CharField(max_length=50, default = 'a')
    classroomId = models.IntegerField(default = 0)
    repairType = models.CharField(max_length=50, default = 'a')
    #addTime = models.IntegerField(default = 1)
    done = models.BooleanField(default = False)
    #addDate = models.DateTimeField('addDate',default = timezone.now)
    

    def __str__(self):
        return self.task + "-" + str(self.mailNum) + "-" + str(self.phoneNum) + "-" + self.building +str(self.done)
    
#python manage.py makemigrations这个命令是记录我们对models.py的所有改动，并且将这个改动迁移到migrations这个文件下生成一个文件例如：0001文件，
#如果你接下来还要进行改动的话可能生成就是另外一个文件不一定都是0001文件，但是这个命令并没有作用到数据库，这个刚刚我们在上面的操作过程之后已经看到了，
#而当我们执行python manage.py migrate 命令时  这条命令的主要作用就是把这些改动作用到数据库也就是执行migrations里面新改动的迁移文件更新数据库，比如创建数据表，或者增加字段属性
#另外一个需要注意的是这两个命令默认情况下是作用于全局，也就是对所有最新更改的models或者migrations下面的迁移文件进行对应的操作