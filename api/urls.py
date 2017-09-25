from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from api import views

urlpatterns = [
	url(r'^posts$', views.BlogCollectionView.as_view(), name='post-collection'),
	url(r'^posts/(?P<post_pk>\d+)$', views.DetailView.as_view(), name='post-detail'),
	url(r'^(?P<token>(\w|\-)+)/post$', views.CreatePost.as_view(), name='post editing'),
	url(r'^(?P<token>(\w|\-)+)/posts/(?P<post_pk>\d+)$', views.BlogDetailView.as_view(), name='post-detail'),
	url(r'^posts/(?P<post_pk>\d+)/comments$',views.BlogPostComments.as_view(),name='comment-collection'),
	url(r'^comments/(?P<comment_pk>\d+)/comments$',views.CommentDetail.as_view(),name='comment-detail')
]
