from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Tracker

class ExpenseListView(ListView):
    model = Tracker
    template_name = 'home.html' 
    context_object_name = 'expenses'
    ordering = ['date']
    paginate_by = 10

class ExpenseCreateView(CreateView):
    model = Tracker
    fields = ['category', 'amount', 'title', 'date', 'payment_method']
    template_name = 'form.html'
    success_url = reverse_lazy('home') 

class ExpenseUpdateView(UpdateView):
    model = Tracker
    fields = ['category', 'amount', 'title', 'date', 'payment_method']
    template_name = 'form.html'
    success_url = reverse_lazy('home')  

class ExpenseDeleteView(DeleteView):
    model = Tracker
    success_url = reverse_lazy('home') 
