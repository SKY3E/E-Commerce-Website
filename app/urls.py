from django.urls import path
from . import views
 
urlpatterns = [
  path('', views.home, name='home'),
  path('item_store', views.item_store, name='item_store'),
]