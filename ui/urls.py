from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from ui import views


urlpatterns = [
	url(r'^$', views.Index.as_view(), name='ui'),
	url(r'^createuser$', views.CreateUser.as_view(), name='createuser'),
	url(r'^login$', views.Login.as_view(), name='login'),
	url(r'^contact$', views.Contact.as_view(), name='contact'),
	url(r'^poker$', views.Poker.as_view(), name='poker'),
	url(r'^betting$', views.Betting.as_view(), name='betting'),
	url(r'^trading$', views.Trading.as_view(), name='trading'),
	url(r'^storia$', views.Storia.as_view(), name='storia'),
	url(r'^(?P<post>(\w|\-)+)$', views.Post.as_view(), name='post'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
     