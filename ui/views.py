from django.shortcuts import render, redirect
from django.views import View
from api.forms import PostForm

class Index(View):
	template = 'api/index.html'

	def get(self, request):
		return render(request, self.template)

class Post(View):
	template = 'api/post.html'

	def get(self, request, post):
		return render(request, self.template)


class CreateUser(View):
	template = 'ui/create_user.html'

	def get(self, request):
		return render(request, self.template)


class Login(View):
	template = 'ui/login.html'

	def get(self,request):
		return render(request, self.template)





