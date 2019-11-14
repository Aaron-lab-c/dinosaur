from django.urls import path
from main import views


app_name = 'origin'
urlpatterns = [
    path('', views.main, name='main'),
    path('origin/', views.origin, name='origin'),
]