from django.urls import path
from .views import Contract_view, contract_form_view, status_view, StatusCreate, StatusUpdate, StatusDelete, Type_contract, Create_type_contract, Update_type_contract, Type_contract_Delete, Create_contract, Update_contract, contract_Delete, ContractDetailView, Create_contract_form, ContracformtDetailView, Update_contract_form, contract_form_Delete, Annex_view, Create_Annex, annextDetailView, Update_annex, annex_Delete
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    ############### contract ###############
    path('contract', Contract_view.as_view(),name='contract'),
    path('create', Create_contract.as_view(),name='create_contract'),
    path('<int:pk>', ContractDetailView.as_view(), name='contract-detail'),
    path('<int:pk>/update', Update_contract.as_view(), name='update_contract'),
    path('<int:pk>/delete', contract_Delete.as_view(), name='delete_contract'),
    path('form', contract_form_view.as_view(),name='contract_form'),
    path('form/create', Create_contract_form.as_view(),name='create_contract_form'),
    path('contract_form_detail/<int:pk>', ContracformtDetailView.as_view(), name='contract_form_detail'),
    path('contract_form/<int:pk>', Update_contract_form.as_view(), name='update_contract_form'),
    path('form/<int:pk>/delete', contract_form_Delete.as_view(), name='delete_contract_form'),
    path('annex', Annex_view.as_view(),name='annex'),
    path('annex/create', Create_Annex.as_view(),name='create_annex'),
    path('annex_detail/<int:pk>', annextDetailView.as_view(), name='annex_detail'),
    path('annex/<int:pk>', Update_annex.as_view(), name='update_annex'),
    path('annex/<int:pk>/delete', annex_Delete.as_view(), name='delete_annex'),
    path('status_view', status_view.as_view(), name='status_view'),
    path('status/create', StatusCreate.as_view(), name='create_status'),
    path('status/<int:pk>/update', StatusUpdate.as_view(), name='update_status'),
    path('status/<int:pk>/delete', StatusDelete.as_view(), name='delete_status'),
    path('type_contract', Type_contract.as_view(),name='type_contract'),
    path('type_contract/create>', Create_type_contract.as_view(), name='Create-type-contract'),
    path('type_contract/<int:pk>/update', Update_type_contract.as_view(), name='update-type-contract'),
    path('type_contract/<int:pk>/delete', Type_contract_Delete.as_view(), name='delete-type-contract'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)