from django.conf.urls import url
from . import views
urlpatterns = [

    # 主页
    url(r'^$', views.index),
    url(r'^index/$', views.index, name="index"),

    # 关于我
    url(r'^about/$', views.about, name="about"),

    # 留言板
    url(r'^message/$', views.message, name="message"),

    # 登陆
    url(r'^login/$', views.login, name="login"),
    # 注册
    url(r'^register/$', views.register, name="register"),
    # 注销
    url(r'^logout/$', views.logout, name="logout"),


    # 心得笔记
    url(r'^study_notes/$', views.study_note, name="study_notes"),
    url(r'^study_notes/(\d+)/$', views.study_note_pags, name="study_notes_page"),
    url(r'^study_notes/django(\d+)/$', views.djangos, name="django"),
    url(r'^study_notes/python(\d+)/$', views.pythons, name="python"),
    url(r'^base/$', views.base),

    url(r'^verify_code/$', views.verify_code),

    url(r'^ajaxNote/$', views.ajax_Test),
    url(r'^note_info/$', views.note_info),
]

