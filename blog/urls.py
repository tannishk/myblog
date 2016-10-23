from django.conf.urls import url,include
from django.contrib import admin
from . import views
app_name = 'blog'
urlpatterns = [
    url(r'^$',views.post_list,name='post_list'),
    url(r'^post/(?P<pk>\d+)/$',views.post_display,name='post_display')
]