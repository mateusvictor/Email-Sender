from django.contrib.auth.models import User
from django.db import models


class Receiver(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	receiver = models.EmailField(max_length=200)

	def __str__(self):
		return self.receiver

