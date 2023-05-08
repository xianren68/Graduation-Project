from django.db import models
# Create your models here.
# 创建用户模型类
class User(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    avatar = models.CharField(max_length=40)
    permissions = models.IntegerField()
    def __str__(self):
        return self.name
    class Meta:
        magaged:True
        db_table = 'user'

# 添加用户      
def saveUser(user:User):
    # 查询是否存在
    try:
        user = User.objects.get(name=user.name)
        return 1003
    except:
        user.save()
        return 200
        
# 查询用户
def getUser(name:str,password:str)->int:
    try:
        user = User.objects.get(name=name)
    except:
        return 1001
    if user.password == password:
        return 200
    else:
        return 1002
# 获取头像
def getAva(name:str)->str:
    user = User.objects.get(name=name)
    return user.avatar

# # 修改用户
# def editUser(newData:dict)->int:
#     old = User.objects.get(name=newData.name)
#     # 删除头像