from .models import Car
from django.views.generic import ListView

class CarsList(ListView):
    model = Car
    template_name = 'cars-list.html'
    context_object_name = 'cars'