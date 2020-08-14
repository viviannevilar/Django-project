from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('<int:pk>/update/', views.UpdateStoryView.as_view(), name='update-story'),
    path('<int:pk>/delete/', views.DeleteStoryView.as_view(), name='delete-story'),
    path('<int:pk>/favourite_post/', views.FavouriteView, name='favourite-story'),  
    path('add-story/', views.AddStoryView.as_view(), name='newsStory'),
    path('authors/<str:username>/', views.UserStoriesView.as_view(), name='userstories'),
    path('categories/<str:slug>/', views.CategoryStoriesView.as_view(), name='cat-stories'),
    path('cat/all/<str:slug>/', views.CatStoriesView.as_view(), name='cat-all-stories'),
    path('uncategorised/', views.UncategorisedStoriesView.as_view(), name='uncat-stories'),
    path('all/uncategorised/', views.UncatStoriesView.as_view(), name='uncat-all-stories'),
    path('create_category/', views.CreateCategoryView.as_view(), name='create-cat'),
    path('all_categories/', views.AllCategoriesView.as_view(), name='all-categories'),
    path('search_results/', views.SearchResultsView.as_view(), name='search'),
    path('latest_stories/', views.LatestStoriesView.as_view(), name='latest-stories'),
    path('top_stories/', views.TopStoriesView.as_view(), name='top-stories'),
    path('categories/', views.CategoriesView.as_view(), name='all-cat'),
    # path('stories/mine/', views.MyStoriesView.as_view(), name='mystories'),    
]

