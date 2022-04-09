from email import message
from ntpath import join
from pyexpat import model
from unicodedata import name
from venv import create
from django.http import HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from sqlalchemy import true

from customer.models import customer, director
from .models import contract, typecontract, status, contractform, annex,contract_delegation

# Create your views here.
############ Contract ############

class status_view(LoginRequiredMixin,TemplateView):
    template_name = 'contract/status.html'
    model = status

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'status_list': self.model.objects.all(),
        }
        return context

class StatusCreate(LoginRequiredMixin,CreateView):
    model = status
    fields = ['name', 'active']
    success_url = reverse_lazy('status_view')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class StatusUpdate(LoginRequiredMixin,UpdateView):
    model = status
    fields = ['name', 'active']
    success_url = reverse_lazy('status_view')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False

class StatusDelete(LoginRequiredMixin,DeleteView):
    model = status
    success_url = reverse_lazy('status_view')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False

class Type_contract(LoginRequiredMixin,TemplateView):
    template_name = 'contract/type-contract.html'
    model = typecontract

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'typecontract_list': self.model.objects.all(),
        }
        return context

class Create_type_contract(LoginRequiredMixin,CreateView):
    template_name = 'contract/add-type-contract.html'
    model = typecontract
    # form_class = StatusForm
    fields = '__all__'
    success_url = reverse_lazy('type_contract')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class Update_type_contract(LoginRequiredMixin,UpdateView):
    model = typecontract
    # form_class = StatusForm
    fields = '__all__'
    success_url = reverse_lazy('type_contract')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False 

class Type_contract_Delete(LoginRequiredMixin,DeleteView):
    model = typecontract
    success_url = reverse_lazy('type_contract')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


class Contract_view(LoginRequiredMixin,TemplateView):
    template_name = 'contract/contract.html'
    model = contract

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_list'] = status.objects.all()
        context['typecontract_list'] = typecontract.objects.all()
        context['customer_list'] = customer.objects.all()
        context['director_list'] = director.objects.all()
        context['contract_list'] = contract.objects.all()
        return context

class Create_contract(LoginRequiredMixin,CreateView):
    template_name = 'contract/add-contract.html'
    model = contract
    fields = '__all__'
    success_url = reverse_lazy('contract')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_list'] = status.objects.all()
        context['typecontract_list'] = typecontract.objects.all()
        context['director_list'] = director.objects.all()
        context['customer_list'] = customer.objects.all()
        context['contract_list'] = contract.objects.all()
        return context

    def form_valid(self, form):
        form.instance.statuss = self.request.POST["status"]
        form.instance.typecontracts = self.request.POST["typecontract"]
        form.instance.customers = self.request.POST["customer"]
        form.instance.directors = self.request.POST["director"]
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False 


class ContractDetailView(DetailView):
    model = contract

class Update_contract(LoginRequiredMixin,UpdateView):
    template_name = 'contract/edit-contract.html'
    model = contract
    fields = '__all__'
    success_url = reverse_lazy('contract')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_list'] = status.objects.all()
        context['typecontract_list'] = typecontract.objects.all()
        context['customer_list'] = customer.objects.all()
        context['director_list'] = director.objects.all()
        context['contract_list'] = contract.objects.all()
        return context

    def form_valid(self, form):
        form.instance.statuss = self.request.POST["status"]
        form.instance.typecontracts = self.request.POST["typecontract"]
        form.instance.customers = self.request.POST["customer"]
        form.instance.directors = self.request.POST["director"]
        form.instance.user = self.request.user
        return super().form_valid(form)
        
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False 

class contract_Delete(LoginRequiredMixin,DeleteView):
    model = contract
    success_url = reverse_lazy('contract')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False

class contract_form_view(LoginRequiredMixin,TemplateView):
    template_name = 'contract/contract-form.html'
    model = contractform
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_list'] = status.objects.all()
        context['typecontract_list'] = typecontract.objects.all()
        context['customer_list'] = customer.objects.all()
        context['director_list'] = director.objects.all()
        context['contractform_list'] = contractform.objects.all()
        return context

class Create_contract_form(LoginRequiredMixin,CreateView):
    template_name = 'contract/add-contract-form.html'
    model = contractform
    fields = '__all__'
    success_url = reverse_lazy('contract_form')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_list'] = status.objects.all()
        context['typecontract_list'] = typecontract.objects.all()
        context['director_list'] = director.objects.all()
        context['customer_list'] = customer.objects.all()
        context['contractform_list'] = contractform.objects.all()
        return context

    def form_valid(self, form):
        form.instance.statuss = self.request.POST["status"]
        form.instance.typecontracts = self.request.POST["typecontract"]
        form.instance.customers = self.request.POST["customer"]
        form.instance.directors = self.request.POST["director"]
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False 

class ContracformtDetailView(DetailView):
    model = contractform

