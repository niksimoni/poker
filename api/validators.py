from django.core.exceptions import ValidationError

def check_password_length(value):
	if len(value) <= 7:
		raise ValidationError('Password too short, has to be greater than 8 characters')
		