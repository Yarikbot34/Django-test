from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Publication(models.Model):
    name = models.CharField(max_length = 250)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='articles')

    def __str__(self):
        return self.name