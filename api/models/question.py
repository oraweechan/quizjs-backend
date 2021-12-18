from django.db import models
from .quiz import Quiz


class Question(models.Model):
	quiz = models.ForeignKey(
		Quiz, 
		related_name='questions', 
		on_delete=models.CASCADE
	)
	prompt = models.CharField(max_length=255, default='')

	def __str__(self):
		return self.prompt