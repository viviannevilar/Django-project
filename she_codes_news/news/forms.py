from django import forms
from django.forms import ModelForm#, SplitDateTimeField, SplitDateTimeWidget
from .models import NewsStory, Category

class StoryForm(ModelForm):

    class Meta:
        model = NewsStory
        #fields = "__all__"    
        fields = ['title', 'pub_date', 'content', 'image','category']     
        #exclude = ['author'] #yet another way to set the fields, by excluding some         
        widgets = {
            'pub_date': forms.DateInput(
                format = ('%d/%m/%Y'),
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
            'title': forms.TextInput(
                attrs = {
                    'class': 'form-title'
                }
            )
        }


class CategoryForm(ModelForm):

    class Meta:
        model = Category
        fields = ['name']

