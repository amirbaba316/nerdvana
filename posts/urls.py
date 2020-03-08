from django.urls import path,re_path
from .views import CreatePost,PostListView,PostDetailView,PostDeleteView,PostUpdateView,CommentPostView,SubCommentPostView,MetaCommentPostView

urlpatterns=[
    re_path(r'^create_post/(?P<pk>\d+)/$',CreatePost.as_view(),name="create_post"),
    path('list_post/',PostListView.as_view(),name="list_post"),
    re_path(r'^detail_post/(?P<pk>\d+)/$',PostDetailView.as_view(),name="detail_post"),
    re_path(r'^delete_post/(?P<pk>\d+)/$',PostDeleteView.as_view(),name="delete_post"),
    re_path(r'^update_post/(?P<pk>\d+)/$',PostUpdateView.as_view(),name="update_post"),
    re_path(r'^post_comment/(?P<pk>\d+)/$',CommentPostView.as_view(),name="post_comment"),
    re_path(r'^post_sub_comment/(?P<pk>\d+)/$',SubCommentPostView.as_view(),name="post_sub_comment"),
    re_path(r'^post_meta_comment/(?P<c_pk>\d+)/(?P<s_pk>\d+)/$',MetaCommentPostView.as_view(),name="post_meta_comment"),

]