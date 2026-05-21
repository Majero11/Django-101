from django.urls import path 
from .views import HomePageVIew
app_name = 'feed'

urlpatterns = [
    path('', HomePageView.as_view(), name='index')
]