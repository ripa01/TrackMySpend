from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Tracker(models.Model):
    category = models.CharField(max_length=100)
    amount = models.IntegerField()
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    payment_method = models.CharField(max_length=50, choices=[
        ('Cash', 'Cash'), 
        ('Credit Card', 'Credit Card'), 
        ('Debit Card', 'Debit Card'), 
        ('Online Payment', 'Online Payment')
    ])

    def __str__(self):
        return self.category

    

