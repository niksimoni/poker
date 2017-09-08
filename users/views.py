import json

from django.views import View
from django.http import JsonResponse
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from users.models import UserProfile



class CreateUser(View):

	def get(self, request, token):
		pass

	def __serialize(self, userprofile):
		return {
			"token": userprofile.token
		}

	def post(self, request):
		data = json.loads(request.body.decode())
		newuser = User.objects.create_user(
			username = data["username"],
			password = data["password"]
		)

		userprofile = UserProfile.objects.create(user = newuser)
		return JsonResponse(self.__serialize(userprofile))


class Login(View):
	
	def __serialize_user(self, user):
		return {
			"token": user.token
		}	


	def post(self, request):

		data = json.loads(request.body.decode())
		username = data['username']
		password = data['password']

		user = authenticate(request, username=username, password=password)

		if user:
			userprofile = UserProfile.objects.get(user = user)
			login(request, user)
			return JsonResponse(self.__serialize_user(userprofile), status=200)
				
		else:
			return JsonResponse({"error_message":"wrong login details"}, status=401)



def unix_timezone(date):
	epoch = timezone.datetime.fromtimestamp(0, timezone.get_current_timezone())
	return (date - epoch).total_seconds()*1000


