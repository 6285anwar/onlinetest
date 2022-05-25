"""onlinetest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from app import views
from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.login,name='login'),
    re_path(r'^register$', views.register,name='register'),


#============ Admin Module ======================
    re_path(r'^admin_logout/$', views.admin_logout,name='admin_logout'),
    re_path(r'^admin_index/$', views.admin_index,name='admin_index'),
    re_path(r'^admin_home/$', views.admin_home,name='admin_home'),
    re_path(r'^admin_user/$', views.admin_user,name='admin_user'),
    re_path(r'^admin_add_subject/$', views.admin_add_subject,name='admin_add_subject'),
    re_path(r'^admin_add_exam/(?P<id>\d+)/$', views.admin_add_exam,name='admin_add_exam'),
    re_path(r'^admin_exams_adding/(?P<id>\d+)/$', views.admin_exams_adding,name='admin_exams_adding'),
    re_path(r'^admin_exam/$', views.admin_exam,name='admin_exam'),
    re_path(r'^admin_add_questions/(?P<id>\d+)/$', views.admin_add_questions,name='admin_add_questions'),
    re_path(r'^admin_view_questions/(?P<id>\d+)/$', views.admin_view_questions,name='admin_view_questions'),
    re_path(r'^admin_question_delete/(?P<id>\d+)/$', views.admin_question_delete,name='admin_question_delete'),
    re_path(r'^admin_exam_delete/(?P<id>\d+)/$', views.admin_exam_delete,name='admin_exam_delete'),  
    re_path(r'^admin_sub_add/$', views.admin_sub_add,name='admin_sub_add'),
    re_path(r'^admin_deletesub/(?P<id>\d+)/$', views.admin_deletesub,name='admin_deletesub'),

#============ User Module ======================
    re_path(r'^user_logout/$', views.user_logout,name='user_logout'),
    re_path(r'^user_index/$', views.user_index, name='user_index'),
    re_path(r'^user_home/$', views.user_home, name='user_home'),
    re_path(r'^user_subject/$', views.user_subject, name='user_subject'),
    re_path(r'^user_exam/(?P<id>\d+)/$', views.user_exam,name='user_exam'),
    re_path(r'^user_exam_attend/(?P<id>\d+)/$', views.user_exam_attend,name='user_exam_attend'),
    re_path(r'^user_answer/$', views.user_answer,name='user_answer'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
