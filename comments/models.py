from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    """
    Comment model to a post by staff
    """
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    class Meta:
        ordering = ["-created_at"]
    
    def __str__(self):
        return self.comment