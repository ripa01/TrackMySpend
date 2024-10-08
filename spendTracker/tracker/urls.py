from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', ExpenseListView.as_view(), name='home'),
    path('create', ExpenseCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ExpenseUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ExpenseDeleteView.as_view(), name='delete'),
    path('dashboard', ExpenseChartView.as_view(), name='dashboard'),
    path('calculator', Calculator.as_view(), name='calculator'),
    
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

