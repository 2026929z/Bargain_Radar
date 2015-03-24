from django.conf.urls import patterns, url,include
from radar import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^basket/$', views.basket, name='basket'),
                       url(r'^blog/$', views.blog, name='blog'),
                       url(r'^checkout/$', views.checkout, name='checkout'),
                       url(r'^contact/$', views.contact, name='contact'),
                       url(r'^details/$', views.details, name='details'),
                       url(r'^error/$', views.error, name='error'),
                       url(r'^login/$', views.showLogin, name='login'),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^shop/$', views.shop, name='shop'),
                       url(r'^single_blog/$', views.single_blog, name='single_blog'),
                       url(r'^user_login/$', views.user_login, name='user_login'),
                       url(r'^user_logout/$', views.user_logout, name='user_logout'),
                       )
