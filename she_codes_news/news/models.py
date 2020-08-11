from django.db import models
from django.conf import settings
import datetime

class Category(models.Model):
    name = models.CharField(max_length = 30, unique=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='categories',
        on_delete=models.SET_NULL,
        null=True
    )
    def __str__(self):
        return self.name
        #return str(self.id) + "-" + self.name

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(null=True,blank=True)#auto_now_add=True
    edit_date = models.DateTimeField(auto_now=True,blank=True,null=True)
    content = models.TextField()
    image = models.URLField(default='https://i.imgur.com/odto5AG.jpg', blank=True, max_length=200)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='published_stories'
        )
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
        related_name = 'cat_stories'
        )
    favourites = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='favourites')

    @property
    def fav_count(self):
        return self.favourites.count()

    @property
    def edited(self):
        if self.pub_date:
            draft = (self.edit_date.replace(microsecond=0) - self.pub_date.replace(microsecond=0)) > datetime.timedelta(seconds=1)
        else:
            draft = True
        """ returns True if pub_date and edited are essentially the same """
        return draft
   