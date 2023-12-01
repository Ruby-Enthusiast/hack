from django.db import models

# Create your models here.

class Comment(models.Model):
    author = models.CharField(max_length=100)
    text = models.TextField()
    password = models.CharField(max_length=20)  # Add a password field
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.author} - {self.created_at}'