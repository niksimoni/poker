from django import forms
from api.validators import check_password_length
from django.contrib.auth.models import User #, Group
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from api.models import Post, Comment


class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'image', 'content']
 


class UserForm(UserCreationForm):
	password1 = forms.CharField(validators=[check_password_length],widget=forms.PasswordInput)
	
	class Meta:
		model = User
		fields = ['username', 'password'] 
	

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['content']

