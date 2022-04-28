from dataclasses import field
from email.policy import default
from enum import auto
from re import U
from tkinter.messagebox import NO
from turtle import update
from unicodedata import name
from venv import create
from django.db import models
from django.urls import reverse
from requests import delete
from sqlalchemy import false, null, true
from customer.models import customer, director
from django.conf.urls.static import static
from django.contrib.auth.models import User

# Create your models here.

class typecontract(models.Model):
    class Meta:
        ordering = ['created_date']
    name = models.CharField(null=false, unique=true, max_length=200)
    created_date = models.DateTimeField(auto_now_add=true)
    updated_date = models.DateTimeField(auto_now=true)
    active = models.BooleanField(default=true)

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse('typecontract-detail', kwargs={'pk': self.pk})

class pricelist(models.Model):
    class Meta:
        ordering = ['created_date']
    name = models.CharField(null=false, unique=true, max_length=200)
    created_date = models.DateTimeField(auto_now_add=true)
    updated_date = models.DateTimeField(auto_now=true)
    active = models.BooleanField(default=true)

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse('pricelist-detail', kwargs={'pk': self.pk})

class status(models.Model):
    class Meta:
        ordering = ['created_date']
    name = models.CharField(null=false, unique=true, max_length=200)
    created_date = models.DateTimeField(auto_now_add=true)
    updated_date = models.DateTimeField(auto_now=true)
    active = models.BooleanField(default=true)

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse('status-detail', kwargs={'pk': self.pk})


class contract(models.Model):
    class Meta:
        ordering = ['created_date']
    name = models.CharField(null=false, max_length=100, unique=true)
    abstract = models.CharField(null=false, max_length=150, default=None)
    signing_date = models.DateField(null=true,default= None,blank=true)
    value_date = models.DateField(blank=true, default= None)
    expire_date = models.DateField(blank=true, default= None)
    active = models.BooleanField(default=true)
    typecontract = models.ForeignKey(typecontract, on_delete=models.SET_NULL, null=true, blank=true)
    status = models.ForeignKey(status, on_delete=models.SET_NULL, null=true, blank= true)
    contract_value = models.CharField(null=true, default=None, blank=true, max_length=100)
    guaranteed_value = models.CharField(null=true, blank=true, default=None, max_length=100)
    customer = models.ForeignKey(customer, on_delete=models.SET_NULL, null= true, blank=true)
    director = models.ForeignKey(director, on_delete=models.SET_NULL, null= true, blank=true)
    upload_file = models.FileField(upload_to='contracts/%Y/%m', blank=true, default=None)
    upload_contract = models.FileField(upload_to='contracts/%Y/%m', blank=true, default=None)
    note = models.TextField(null=true, blank=true, default=None)
    pricelist = models.ForeignKey(pricelist, on_delete=models.SET_NULL, null=true, blank= true, default=None)
    created_date = models.DateTimeField(auto_now_add=true)
    updated_date = models.DateTimeField(auto_now=true)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=true, blank=true)
    
    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse('contract-detail', kwargs={'pk': self.pk})

class contractform(models.Model):
    class Meta:
        ordering = ['created_date']
    name = models.CharField(max_length=100, null=false, blank=true, unique=true)
    abstract = models.CharField(max_length=150, blank=true, default=None)
    signing_date = models.DateField(blank=true, default= None)
    value_date = models.DateField(blank=true,default= None)
    expire_date = models.DateField(blank=true, default= None)
    active = models.BooleanField(default=true)
    typecontract = models.ForeignKey(typecontract, on_delete=models.SET_NULL,null=true, blank=true)
    status = models.ForeignKey(status, on_delete=models.SET_NULL, null=true, blank= true)
    contract_value = models.CharField(blank=true,default=None, max_length=100)
    guaranteed_value = models.CharField(blank=true, default=None, max_length=100)
    customer = models.ForeignKey(customer, on_delete=models.SET_NULL, null=true, blank= true)
    director = models.ForeignKey(director, on_delete=models.SET_NULL, null= true, blank=true)
    upload_contract = models.FileField(upload_to='contract_form/%Y/%m', blank= true, default=None)
    note = models.TextField(blank=true, default=None)
    pricelist = models.ForeignKey(pricelist, on_delete=models.SET_NULL, null=true, blank= true, default=None)
    created_date = models.DateTimeField(auto_now_add=true)
    updated_date = models.DateTimeField(auto_now=true)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=true, blank=true)

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse('contractform-detail', kwargs={'pk': self.pk})

class annex(models.Model):
    class Meta:
        ordering = ['created_date']
    name = models.CharField(max_length=100, null=false, blank=true)
    abstract = models.CharField(max_length=150, blank=true, default=None)
    signing_date = models.DateField(blank=true, default= None)
    value_date = models.DateField(blank=true,default= None)
    expire_date = models.DateField(blank=true, default= None)
    active = models.BooleanField(default=true)
    contract = models.ForeignKey(contract, on_delete=models.CASCADE,null=true, blank=true)
    status = models.ForeignKey(status, on_delete=models.SET_NULL, null=true, blank= true)
    contract_value = models.CharField(blank=true,default=None, max_length=100)
    customer = models.ForeignKey(customer, on_delete=models.SET_NULL, null=true, blank= true)
    director = models.ForeignKey(director, on_delete=models.SET_NULL, null= true, blank=true)
    upload_contract = models.FileField(upload_to='contract_annex/%Y/%m', blank= true, default=None)
    note = models.TextField(blank=true, default=None)
    pricelist = models.ForeignKey(pricelist, on_delete=models.SET_NULL, null=true, blank= true, default=None)
    created_date = models.DateTimeField(auto_now_add=true)
    updated_date = models.DateTimeField(auto_now=true)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=true, blank=true)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('annex-detail', kwargs={'pk': self.pk})
# phân quyền hợp đồng
# id_user,  id_contract, permission, group, created
class contract_delegation(models.Model):
    class Meta:
        ordering = ['created']
    id_user = models.IntegerField()
    id_contract = models.IntegerField()
    permission = models.BooleanField(default=true)
    group = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=true)
    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('contract-delegation', kwargs={'pk': self.pk})
#nhóm làm việc giữa các thành viên
class groupModel(models.Model):
    NameGroup = models.CharField(max_length=255)
    Member = models.JSONField()
    Contract = models.JSONField(default=[])
    createByUserId = models.IntegerField(default=0)
    Created = models.DateTimeField(auto_now_add=true)










