from django.db import models
from django.contrib.auth import get_user_model



class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    #author = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    content = models.TextField()
    image = models.URLField(default='https://i.imgur.com/odto5AG.jpg', blank=True, max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='published_stories'
    )

    #def date_published(self):
    #    return self.pub_date.strftime('%B %d %Y')