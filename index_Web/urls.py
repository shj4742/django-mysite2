from django.conf.urls import url
from django.conf.urls import include

from . import views

# app_name  类似 namespace

app_name = 'index_Web'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^find_doctor/$',     views.find_doctor, name='find_doctor'),
    url(r'^classic_answer/$',  views.classic_answer, name='classic_answer'),
    url(r'^health_info/$',     views.health_info, name='health_info'),
    url(r'^repository/$',      views.repository, name='repository'),
    url(r'^login/',views.login, name='login'),
    url(r'^registe_handle/', views.registe_handle, name='registe_handle'),
    url(r'^register/', views.registe, name='registe')
]