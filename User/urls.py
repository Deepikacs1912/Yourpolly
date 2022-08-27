from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from . import views as user_views
urlpatterns = [
    
    path('profile/',views.profile,name = 'profile' ),
    path('login/', views.Login, name ='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='User/logout.html'), name= 'logout' ),
    path('register/', views.register, name ='register'),
]

