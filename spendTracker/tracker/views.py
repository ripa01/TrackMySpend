from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *

class ExpenseListView(ListView):
    model = Tracker
    template_name = 'home.html' 
    context_object_name = 'expenses'
    ordering = ['date']

