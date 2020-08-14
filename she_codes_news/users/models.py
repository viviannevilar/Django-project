from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pic = models.URLField(default='https://i.imgur.com/EqUd38p.png', max_length=200)
    bio = models.TextField(blank = True, max_length=500)
    #pass #this is where I would put my own fields

    def __str__(self):
        return self.username
    

    # @property
    # def full_name(self):
    #     return self.name + " " + self.surname

    # @full_name.setter
    # def full_name(self, value):
    #     names = value.split(' ')
    #     self.first_name = names[0]
    #     self.last_name = names[1]