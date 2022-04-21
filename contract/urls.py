import re
from tokenize import group
from django.urls import path
from requests import request
from .views import Contract_view, Create_group, contract_form_view, detail_group, group_s, status_view, StatusCreate, StatusUpdate, StatusDelete, Type_contract, Create_type_contract, Update_type_contract, Type_contract_Delete, Create_contract, Update_contract, contract_Delete, ContractDetailView, Create_contract_form, ContracformtDetailView, Update_contract_form, contract_form_Delete, Annex_view, Create_Annex, annextDetailView,Update_annex, annex_Delete,decentralization
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
    #new api
    path('decentralization/<int:id_contract>/<int:id_user>/<int:group>',decentralization.api_decentralization,name="decentralization"),
    path('get_all_contract/<int:id_user>',decentralization.get_all_contract_by_user_id,name="get_all_contract_by_user_id"),
    path('cancel/<int:id_contract>/<int:id_user>',decentralization.cancel_contract,name="cancel_contract"),
    path('active/<int:id_contract>/<int:id_user>',decentralization.active_contract,name="active_contract"),
    path('getOnly/<int:id_contract>',decentralization.get_only_contract_by_id,name="get_only_contract_by_id"),


    path('createGroup',group_s.create,name="createGroup"),
    path('getGroup',group_s.getGroup,name="getGroup"),


    #create group

    path('create/group', Create_group.as_view(),name='group_create'),
    path('detail/group', detail_group.as_view(),name='detail_group'),
    






]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)