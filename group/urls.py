from django.urls import path,re_path
from .views import CreateGroup,GroupListView,GroupDetailView,GroupDeleteView,GroupUpdateView,FollowGroupView

urlpatterns=[
    path('create_group/',CreateGroup.as_view(),name="create_group"),
    path('list_group/',GroupListView.as_view(),name="list_group"),
    re_path(r'^detail_group/(?P<pk>\d+)/$',GroupDetailView.as_view(),name="detail_group"),
    re_path(r'^follow_group/(?P<pk>\d+)/$',FollowGroupView.as_view(),name="follow_group"),
    re_path(r'^delete_group/(?P<pk>\d+)/$',GroupDeleteView.as_view(),name="delete_group"),
    re_path(r'^update_group/(?P<pk>\d+)/$',GroupUpdateView.as_view(),name="update_group"),
]