from django.db import models
from django.db.models.fields import BooleanField

class Todolist(models.Model):
      
    description = models.TextField()
    
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.description