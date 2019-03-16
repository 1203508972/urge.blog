from django.contrib import admin
from .models import *
# Register your models here.


# 注册
@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ['id', 'Username', 'Password', 'Email', 'Gender', 'Create_time', 'Last_time']
    search_fields = ['Username', 'id']


@admin.register(AboutMe)
class AdminAbout(admin.ModelAdmin):
    list_display = ['id', 'About_name', 'Create_time', 'Last_time']
    # 搜索字段
    search_fields = ['About_name']
    # 过滤字段 list_filter = ['About_name']
    #  分页 list_per_page = 10   ->10个数据为一页


@admin.register(Note)
class AdminNote(admin.ModelAdmin):
    list_display = ['id', 'Note_name', 'Note_author', 'Note_summary', 'Create_time', 'Last_time']
    search_fields = ['Note_name', 'id']
    list_per_page = 10


@admin.register(Message)
class AdminMessage(admin.ModelAdmin):
    list_display = ['User_name', 'email', 'message', 'Create_time']
    search_fields = ['User_name']
    list_per_page = 10

# class UserProfileAdmin(admin.ModelAdmin):
    # 定义admin总览里每行的显示信息
    # list_display = ['cname', 'username', 'email']
    # 定义搜索框以哪些字段可以搜索
    # search_fields = ['cname', 'username']
# 引用的固定格式，注册的model和对应的Admin，Admin放在后边
# 同样还有noregister方法：比如admin.site.noregister(Group)，把group这个表在admin中去掉（默认user和group都是注册到admin中的）

# class diary(admin.ModelAdmin):
#     list_display = ['id', 'Dname', 'Dauthor', 'Dsummary', 'Dtime']
#     list_filter = ['Dname']
#     search_fields = ['Dname']
#     list_per_page = 10
