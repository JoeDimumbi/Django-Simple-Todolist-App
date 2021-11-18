from django.db import models
from datetime import *
from django.utils import timezone

# Create your models here.
class TaskList(models.Model):
      # id will be created automatically
    task = models.CharField(max_length=500)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)    
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task + " - " + str(self.done) + " - " + str(self.created_at)

class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name 