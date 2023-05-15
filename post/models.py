from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model to be created by staff
    Default image set so that we can always reference image.url.
    """
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to="images/", default='../default_post_sqpxy8', blank=True,)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f'{self.id} {self.title}'
