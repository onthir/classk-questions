from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth

app_name = 'accounts'
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/(?P<user>[.\-\w]+)$', views.profile, name='profile'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^update-profile/(?P<user>[.\-\w]+)/$', views.update_profile, name='update_profile'),
    url(r'all-questions/(?P<user>[.\-\w]+)/$', views.all, name='all'),
    url(r'all-answers/(?P<user>[.\-\w]+)/$', views.all2, name='all2')



]
