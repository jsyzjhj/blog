from django.conf.urls import url
from . import views

app_name='diao'
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$',views.detial,name='detial'),
    url(r'^archives/(?P<year>[0-9]{1,2})/$',views.archives,name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$',views.category,name='category')
]
