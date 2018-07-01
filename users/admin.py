from django.contrib import admin
from .models import CustomerUser

#@@staff_member_required  # TODO think about it
@admin.register(CustomerUser)
class CustomerUserAdmin(admin.ModelAdmin):
    readonly_fields = ('user_created', )
    list_display = ('first_name', 'last_name', 'iban')
    list_display_links = ('first_name', 'last_name')

    def get_actions(self, request):
        actions = super(CustomerUserAdmin, self).get_actions(request)
        if not request.user.is_superuser and 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
    
    def save_model(self, request, obj, form, change):
        obj.user_created = request.user  
        obj.save()

    def has_change_permission(self, request, obj=None):
        if obj and obj.user_created != request.user and not request.user.is_superuser:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        if obj and obj.user_created != request.user and not request.user.is_superuser:
            return False
        return True