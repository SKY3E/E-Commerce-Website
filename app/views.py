import re
from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'home.html')

def item_store(request):
  return render(request, 'item-store.html')