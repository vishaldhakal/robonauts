from django.db import models

class video(models.Model):
    video_link = models.CharField(max_length=10000)
    video_title = models.CharField(max_length=400)
    video_subtitle = models.CharField(max_length=400)

    def __str__(self):
        return self.video_title
