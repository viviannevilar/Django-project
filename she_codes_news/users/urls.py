from django.urls import path
from .views import CreateAccountView, UserView#, UpdateAccountView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createaccount'),
    path('profile/<str:slug>/', UserView.as_view(), name='profile'),    
    #path('<int:pk>/update/', UpdateAccountView.as_view(), name='updateaccount'),
]