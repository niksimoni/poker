import json
from django.http import JsonResponse
from django.views import View
from django.http import HttpResponseNotAllowed
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from api.models import Post
from api.forms import PostForm, UserForm, CommentForm
from users.models import UserProfile
from api.models import Comment


def unix_timezone(date):
	epoch = timezone.datetime.fromtimestamp(0, timezone.get_current_timezone())
	return (date - epoch).total_seconds()*1000


class BlogCollectionView(View):
	
	def _to_json(self, posts):
		return {
			'posts': [{
				'pk': post.pk,
				'title': post.title,
				'image': post.image.url,
				'content': post.content,
				'user': post.user.username,
				'created_at': unix_timezone(post.created_at),
			} for post in posts]
		}

	
	def get(self, request):
		posts = Post.objects.all()
		return JsonResponse(self._to_json(posts))


class CreatePost(View):
	form_class = PostForm
	

	def post(self, request, token):
		userprofile = UserProfile.objects.get(token=token) #get in database
		form = self.form_class(request.POST, request.FILES)
		if form.is_valid():
			form.instance.user = userprofile.user
			post = form.save()
			return JsonResponse({
				'pk': post.pk, 
				"post": {
					'pk': post.pk,
					'title': post.title,
					'image': post.image.url,
					'content': post.content,
					'user': post.user.username,
					'created_at': unix_timezone(post.created_at),
				}
			})

		else:
			print(form.errors)
			context = {'PostForm' : form.errors.as_json()}
			return JsonResponse(context, status=422)
	

class BlogDetailView(View):
	form_class = PostForm

	def _to_json(self, posts):
		return {
			'posts': [{
				'pk': post.pk,
				'title': post.title,
				'image': post.image.url,
				'content': post.content,
				'user': post.user.username,
				'created_at': unix_timezone(post.created_at),
			} for post in posts]
		}

	
	def get(self, request, post_pk):
		posts = [Post.objects.get(pk=post_pk)]
		return JsonResponse(self._to_json(posts))


	
	def put(self, request, token, post_pk):
		userprofile = UserProfile.objects.get(token=token)
		post = Post.objects.get(pk = post_pk, user = userprofile.user)
		data = json.loads(request.body.decode()) #request.body only for API to grab
		form = self.form_class(data=data, instance=post)
		if form.is_valid():
			post = form.save()
			return JsonResponse({'pk': post.pk})
		else:
			context = {'PostForm' : form.errors.as_json()}
			return JsonResponse(context, status=422)


	def delete(self, request, post_pk, token):
		userprofile = UserProfile.objects.get(token=token)
		post = Post.objects.get(pk = post_pk, user = userprofile.user)
		post.delete()
		return JsonResponse({'pk': post.pk}) #pk not needed on index page


class BlogPostComments(View):

	def get(self, request, post_pk):
		post = Post.objects.get(pk = post_pk)
		comments = post.comments.all()
		return JsonResponse(self._to_json(comments))

	def _to_json(self, comments):
		return {
			'comments': [{
				'pk': comment.pk,
				'content': comment.content,
				'user': comment.user.username,
				'created_at': unix_timezone(comment.created_at),
			} for comment in comments] 
		}

	def post(self, request, token, post_pk):
		userprofile = UserProfile.objects.get(token=token) #get in database
		data = json.loads(request.body.decode()) #request.body only for API to grab
		print(data)
		post = Post.objects.get(pk = post_pk)
		form = CommentForm(data) #called from model direct no self
		if form.is_valid():

			form.instance.user = userprofile.user
			comment = form.save(commit=False)
			comment.content_object = post
			comment.save()
			return JsonResponse({'pk': comment.pk})
		else:
			context = {'CommentForm' : form.errors.as_json()}
			return JsonResponse(context, status=422)

class CommentDetail(View):


	def get(self, request, comment_pk):

		comment = Comment.objects.get(pk = comment_pk)
		comments = comment.comments.all()
		return JsonResponse(self._to_json(comments))
	
	def _to_json(self, comments):
		return {
			'comments': [{
				'pk': comment.pk,
				'content': comment.content,
				'user': comment.user.username,
				'created_at': unix_timezone(comment.created_at),
			} for comment in comments] 
		}

	def post(self, request, token, comment_pk):
		userprofile = UserProfile.objects.get(token=token)

		comment = Comment.objects.get(pk=comment_pk)
		data = json.loads(request.body.decode()) #request.body only for API to grab
		form = CommentForm(data) #called from model direct no self
		if form.is_valid():

			form.instance.user = userprofile.user
			new_comment = form.save(commit=False)
			new_comment.content_object = comment
			new_comment.save()
			return JsonResponse({'pk': comment.pk})
		else:
			context = {'CommentForm' : form.errors.as_json()}
			return JsonResponse(context, status=422)
