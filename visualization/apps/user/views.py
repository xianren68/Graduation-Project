from django.shortcuts import render
from utils import error,save,encryption
from . import models
from django.http import HttpResponse, JsonResponse
# Create your views here.
# 接收前端的数据并调用数据库操作


# 登录
def login(request):
    name = request.GET.get('name')
    password = request.GET.get('password')
    password = encryption.encryption(password)
    code = models.getUser(name,password)
    # 要返回的数据
    data = {}
    data['code'] = code
    data['msg'] = error.getMsg(code)
    response = HttpResponse(JsonResponse(data))
    if code == 200 :
        # cookie携带用户名及头像
            # 用户名
            response.set_cookie('name',name,max_age=60*60*12)
            # 头像
            response.set_cookie('avatar','http://localhost:5000/static/avatar/'+models.getAva(name),max_age=60*60*12)
            return response
    return response

# 注册
def register(request):
    if request.method == "POST":
        # 获得前端的用户名，用户密码和头像
        user = models.User()
        user.name = request.POST['name']
        user.password = request.POST['password']
        user.permissions = int(request.POST['permissions'])
        avatar = request.FILES.get('file')
        # 对密码和图片名进行hash
        if avatar != None :
            fileName = avatar.name
            fileName = encryption.encryption(fileName)+'.'+fileName.split('.')[1]
            if not save.isExists(fileName):
                save.saveProfile(fileName,avatar.read())
            user.avatar = fileName
        user.password = encryption.encryption(user.password)
        # 存入数据库
        code = models.saveUser(user)
        # 返回的数据
        data = {}
        data['code'] = code
        data['msg'] = error.getMsg(code)
        return JsonResponse(data)
        
# 修改用户
def editUserInfo(request):
    if request.method == 'PUT':
        user = models.User()
        user.name = request.POST['name']
        user.password = request.POST['password']
        avatar = request.FILES.get('file')
        if avatar != None :
            fileName = avatar.name
            fileName = encryption.encryption(fileName)+'.'+fileName.split('.')[1]
            if not save.isExists(fileName):
                save.saveProfile(fileName,avatar.read())
            user.avatar = fileName
        user.password = encryption.encryption(user.password)
        # 存入数据库
        code = models.saveUser(user)