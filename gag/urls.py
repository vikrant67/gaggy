from django.conf.urls import url
from . import views

app_name='gag'
urlpatterns = [

    #/gag/
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^logout/$', views.logout_user, name='logout_user'),
    url(r'^login/$', views.login_user, name='login_user'),
    url(r'^like/$', views.like, name='like'),
    url(r'^dislike/$', views.dislike, name='dislike'),
    url(r'^upload/$', views.UploadFormView.as_view(), name='upload'),
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^postcomment/$', views.post_comment, name='post-comment'),
    url(r'^showcomment/$', views.show_comments, name='show-comment'),

]

