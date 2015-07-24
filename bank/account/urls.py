from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from account import views

urlpatterns = patterns('',
	url(r'^$', views.Home.as_view(), name='home'), 
	url(r'^about/$', login_required(views.About.as_view(), login_url='/admin/login'), name='about'), 
	url(r'^account/create/', login_required(views.CreateAccount.as_view(), login_url='/admin/login'), name='create_account'),
)
