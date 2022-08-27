from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('create/', views.createpoll, name='createpoll'),
    path('vote/<poll_id>', views.votepoll, name='votepoll'),
    path('result/<poll_id>', views.result, name='result'),
    path('allvote', views.allvote, name='allvote'),
]
