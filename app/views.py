import re
from django.shortcuts import render
from .models import item

# Create your views here.
def home(request):
  return render(request, 'home.html')

def item_store(request):
  items = item.objects.all()
  return render(request, 'item-store.html', {'items': items})

def item_store_bakery(request):
  items = item.objects.all()
  return render(request, 'item-store-bakery.html', {'items': items})

def item_store_meatseafood(request):
  items = item.objects.all()
  return render(request, 'item-store-meat&seafood.html', {'items': items})

def item_store_fruits(request):
  items = item.objects.all()
  return render(request, 'item-store-fruits.html', {'items': items})

def item_store_vegetables(request):
  items = item.objects.all()
  return render(request, 'item-store-vegetables.html', {'items': items})

def item_store_dairy(request):
  items = item.objects.all()
  return render(request, 'item-store-dairy.html', {'items': items})