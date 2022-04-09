
from django.conf import settings
from django.conf.urls.static import static
from layouts import urls
import contract, customer, e_mail
from django.contrib import admin
from django.urls import path,include
# from django.conf.urls import include, url
from morvin import views
from django.views.generic import TemplateView
from .views import MyPasswordSetView ,MyPasswordChangeView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    # Index
    path('', views.Index.as_view(),name='index'),
    # reports
    path('reports/', views.reports.as_view(),name='reports'),
    # customers
    path('customer/', include('customer.urls')),
    # Email
    path('email/',include('e_mail.urls')),
    # contract
    path('contract/', include('contract.urls')),
    # Allauth
    path('account/', include('allauth.urls')),
    # logout
    path('logout/', TemplateView.as_view(template_name="account/logout-success.html"),name="logout"),
    #Custum change password done page redirect
    path('accounts/password/change/', login_required(MyPasswordChangeView.as_view()), name="account_change_password"),
    #Custum set password done page redirect
    path('accounts/password/set/', login_required(MyPasswordSetView.as_view()), name="account_set_password"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)