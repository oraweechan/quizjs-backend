from django.db import models
from .question import Question


class Answer(models.Model):
	question = models.ForeignKey(
		Question, 
		related_name='answers', 
		on_delete=models.CASCADE
	)
	text = models.CharField(max_length=255)
	correct = models.BooleanField(default=False)

	def __str__(self):
		return self.text