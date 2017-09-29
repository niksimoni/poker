from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length =30, unique=True)
	image = models.ImageField(upload_to='posts/')
	content = models.TextField()
	slug = models.SlugField(max_length =50)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True )
	subject = models.CharField(max_length =30)
	tags = GenericRelation('api.TaggedItem', related_query_name="post_set")
	comments = GenericRelation('api.Comment', related_query_name="comment_set")


class TaggedItem(models.Model):
	tag = models.SlugField()
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

class Comment(models.Model):    
	user = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add = True)
	content = models.TextField()
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')	
	comments = GenericRelation('api.Comment', related_query_name="comment_set")

class Message(models.Model):
	name = models.TextField()
	email = models.EmailField(max_length=254)
	subject = models.TextField()
	message = models.TextField()
	created_at = models.DateTimeField(auto_now = True)

