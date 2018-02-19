from django.conf.urls import url
from . import views

app_name='comments'
urlpatterns=[
    url(r'^comment/post/(?P<post_pk>\d+)/$',views.postComment,name='postComment')
]