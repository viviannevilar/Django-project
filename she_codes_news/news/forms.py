from django import forms
from django.forms import ModelForm#, SplitDateTimeField, SplitDateTimeWidget
from .models import NewsStory

class StoryForm(ModelForm):
    # pub_date = SplitDateTimeField(
    # # use split date time field to allow the user to input both date and time
    #     widget=SplitDateTimeWidget(
    #         # we use the split date time widget to specify how the html gets built
    #         date_attrs={'type': 'date'},
    #         # type date tells django to use the HTML5 date input
    #         time_attrs={'type': 'time'},
    #         # type time tells django to use the HTML5 time input
    #     )
    # )

    class Meta:
        model = NewsStory
        #fields = "__all__" 
        #fields = ['title', 'author', 'pub_date', 'content', 'image']        
        fields = ['title', 'pub_date', 'content', 'image','category']     
        #exclude = ['title'] #yet another way to set the fields, by excluding some         
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
