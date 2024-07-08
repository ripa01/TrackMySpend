from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Tracker
from django.views.generic import TemplateView
from django.db.models import Sum
from datetime import datetime
import json


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_expenses'] = Tracker.objects.order_by('-date')[:5]
        return context
    




class ExpenseUpdateView(UpdateView):
    model = Tracker
    fields = ['category', 'amount', 'title', 'date', 'payment_method']
    template_name = 'form.html'
    context_object_name = 'expense'
    success_url = reverse_lazy('home')  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_expenses'] = Tracker.objects.order_by('-date')[:5]
        return context

class ExpenseDeleteView(DeleteView):
    model = Tracker
    success_url = reverse_lazy('home') 



class ExpenseChartView(TemplateView):
    template_name = 'dashboard.html'

    def get_category_trends_data(self):
        data = {
            'labels': [],
            'datasets': []
        }

        categories = Tracker.objects.values('category').distinct()

        for category in categories:
            category_name = category['category']
            expenses = Tracker.objects.filter(category=category_name) \
                                      .order_by('date') \
                                      .values_list('date', 'amount')

            dataset = {
                'label': category_name,
                'data': [],
                'fill': False,
                'borderColor': 'rgb(75, 192, 192)',
                'lineTension': 0.1
            }

            for expense in expenses:
                dataset['data'].append({
                    'x': expense[0].strftime('%Y-%m-%d'),
                    'y': expense[1]
                })

            data['datasets'].append(dataset)

        return data

    def get_yearly_expense_data(self):
        data = {
            'labels': [],
            'data': []
        }

        current_year = datetime.today().year

        for month in range(1, 12):
            expenses = Tracker.objects.filter(date__year=current_year, date__month=month) \
                                      .aggregate(total_amount=Sum('amount'))

            data['labels'].append(datetime(current_year, month, 1).strftime('%b'))
            data['data'].append(expenses['total_amount'] if expenses['total_amount'] else 0)

        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

      
        category_trends_data = self.get_category_trends_data()
        yearly_expense_data = self.get_yearly_expense_data()

        
        context['category_trends_data'] = json.dumps(category_trends_data)
        context['yearly_expense_data'] = json.dumps(yearly_expense_data)

        return context


  


