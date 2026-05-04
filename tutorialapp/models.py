from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}: {self.comment[:20]}..."
    