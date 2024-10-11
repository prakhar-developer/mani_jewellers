from django.shortcuts import render
from .models import Rate

def home(request):
    rates = Rate.objects.all()
    return render(request, 'rates/home.html', {'rates': rates})
