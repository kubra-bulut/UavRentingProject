from django.urls import reverse,reverse_lazy

from django.views.generic import TemplateView

# Create your views here.

class Home(TemplateView):#Displays home or front page.
    template_name = 'index.html'

