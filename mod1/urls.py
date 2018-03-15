from django.conf.urls import url
from . import views
from mod1 import views as core_views
from django.contrib.auth.views import logout
app_name = 'mod1'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', core_views.register, name='register'),
    url(r'^home/$', views.home, name='home'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
     url(r'^oracle/$', views.oracle, name='oracle'),
     url(r'^mysql/$', views.mysql, name='mysql'),
     url(r'^mariadb/$', views.mariadb, name='mariadb'),
      url(r'^postgres/$', views.postgres, name='postgres'),
      url(r'^mysqllambda/$', views.mysqllambda, name='mysqllambda'),
 
 

    ]