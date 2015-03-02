from django.conf.urls import patterns, url
from site_one import views

urlpatterns = patterns('',
	          url(r'^$', views.index, name='index'),
	          url(r'^blogpost/(?P<blog_title_url>\w+)/$', views.blog, name='blog'),
	          url(r'^add_post/$', views.add_post, name='add_post'),
	          url(r'^register/$', views.register, name='register'),
	          url(r'^login/$', views.user_login, name='login'),
	          url(r'^logout/$', views.user_logout, name='logout'),
	          url(r'^about/$', views.about, name='about')
	          )