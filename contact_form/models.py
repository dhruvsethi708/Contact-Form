
from django.db import models
from django.utils import timezone

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
