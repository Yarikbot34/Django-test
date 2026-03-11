from django.db import models

# Create your models here.
class Publication(models.Model):
    name = models.CharField(max_length = 250)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name