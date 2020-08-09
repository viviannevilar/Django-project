from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('<int:pk>/update/', views.UpdateStoryView.as_view(), name='update-story'),    
    path('<int:pk>/favourite_post/', views.FavouriteView, name='favourite-story'),  
    path('add-story/', views.AddStoryView.as_view(), name='newsStory'),
    path('authors/<str:username>/', views.UserStoriesView.as_view(), name='userstories'),
    path('categories/<str:slug>/', views.CategoryStoriesView.as_view(), name='cat-stories'),
    # path('stories/mine/', views.MyStoriesView.as_view(), name='mystories'),    
]

