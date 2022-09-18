from django.contrib import admin
from .models import Redirect

@admin.register(Redirect)
class RedirectAdmin(admin.ModelAdmin):
    actions = ['activate_redirect', 'deactivate_redirect']
    list_display = ('key', 'url', 'active')
    readonly_fields = ('updated_at', 'created_at')
    list_filter = ('active',)
    
    def activate_redirect(self, request, queryset):
        for redirect in queryset:
            redirect.active = True
            redirect.save()
    activate_redirect.short_description = "Activar redirects seleccionado/s"
    
    
    def deactivate_redirect(self, request, queryset):
        for redirect in queryset:
            redirect.active = False
            redirect.save()
    deactivate_redirect.short_description = "Desactivar redirects seleccionado/s"