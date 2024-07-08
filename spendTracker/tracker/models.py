from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Tracker(models.Model):
    category = models.CharField(max_length=100)
    amount = models.IntegerField()
    title = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    payment_method = models.CharField(max_length=50, choices=[
        ('Cash', 'Cash'), 
        ('Credit Card', 'Credit Card'), 
        ('Debit Card', 'Debit Card'), 
        ('Online Payment', 'Online Payment'),
         ('Bank Transfer', 'Bank Transfer')
    ])

    def __str__(self):
        return self.category

    

