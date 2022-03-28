from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from allauth.account.views import PasswordSetView,PasswordChangeView
from contract.models import contract, typecontract, status, contractform, annex
from customer.models import customer, director
from django.urls import reverse_lazy

class Index(LoginRequiredMixin,TemplateView):
    template_name = "index.html"
    model = contract

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_list'] = status.objects.all()
        context['typecontract_list'] = typecontract.objects.all()
        context['customer_list'] = customer.objects.all()
        context['director_list'] = director.objects.all()
        context['contract_list'] = contract.objects.all()
        return context
class reports(LoginRequiredMixin,TemplateView):
    template_name = "reports.html"
class MyPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy('index')
class MyPasswordSetView(LoginRequiredMixin, PasswordSetView):
    success_url = reverse_lazy('index')