class Update_contract_form(LoginRequiredMixin,UpdateView):
    template_name = 'contract/edit-form.html'
    model = contractform
    fields = '__all__'
    success_url = reverse_lazy('contract_form')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_list'] = status.objects.all()
        context['typecontract_list'] = typecontract.objects.all()
        context['customer_list'] = customer.objects.all()
        context['director_list'] = director.objects.all()
        context['contractform_list'] = contractform.objects.all()
        return context

    def form_valid(self, form):
        form.instance.statuss = self.request.POST["status"]
        form.instance.typecontracts = self.request.POST["typecontract"]
        form.instance.customers = self.request.POST["customer"]
        form.instance.directors = self.request.POST["director"]
        form.instance.user = self.request.user
        return super().form_valid(form)
        
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False 

class contract_form_Delete(LoginRequiredMixin,DeleteView):
    model = contractform
    success_url = reverse_lazy('contract_form')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False

class Annex_view(LoginRequiredMixin,TemplateView):
    template_name = 'contract/annex.html'
    model = annex

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_list'] = status.objects.all()
        context['typecontract_list'] = typecontract.objects.all()
        context['customer_list'] = customer.objects.all()
        context['director_list'] = director.objects.all()
        context['annex_list'] = annex.objects.all()
        return context

class Create_Annex(LoginRequiredMixin,CreateView):
    template_name = 'contract/add-annex.html'
    model = annex
    fields = '__all__'
    success_url = reverse_lazy('annex')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_list'] = status.objects.all()
        context['contract_list'] = contract.objects.all()
        context['director_list'] = director.objects.all()
        context['customer_list'] = customer.objects.all()
        context['annex_list'] = annex.objects.all()
        return context

    def form_valid(self, form):
        form.instance.statuss = self.request.POST["status"]
        form.instance.contracts = self.request.POST["contract"]
        form.instance.customers = self.request.POST["customer"]
        form.instance.directors = self.request.POST["director"]
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False 

class annextDetailView(DetailView):
    model = contractform

class Update_annex(LoginRequiredMixin,UpdateView):
    template_name = 'contract/edit-annex.html'
    model = annex
    fields = '__all__'
    success_url = reverse_lazy('annex')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_list'] = status.objects.all()
        context['contract_list'] = contract.objects.all()
        context['customer_list'] = customer.objects.all()
        context['director_list'] = director.objects.all()
        context['annex_list'] = annex.objects.all()
        return context

    def form_valid(self, form):
        form.instance.statuss = self.request.POST["status"]
        form.instance.contracts = self.request.POST["contract"]
        form.instance.customers = self.request.POST["customer"]
        form.instance.directors = self.request.POST["director"]
        form.instance.user = self.request.user
        return super().form_valid(form)
        
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False 

class annex_Delete(LoginRequiredMixin,DeleteView):
    model = annex
    success_url = reverse_lazy('annex')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False

class decentralization():
    # create data
    def api_decentralization(request,id_contract,id_user):
        if request.method == 'POST':
            check_data = contract_delegation.objects.filter(id_user=id_user,id_contract=id_contract).values()
            if check_data:
                return JsonResponse({'message':'The user has permission'})
            else:
                contractDelegation = contract_delegation.objects.create(id_user=id_user,id_contract=id_contract,permission=True)
                contractDelegation.save()
                return JsonResponse({'status':200,'message':'successful'})
        else:
            return JsonResponse({'status':401,'message':'Not found'})
    # get all data
    def get_all_contract_by_user_id(request,id_user):
        if request.method == 'POST':
            data = contract_delegation.objects.filter(id_user=id_user).values()
            data_contract = []
            for item in data:
                if item['permission'] == True:
                    data_contract.append({'id_contract':item['id_contract'],'created':item['created']})
            return JsonResponse({'data':list(data_contract)})
        else:
            return JsonResponse({'status':401,'message':'Not found'})
    # cancel contract
    def cancel_contract(request,id_contract,id_user):
        if request.method == 'POST':
            check_data = contract_delegation.objects.filter(id_user=id_user,id_contract=id_contract).values()
            if check_data:
                contract_delegation.objects.filter(id_user=id_user,id_contract=id_contract).update(permission=False)
                return JsonResponse({'status':200,'message':'successful'})
            else:
                return JsonResponse({'status':401,'message':'Not found'})
        else:
            return JsonResponse({'status':401,'message':'Not found'})
    #active contract
    def active_contract(request,id_contract,id_user):
        if request.method == 'POST':
            check_data = contract_delegation.objects.filter(id_user=id_user,id_contract=id_contract).values()
            if check_data:
                contract_delegation.objects.filter(id_user=id_user,id_contract=id_contract).update(permission=True)
                return JsonResponse({'status':200,'message':'successful'})
            else:
                return JsonResponse({'status':401,'message':'Not found'})
        else:
            return JsonResponse({'status':401,'message':'Not found'})

    def get_only_contract_by_id(request,id_contract):
        if request.method =='GET':
            contract_data = contract.objects.filter(id=id_contract).values()
            if contract_data:
                return JsonResponse({'status':200,'data':list(contract_data)[0]})
            else:
                return JsonResponse({'status':401,'message':'Not found'})
        else:
            return JsonResponse({'status':401,'message':'Not found'})


    
