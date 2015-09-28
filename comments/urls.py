from django.conf.urls import url
from . import views




urlpatterns = [
	url(r'^comment-create/(?P<object_id>\d+)$', views.CommentCreateView.as_view(), name='comment_create'),
	url(r'^(?P<pk>\d+)$', views.CommentListView.as_view(), name='comment_list'),
]
