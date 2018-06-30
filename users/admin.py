from django.contrib import admin
from .models import CustomerUser


class CustomerUserAdmin(admin.ModelAdmin):
    #exclude =('user_created', ) # TODO think exclude or readonly
    readonly_fields = ('user_created', )
    
    def save_model(self, request, obj, form, change):
        obj.user_created = request.user  
        obj.save()
        
admin.site.register(CustomerUser, CustomerUserAdmin)