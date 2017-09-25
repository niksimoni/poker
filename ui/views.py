from django.shortcuts import render, redirect
from django.views import View
from api.forms import PostForm


class Index(View):
	template = 'Company/index_login.html'

	def get(self, request):
		if not request.user.is_authenticated():
			return redirect("Company:index")
		return render(request, self.template)

class Post(View):
	template = 'Company/post.html'

	def get(self, request, post):
		return render(request, self.template)

class Contact(View):
	template = 'Company/contact.html'

	def get(self, request):
		return render(request, self.template)


class CreateUser(View):
	template = 'Company/register.html'

	def get(self, request):
		return render(request, self.template)


class Login(View):
	template = 'Company/login.html'

	def get(self,request):
		return render(request, self.template)

class Poker(View):
	template = 'Company/poker.html'

	def get(self, request):
		return render(request, self.template)


class Betting(View):
	template = 'Company/betting.html'

	def get(self, request):
		return render(request, self.template)


class Trading(View):
	template = 'Company/trading.html'

	def get(self,request):
		return render(request, self.template)


class Storia(View):
	template = 'Company/storia.html'

	def get(self, request):
		return render(request, self.template)






