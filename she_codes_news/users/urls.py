from django.urls import path
from .views import CreateAccountView, UserView, UpdateAccountView


app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createaccount'),
    path('<str:slug>/profile/', UserView.as_view(), name='profile'),    
    path('<str:slug>/update/', UpdateAccountView.as_view(), name='updateaccount'),
]


    #path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),  
