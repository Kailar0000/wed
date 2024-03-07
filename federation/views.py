from django.shortcuts import render
from .models import Federation, Club, Event

def federation_page(request):
    all_federation = Federation.object.all()
    return render(request, 'federation/federation_page.html', {'all_federation': all_federation})