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
    url(r'^user/change_password/$', login_required(auth.password_change), {'post_change_redirect' : '/','template_name': 'account/change_password.html'}, name='change_password'),
    url(r'^update-profile/(?P<user>[.\-\w]+)/$', views.update_profile, name='update_profile')


]
