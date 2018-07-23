from django.shortcuts import render
from django.shortcuts import redirect
from .forms import UserForm,RegisterForm
from .models import user_info


# Create your views here.


import hashlib


def hash_code(s, salt='mysite'):  # 加点盐
    h = hashlib.md5()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()


def index(request):
    return  render(request, 'index.html')


def register(request):

    message = ""
    register_form = RegisterForm()
    if request.session.get('is_login'):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            address = register_form.cleaned_data['address']
            email = register_form.cleaned_data['email']
            age = register_form.cleaned_data['age']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'register.html', locals())
            else:
                same_name_user = user_info.objects.filter(username=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'register.html', locals())
                same_email_user = user_info.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'register.html', locals())

                # 当一切都OK的情况下，创建新用户
                new_user = user_info.objects.create()
                new_user.username = username
                new_user.password = hash_code(password1)  # 使用加密密码
                new_user.address = address
                new_user.email = email
                new_user.age = age
                new_user.sex = sex
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    # print(register_form)
    return render(request, 'register.html', locals())


def login(request):
    if request.session.get('is_login'):
        return redirect('/index')

    message = ""
    login_form = UserForm()

    # if request.method == 'POST':
    #     username = request.POST.get('username', None)
    #     password = request.POST.get('password', None)
    #     if username and password:
    #         # username = username.strip()
    #         try:
    #             user = user_info.objects.get(username=username)
    #             if user.password == password:
    #                 return redirect('/index/')
    #             else:
    #                 message = '密码错误'
    #         except:
    #             message='用户名不存在'
    # return render(request, 'login.html', {'message': message})

    ####使用表单方式,他会提前帮你处理数据
    if request.method == 'POST':
        login_form = UserForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = user_info.objects.get(username=username)
                if user.password == hash_code(password):  # 哈希值和数据库内的值进行比对
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.username
                    return redirect('/index/')
                else:
                    message = '密码错误'
            except:
                message='用户名不存在'
        # return render(request, 'login.html', {'message': message, 'login_form':login_form})

    ####get方式的请求会返回原页面
    ####locals()返回当前所有的本地变量字典，存在部分是模板用不到变量
    return render(request, 'login.html', locals())

def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/index/")





user_list=[]
for i in range(1,21):
    user_list.append({"username":"try"+str(i),"sexual":"male","email":"try"+str(i)+"@163.com"})

def home(request):
    if request.method == 'POST':
        u = request.POST.get('username', None)
        s = request.POST.get('sexual', None)
        e = request.POST.get('email', None)
        user_list.append({"username":u,"sexual":s,"email":e})
    return render(request,'home.html',{"user_list":user_list})
