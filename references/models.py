from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your models here.

class References(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField(max_length=80, blank=True)
    description = models.TextField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'references_post')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    link = models.URLField()

    objects = models.Manager()

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self) :
        return reverse_lazy('references:references_list')
    
