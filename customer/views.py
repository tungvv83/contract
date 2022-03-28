from unicodedata import name
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import director, customer
from customer import models

# Create your views here.

class customer_view(LoginRequiredMixin,TemplateView):
    template_name = 'customer/customer.html'
    model = customer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['customer_list'] = customer.objects.all()
        cus = customer.objects.all()
        context= {'customer_list': cus}
        return context

class Create_customer(LoginRequiredMixin,CreateView):
    model = customer
    fields = '__all__'
    success_message = 'Success: Item was created.'
    success_url = reverse_lazy('customer')


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class Update_customer(LoginRequiredMixin,UpdateView):
    model = customer
    fields = '__all__'
    success_url = reverse_lazy('customer')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False

        
class Delete_customer(LoginRequiredMixin,DeleteView):
    model = customer
    success_url = reverse_lazy('customer')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False

class director_view(LoginRequiredMixin,TemplateView):
    template_name = 'customer/director.html'
    model = director

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['director_list'] = director.objects.all()
        context['customer_list'] = customer.objects.all()
        return context

class Create_director(LoginRequiredMixin,CreateView):
    template_name = 'customer/director.html'
    model = director
    fields = '__all__'
    success_message = 'Success: Item was created.'
    success_url = reverse_lazy('director')


    def form_valid(self, form):
        form.instance.customers_id = self.request.POST["customer"]
        form.instance.user = self.request.user
        return super().form_valid(form)

class Update_director(LoginRequiredMixin,UpdateView):
    model = director
    # form_class = StatusForm
    fields = '__all__'
    success_url = reverse_lazy('director')


    def form_valid(self, form):
        form.instance.customers = self.request.POST["customer"]
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False

class Delete_director(LoginRequiredMixin,DeleteView):
    model = director
    success_url = reverse_lazy('director')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


