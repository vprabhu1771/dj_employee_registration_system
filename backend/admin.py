from django.contrib import admin

# Register your models here.
from django.utils.html import format_html
from backend.models import CustomUser

from django.contrib.auth.admin import UserAdmin
from backend.forms import CustomerUserCreationForm,CustomerUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomerUserCreationForm
    form = CustomerUserChangeForm
    model = CustomUser
    list_display = ('first_name', 'last_name', 'email', 'gender' , 'image_tag', 'phone', 'hire_date', 'is_staff','is_active',)
    list_filter = ('first_name', 'last_name', 'email','is_staff','is_active', 'phone', 'hire_date',)
    fieldsets = (
        (None,{'fields': ('first_name', 'last_name', 'email','gender', 'phone', 'hire_date', 'password')}),
        ('Permissions',{'fields':('is_staff','is_active', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('first_name', 'last_name', 'email','gender', 'phone', 'hire_date', 'password1','password2','is_staff','is_active', 'groups', 'user_permissions')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    def image_tag(self,obj):
        return format_html('<img src = "{}"width="150" height="150"/>'.format(obj.image.url))

    image_tag.short_description = 'Image'

admin.site.register(CustomUser,CustomUserAdmin)