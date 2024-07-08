from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Tracker(models.Model):
    category = models.CharField(max_length=100)
    amount = models.IntegerField()
    title = models.TextField()
    date = models.DateField()
    payment_method = models.CharField(max_length=50, choices=[
        ('Cash', 'Cash'), 
        ('Card', 'Card'), 
        ('Online Payment', 'Online Payment'),
         ('Bank Transfer', 'Bank Transfer')
    ])

    def __str__(self):
        return self.category
    

    def get_absolute_url(self):
        return reverse('update', kwargs={'pk': self.pk})

    


    

