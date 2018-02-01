from django.conf.urls import url
from . import views

app_name = 'main'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'ask-question/$', views.question, name='ask-question'),
    url(r'^details/(?P<slug>[.\-\w]+)$', views.details, name='details'),
    url(r'^delete/(?P<slug>[.\-\w]+)/$', views.delete, name='delete'),
    url(r'^edit/(?P<slug>[.\-\w]+)/$', views.edit_details, name='edit'),
    url(r'^answer/(?P<slug>[.\-\w]+)/$', views.answer, name='answer'),
    url(r'^answer/update/(?P<slug>[.\-\w]+)/$', views.update_answer, name='update_answer'),
    url(r'^answer/delete/(?P<slug>[.\-\w]+)/$', views.delete_answer, name='delete_answer'),
    url(r'^questions/filter/(?P<tag>[.\-\w]+)/$', views.filter_types, name='filter'),
    url(r'^website-tutorial/$', views.tutorial, name='tutorial'),
    url(r'^request/topic/$', views.request_topic, name='request_topic'),
    url(r'^display/requests/$', views.display_request, name='display_request'),
    url(r'^details/(?P<slug>[.\-\w]+)/(?P<id>\d+)/satisfied/$', views.satisfied, name='satisfied'),
]
