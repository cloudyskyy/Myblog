from blog import views
from django.conf.urls import url

app_name='blog'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^index$',views.index,name='index1'),
    url(r'^post/(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^archieves/(?P<year>\d{4})/(?P<month>\d{1,2})/$',views.archives,name='archives'),
    url(r'^category/(?P<pk>\d+)/$',views.category,name='category'),
]