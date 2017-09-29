from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from api import views

urlpatterns = [
	url(r'^messages$', views.Messages.as_view(), name='messages'),
	url(r'^posts$', views.BlogCollectionView.as_view(), name='post-collection'),
	url(r'^poker$', views.Poker.as_view(), name='poker'),
	url(r'^betting$', views.Betting.as_view(), name='betting'),
	url(r'^trading$', views.Trading.as_view(), name='trading'),
	url(r'^fullpoker$', views.FullPoker.as_view(), name='poker'),
	url(r'^fullbetting$', views.FullBetting.as_view(), name='betting'),
	url(r'^fulltrading$', views.FullTrading.as_view(), name='trading'),
	url(r'^posts/(?P<post_pk>\d+)$', views.DetailView.as_view(), name='post-detail'),
	url(r'^(?P<token>(\w|\-)+)/post$', views.CreatePost.as_view(), name='post editing'),
	url(r'^(?P<token>(\w|\-)+)/posts/(?P<post_pk>\d+)$', views.BlogDetailView.as_view(), name='post-detail'),
	url(r'^posts/(?P<post_pk>\d+)/comments$',views.BlogPostComments.as_view(),name='comment-collection'),
	url(r'^comments/(?P<comment_pk>\d+)/comments$',views.CommentDetail.as_view(),name='comment-detail')
]
