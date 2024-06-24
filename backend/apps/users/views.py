from django.shortcuts import render
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from engineio import json

from apps.users.models import MyUser
# 引入JsonResponse模块
from django.http import JsonResponse
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def get_users(request):
    try:
        obj_users=MyUser.objects.all().values()
        users=list(obj_users)
        return JsonResponse({'code': 1,'data': users})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': '获取信息错误，具体错误：'+str(e)})

def reg(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        uname = data['username']
        users = MyUser.objects.filter(username=uname)
        if users:
            info = '用户已经存在'
        else:
            # 接收页面传递过来的参数，进行用户新增
            user = MyUser.objects.create_user(username=data['username'], password=data['password'],is_staff=1,is_superuser=0)
            info = '注册成功,请登陆'
        return JsonResponse({"code": 201, "info": info})

def url_reverse(request):
    return  render(request,"")

def user_login(request):
    return render(request,"shop/user_login.html")

def ajax_login_data(request):
    if request.method=="POST":
        data = json.loads(request.body.decode("utf-8"))
        uname=data['username']
        pwd=data['password']
        json_dict={}
        if uname and pwd:  ## 不为空的情况下，查询数据库
            if MyUser.objects.filter(username=uname): #判断用户是否存在
                #如果存在，进行验证
                user=authenticate(username=uname,password=pwd)
                if user: #如果验证通过
                    if user.is_active: #如果用户状态为激活
                        login(request,user) #进行登陆操作，完成session的设置
                        json_dict["name"]=uname
                        json_dict["code"]=1000
                        json_dict["msg"]="登陆成功"
                    else:
                        json_dict["code"]=1001
                        json_dict["msg"]="用户还未激活"
                else:
                    json_dict["code"]=1002
                    json_dict["msg"]="账号密码不对，请重新输入"
            else:
                json_dict["code"]=1003
                json_dict["msg"]="用户账号有误，请查询"
        else:
            json_dict["code"]=1004
            # json_dict["msg"]="用户名或者密码为空"
            json_dict["msg"]=uname+pwd
        return JsonResponse(json_dict)