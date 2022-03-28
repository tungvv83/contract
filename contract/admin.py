from django.contrib import admin
from .models import contract, contractform, annex, status, typecontract

# Register your models here.

admin.site.register(contract)
admin.site.register(contractform)
admin.site.register(annex)
admin.site.register(status)
admin.site.register(typecontract)
