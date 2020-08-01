from django.db import models


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    content = models.TextField()
    image = models.URLField()

    #def date_published(self):
    #    return self.pub_date.strftime('%B %d %Y')