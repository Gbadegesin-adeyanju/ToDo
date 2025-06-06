from django.db import models

# Create your models here.

class ToDo(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description}"
