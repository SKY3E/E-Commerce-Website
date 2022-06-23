import re
from django.shortcuts import render
from .models import item
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
  return render(request, 'home.html')

def item_store(request):
  items = item.objects.all()
  return render(request, 'item-store.html', {'items': items})