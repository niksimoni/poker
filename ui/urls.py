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
	url(r'^(?P<post>(\w|\-)+)$', views.Post.as_view(), name='post'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
     