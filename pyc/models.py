from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
	body = models.TextField()
	timestamp = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return self.title