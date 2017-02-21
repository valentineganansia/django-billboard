from django.conf.urls import url
from django.contrib.auth import views as authviews

from . import views
urlpatterns =[
    url(r'^$',views.index, name='index'),
    url(r'^newpost$', views.newpost, name='newpost'),
    url(R'^login/$', authviews.login, name='login'),
    url(R'^logout/$', authviews.logout, {'next_page': 'index'}, name='logout'),

]