from django.db import models
from django.contrib.auth import get_user_model

class Category(models.Model):
    name = models.CharField(max_length = 30, unique=True)
    author = models.ForeignKey(
        get_user_model(),
        related_name='categories',
        on_delete=models.SET_NULL,
        null=True
    )
    def __str__(self):
        return str(self.id) + "-" + self.name


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    #author = models.CharField(max_length=200)
    pub_date = models.DateTimeField()#auto_now_add=True
    edited = models.DateTimeField(auto_now=True,null=True)
    content = models.TextField()
    image = models.URLField(default='https://i.imgur.com/odto5AG.jpg', blank=True, max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='published_stories'
    )
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL,
        null=True,
        related_name = 'cat_stories')

    #def date_published(self):
    #    return self.pub_date.strftime('%B %d %Y')

# class Tags(models.Model):
#     name = models.CharField(max_length = 30, unique=True)


