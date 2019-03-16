from django.db import models
from tinymce.models import HTMLField


# 创建自己的模板
class User(models.Model):
    """ 用户表 """
    Username = models.CharField(max_length=128, unique=True, verbose_name=u"用户名")
    Password = models.CharField(max_length=256, verbose_name=u"密码")
    Email = models.EmailField(unique=True, verbose_name=u"邮箱")
    # True代表男
    Gender = models.BooleanField(default=True, verbose_name=u"性别")
    # , verbose_name=u"创建时间"
    Create_time = models.DateTimeField(auto_now_add=True)
    # , verbose_name = u"最后一次修改时间"
    Last_time = models.DateTimeField(auto_now=True)
    User_head = models.CharField(max_length=256, verbose_name=u"头像地址", default="/static/images/h.jpg")

    def __str__(self):
        return self.Username

    class Meta:
        db_table = "blog_user"
        ordering = ['id']

    @classmethod
    def create_user(cls, name, password, email, gender):
        user = cls(Username=name, Password=password, Email=email, Gender=gender)
        return user


class AboutMe(models.Model):
    About_name = models.CharField(verbose_name=u"标题", max_length=255, null=True)
    About_content = HTMLField(verbose_name=u'正文', null=True)
    Create_time = models.DateTimeField(auto_now_add=True)
    Last_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.About_content

    class Meta:
        db_table = "blog_about"


class Note(models.Model):
    # NoteObject = models.Manager()
    Note_name = models.CharField(verbose_name=u"标题", max_length=255)
    Note_author = models.CharField(verbose_name=u"作者", max_length=20)
    Note_summary = models.CharField(verbose_name=u"概述", max_length=255, null=True)
    Note_content = HTMLField(verbose_name=u'正文')
    Note_scr = models.CharField(verbose_name=u"图片地址", max_length=255, null=True)
    Note_href = models.CharField(verbose_name=u"Blog地址", max_length=255, null=True)
    Create_time = models.DateTimeField(auto_now_add=True)
    Last_time = models.DateTimeField(auto_now=True)

    # 用str方法在admin系统中使数据能够一一对应
    def __str__(self):
        return self.Note_name

    class Meta:
        db_table = "blog_note"
        ordering = ['id']

    @classmethod
    def save_note(cls, name, author, summary, content, src, href, create_time, last_time):
        note = cls(Note_name=name, Note_author=author, Note_summary=summary, Note_content=content, Note_scr=src,
                   Note_href=href, Create_time=create_time, Last_time=last_time)
        return note


class Message(models.Model):
    User_name = models.CharField(max_length=20, verbose_name=u"用户名")
    # 最大长度和字段名称
    email = models.EmailField(verbose_name=u"邮箱")
    address = models.CharField(max_length=100, verbose_name=u"联系地址")
    message = models.CharField(max_length=200, verbose_name=u"留言信息")
    Create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "blog_message"     # 数据表名称
        ordering = ['id']

# class Diary(models.Model):
#     Diary_name = models.CharField(verbose_name=u"标题", max_length=255)
#     Diary_author = models.CharField(verbose_name=u"作者", max_length=20)
#     Diary_summary = models.CharField(verbose_name=u"概述", max_length=255, null=True)
#     Diary_content = HTMLField('正文')
#     Diary_time = models.DateTimeField(verbose_name=u"时间")
#     Diary_scr = models.CharField(verbose_name=u"图片地址", max_length=255, null=True)
#     Diary_href = models.CharField(verbose_name=u"链接网址", max_length=255, null=True)
#     # 用str方法在admin系统中使数据能够一一对应
#
#     def __str__(self):
#         return self.Diary_name
#
#     class Meta:
#         db_table = "Diary"
