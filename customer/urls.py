from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from .views import Create_director, director_view, Update_director, Delete_director, customer_view, Create_customer, Update_customer, Delete_customer
from django.contrib.auth.decorators import login_required

from customer import views
urlpatterns = [
    # customer
    path('', customer_view.as_view(),name='customer'),
    path('create', Create_customer.as_view(), name='create_customer'),
    path('<int:pk>/update', Update_customer.as_view(), name='update_customer'),
    path('<int:pk>/delete', Delete_customer.as_view(), name='delete_customer'),
    path('director', director_view.as_view(),name='director'),
    path('director/create', Create_director.as_view(), name='create_director'),
    path('director/<int:pk>/update', Update_director.as_view(), name='update_director'),
    path('director/<int:pk>/delete', Delete_director.as_view(), name='delete_director'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)