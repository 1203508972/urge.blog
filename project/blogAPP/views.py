from django.contrib.sessions import serializers
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from .froms import *
from .models import *
import math
from django.core.paginator import Paginator


# 主页
def index(request):
    NoteList = Note.objects.all()[0:7]
    RecommendNoteList = Note.objects.all()[0:3]
    # 把模型中的数据传递给模板，模板再渲染页面将渲染好的页面返回给浏览器
    RecommendNote = Note.objects.filter(pk__in=[21, 22])
    return render(request, 'blogAPP/index.html',
                  {"notes": NoteList,
                   "Recommend_notes": RecommendNoteList,
                   "Recommend_note_topic": RecommendNoteList[0],
                   "RecommendNotes": RecommendNote})


# 关于我
def about(request):
    # AboutList = AboutMe.objects.get(pk=1)
    return render(request, 'blogAPP/menu/about.html', )
    # {"about": AboutList}


# 心得笔记
def study_note(request):
    allList = Note.objects.all()
    paginator = Paginator(allList, 7)
    page = paginator.page(1)
    return render(request, 'blogAPP/menu/study_notes.html',
                  {"notes": page,
                   "Recommend_notes": page[0:3],
                   "Recommend_note_topic": page[0]})


def study_note_pags(request, pageid):

    # 0-8 8-16
    # NoteList = Note.objects.all()[(page - 1) * 7:(page * 7)]
    # Notes = Note.objects.all()
    # p = math.ceil(len(Notes) / 7)
    # pages = []
    # for i in range(1, p + 1):
    #     pages.append(i)
    allList = Note.objects.all()
    paginator = Paginator(allList, 7)
    page = paginator.page(pageid)
    return render(request, 'blogAPP/menu/study_notes.html',
                  {"notes": page,
                   "Recommend_notes": page[0:3],
                   "Recommend_note_topic": page[0]})


# 留言
def message(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        send_message = request.POST.get('message', '')

        user_message = Message()
        user_message.name = name
        user_message.email = email
        user_message.address = address
        user_message.message = send_message
        user_message.save()
        return redirect('/message/')

    List = Message.objects.all()
    return render(request, 'blogAPP/menu/message.html',
                  {"list": List})


# 登陆
def login(request):
    if request.session.get('is_login', None):
        return redirect('/index')

    if request.method == "POST":
        login_form = UserForm(request.POST)
        back_message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = User.objects.get(Username=username)
                if user.Password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.Username
                    request.session['user_head'] = user.User_head
                    request.session.set_expiry(0)
                    return redirect('/index/')
                else:
                    back_message = "密码不正确！"
            except():
                back_message = "用户不存在！"
        return render(request, 'blogAPP/login/login.html', locals())

    login_form = UserForm()
    return render(request, 'blogAPP/login/login.html', locals())


# 注册
def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        back_message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                back_message = "两次输入的密码不同！"
                return render(request, 'blogAPP/login/register.html', locals())
            else:
                same_name_user = User.objects.filter(Username=username)
                if same_name_user:  # 用户名唯一
                    back_message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'blogAPP/login/register.html', locals())
                same_email_user = User.objects.filter(Email=email)
                if same_email_user:  # 邮箱地址唯一
                    back_message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'blogAPP/login/register.html', locals())

                # 当一切都OK的情况下，创建新用户
                # DataTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                # new_user = User()
                # new_user.Username = username
                # new_user.Password = password1
                # new_user.Email = email
                # new_user.Gender = sex
                # new_user.Create_time = DataTime
                # new_user.Last_time = DataTime
                # new_user.User_head = "/static/images/h.jpg"
                new_user = User.create_user(username, password1, email, sex)
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'blogAPP/login/register.html', locals())

    # if request.session.get('is_login', None):
    #     return redirect("/index/")
    # if request.method == 'POST':
    #     back_message = "请检查填写的内容！"
    #     username = request.POST.get("username", '')
    #     password1 = request.POST.get("password1", '')
    #     password2 = request.POST.get("password2", '')
    #     email = request.POST.get("email", '')
    #     gender = request.POST.get("gender", '')
    #     if password1 == password2:
    #         same_user_name = User.objects.filter(username=username)
    #         if same_user_name:
    #             back_message = "用户名不唯一，请修改您的用户名！"
    #             return render(request, 'blogAPP/login/register.html', locals())
    #         else:
    #             same_email = User.objects.filter(email=email)
    #             if same_email:
    #                 back_message = "邮箱信息不唯一，请重新输入！"
    #                 return render(request, 'blogAPP/login/register.html', locals())
    #             else:
    #                 new_user = User.create_user(username, password1, email, gender)
    #                 new_user.save()
    #     else:
    #         back_message = "两次输入的密码不相同，请重新输入！"
    #         return render(request, 'blogAPP/login/register.html', locals())


# 登出
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


# 心得内容页
def djangos(request, page):
    page = int(page)
    DjangoNoteList = Note.objects.get(pk=page)
    return render(request, 'blogAPP/note/note.html', {"Note": DjangoNoteList})


# python的内容页
def pythons(request, page):
    page = int(page)
    PythonNoteList = Note.objects.get(pk=(page + 20))
    return render(request, 'blogAPP/note/note.html', {"Note": PythonNoteList})


def base(request):
    return render(request, 'blogAPP/base.html')


def verify_code(request):
    # 引入绘图模块
    from PIL import Image, ImageDraw, ImageFont
    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色、宽、高
    bg_color = (random.randrange(20, 100), random.randrange(
        20, 100), random.randrange(20, 100))
    width = 100
    height = 50
    # 创建画面对象
    im = Image.new('RGB', (width, height), bg_color)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str = '1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str[random.randrange(0, len(str))]
    # 构造字体对象
    font = ImageFont.truetype(r'C:\Windows\Fonts\consola.ttf', 50)
    # 构造字体颜色
    font_color1 = (255, random.randrange(0, 255), random.randrange(0, 255))
    font_color2 = (255, random.randrange(0, 255), random.randrange(0, 255))
    font_color3 = (255, random.randrange(0, 255), random.randrange(0, 255))
    font_color4 = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=font_color1)
    draw.text((25, 2), rand_str[1], font=font, fill=font_color2)
    draw.text((50, 2), rand_str[2], font=font, fill=font_color3)
    draw.text((75, 2), rand_str[3], font=font, fill=font_color4)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    # request.session['verify_code'] = rand_str
    # 内存文件操作
    import io
    buf = io.BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')


def ajax_Test(request):

    return render(request, 'blogAPP/ajaxTest.html')


def note_info(request):
    notes = Note.objects.all().values('Note_name', "Note_author", "Note_summary")
    note = list(notes)
    return JsonResponse({"data": note})

