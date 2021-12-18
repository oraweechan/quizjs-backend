from django.db import models
from django.contrib.auth import get_user_model


class Quiz(models.Model):
  difficulty = models.CharField(max_length=100)
  owner = models.ForeignKey(
      get_user_model(),
      blank=True,
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return  {self.difficulty}