from django.urls import path
from . import views
 
urlpatterns = [
  path('', views.home, name='home'),
  path('item_store', views.item_store, name='item_store'),
  path('item_store_bakery', views.item_store_bakery, name='item_store_bakery'),
  path('item_store_meatseafood', views.item_store_meatseafood, name='item_store_meatseafood'),
  path('item_store_fruits', views.item_store_fruits, name='item_store_fruits'),
  path('item_store_vegetables', views.item_store_vegetables, name='item_store_vegetables'),
  path('item_store_dairy', views.item_store_dairy, name='item_store_dairy'),
]