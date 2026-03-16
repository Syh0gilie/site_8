from django.urls import path
from . import views

app_name = 'greetings'

urlpatterns = [
    path('', views.index, name='index'),
    path('greeting/<str:surname_id>/', views.get_greeting, name='get_greeting'),
]
