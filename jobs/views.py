from django.shortcuts import render
from django.views.generic import TemplateView,ListView

# Create your views here.

class HomeView(ListView):
    template_name = 'jobs/index.html'
    context_object_name = 'jobs'