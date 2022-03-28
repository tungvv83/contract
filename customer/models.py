from dataclasses import field
from enum import auto
from turtle import update
from unicodedata import name
from venv import create
from django.db import models
from django.forms import ValidationError
from django.urls import reverse
from sqlalchemy import false, null, true
from django.contrib.auth.models import User

# Create your models here.


class customer(models.Model):
    class Meta:
        ordering = ['created_date']
    name = models.CharField(null=false, max_length=255, unique=true)
    tax_code = models.CharField(null=false, max_length=25)
    phone = models.CharField(null=true, max_length=20)
    address = models.CharField(null=true, max_length=255)
    active = models.BooleanField(default=true)
    created_date = models.DateTimeField(auto_now_add=true)
    updated_date = models.DateTimeField(auto_now=true)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=true, blank=true)

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse('customer-detail', kwargs={'pk': self.pk})

class director(models.Model):
    class Meta:
        ordering = ['created_date']
    name = models.CharField(null=false, max_length=150)
    position = models.CharField(null=true, max_length=150)
    authorization = models.CharField(blank=true, max_length=255)
    customer = models.ForeignKey(customer, on_delete=models.SET_NULL, null=true)
    active = models.BooleanField(default=true)
    created_date = models.DateTimeField(auto_now_add=true)
    updated_date = models.DateTimeField(auto_now=true)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=true, blank=true)

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse('director-detail', kwargs={'pk': self.pk})
    

    

