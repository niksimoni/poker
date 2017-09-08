import uuid
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
	user = models.OneToOneField(User)
	token = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	tags = GenericRelation('api.TaggedItem', related_query_name="userprofile_set")

