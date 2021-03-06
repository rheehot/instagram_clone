from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField,ImageSpecField
from imagekit.processors import Thumbnail,ResizeToFill
# Create your models here.


class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    # image = models.ImageField(upload_to="%Y/%m/%d/",blank=True)
    image = ProcessedImageField(
        blank=True,
        format="JPEG",
        processors=[Thumbnail(614,614)],
        upload_to="%Y/%m/%d/"
    )
    image_thumbnail = ImageSpecField(
        source="image",
        processors=[ResizeToFill(614,614)],
        format='JPEG'
    )
    # image = ProcessedImageField(
    #     blank=True,
    #     format="JPEG",
    #     processors=[Thumbnail(614,614),ResizeToFill(614,614)],
    #     upload_to="%Y/%m/%d/"
    # )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
