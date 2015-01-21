from django.db import models
from django.utils import timezone

# Create your models here.
# ForeignKey is always a number - it maps to a UID

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(null=True, blank=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		# return self.title
		return "{}: {}".format(self.author, self.title)