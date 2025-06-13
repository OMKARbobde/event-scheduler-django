from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.title

