from email import message
from ntpath import join
from pyexpat import model
from tokenize import group
from unicodedata import name
from venv import create
from django.http import HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from sqlalchemy import false, true

from customer.models import customer, director
from .models import contract, typecontract, status, contractform, annex,contract_delegation,groupModel,User

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
    def api_decentralization(request,id_contract,id_user,group):
        if request.method == 'POST':
            check_data = contract_delegation.objects.filter(id_user=id_user,id_contract=id_contract).values()
            if check_data:
                return JsonResponse({'status':401,'message':'The user has permission'})
            else:
                contractDelegation = contract_delegation.objects.create(id_user=id_user,id_contract=id_contract,group=group,permission=True)
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

class group_s():
    def create(request):
        iduser = request.POST['userid']
        nameGroup = request.POST['nameGroup']
        member = []
        contract = []
        data = groupModel.objects.create(NameGroup=nameGroup,Member=member,createByUserId=int(iduser),Contract=contract)
        data.save()
        record = data.id
        return JsonResponse({'status':200,'message':'successful','id':record})
    def getGroup(request):
        idUser = request.POST['userid']
        data = groupModel.objects.filter(createByUserId=int(idUser)).values()
        return JsonResponse({'status':200,'message':list(data)})
    def getDataOneGroup(request):
        idGroup = request.POST['id']
        data = groupModel.objects.filter(id=idGroup).values()
        return JsonResponse({'status':200,'message':list(data)[0]})
    def Addmember(request):
        id = request.POST['id']
        idmember = request.POST['idMember']
        name = request.POST['name']
        data =list(groupModel.objects.filter(id=id).values())[0]
        ListMember = data['Member']
        dk = False
        for item in ListMember:
            if int(item['id']) == int(idmember):
               dk = True
               break
        if dk == True:
            return JsonResponse({'status':400,'message':'Thành viên đã được thêm'})
        else: 
            ListMember.append({'id':int(idmember),'name':name})
            groupModel.objects.filter(id=id).update(Member=ListMember)
            return JsonResponse({'status':200,'message':'Thêm thành công'})
    def Addcontract(request):
        id = request.POST['id']
        idcontract = request.POST['idContract']
        data =list(groupModel.objects.filter(id=id).values())[0]
        ListContract = data['Contract']
        dk = False
        for item in ListContract:
            if int(item['id']) == int(idcontract):
               dk = True
               break
        if dk == True:
            return JsonResponse({'status':400,'message':'Hợp đồng đã có'})
        else: 
            ListContract.append({'id':int(idcontract)})
            groupModel.objects.filter(id=id).update(Contract=ListContract)
            return JsonResponse({'status':200,'message':'Chia sẻ thành công'})
    def getAllAccount(request):
        data = list(User.objects.filter().values())
        record = []
        for item in data:
            if item['is_staff'] == False:
                record.append({'id':item['id'],'username': item['username']})

        return JsonResponse({'status':200,'data':record})
    def getAllContract(request):
        data = list(contract.objects.filter().values())
        record = []
        for item in data:
            record.append({'id':item['id'],'name':item['name']})
        return JsonResponse({"status":200,'data':record})
    def GetAllTypeContract(request):
        data = list(typecontract.objects.filter().values())
        record = []
        for item in data:
            record.append({'id':item['id'],'name':item['name']})
        return JsonResponse({'status':200,'data':record})
    def getAllContractGroupById(request):
        id = request.POST['id']
        record = []
        data = list(contract.objects.filter(typecontract_id=id).values())
        for item in data:
            name_contract = list(typecontract.objects.filter(id=item['typecontract_id']).values())[0]['name']
            name_customer = list(customer.objects.filter(id=item['customer_id']).values())[0]['name']
            btn_edit = '<a href="#" onclick="routerEdit({})" class="me-3 text-primary" data-bs-placement="top" title="Edit"><i class="mdi mdi-pencil font-size-18"></i></a>'.format(item['id'])
            btn_delete = '<a href="#deletecontract-{}" class="text-danger" data-bs-toggle="modal" data-bs-toggle="tooltip" data-bs-placement="top" title="Delete"><i class="mdi mdi-trash-can font-size-18"></i></a>'.format(item['id'])
            record.append([item['abstract'],item['signing_date'].strftime("%d/%m/%Y"),item['value_date'].strftime("%d/%m/%Y"),name_contract,name_customer,item['contract_value'],item['guaranteed_value'],btn_edit,btn_delete])
        return JsonResponse({'status':200,'data':record})


    
class Create_group(LoginRequiredMixin,CreateView):
    template_name = 'group/index.html'
    model = contract
    fields = '__all__'
    success_url = reverse_lazy('contract')
class detail_group(LoginRequiredMixin,CreateView):
    template_name = 'group/detail.html'
    model = contract
    fields = '__all__'
    success_url = reverse_lazy('contract')

   
    
   
