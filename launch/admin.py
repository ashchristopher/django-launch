from django.contrib import admin

from launch.models import SignupRequest

class SignupRequestAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('email', 'active', 'invitation_sent', 'signed_up', 'date_added', )
    list_filter = ('active', 'invitation_sent', 'signed_up', )
    date_hierarchy = 'date_added'
    
    
admin.site.register(SignupRequest, SignupRequestAdmin)
