
#https://github.com/django/django/blob/master/django/contrib/auth/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# The below updates the admin interface with the new custom forms
class CustomUserAdmin(UserAdmin):
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),#,
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    #??UserAdminCreationForm
    #??change_password_form = AdminPasswordChangeForm
    list_display = ('email', 'is_superuser', 'is_active', 'last_login', 'date_joined')
    list_filter = ('email', 'is_superuser', 'is_active', 'last_login', 'date_joined')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

admin.site.register(CustomUser, CustomUserAdmin)

#TODO: To be deleted when confirmed that Model below is not needed
# add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    # model = CustomUser
    # list_display = ('email', 'is_superuser', 'is_active', 'last_login', 'date_joined')
    # list_filter = ('email', 'is_superuser', 'is_active', 'last_login', 'date_joined')
    # #Used for viewing users in the admin interface
    # fieldsets = (
    #     (None, {'fields': ('email', 'password')}),
    #     ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active')}),
    # )
    # #Used for user creation in the admin interface
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'password1', 'password2', 'is_staff', 'is_superuser')}
    #     ),
    # )
    # search_fields = ('email',)
    # ordering = ('email',)