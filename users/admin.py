from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from users.models import User


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        def __init__(self, *args, **kwargs):
            super(UserCreationForm, self).__init__(*args, **kwargs)
            self.fields['password1'].required = False
            self.fields['password2'].required = False
            # If one field gets autocompleted but not the other, our 'neither
            # password or both password' validation will be triggered.
            self.fields['password1'].widget.attrs['autocomplete'] = 'off'
            self.fields['password2'].widget.attrs['autocomplete'] = 'off'

        password1 = forms.CharField(
            label=_('Password'), widget=forms.PasswordInput)
        password2 = forms.CharField(
            label=_('Password confirmation'), widget=forms.PasswordInput)


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", 'is_active', 'is_staff', 'is_superuser')


class MyUserAdmin( UserAdmin):
    """Forms to add and change user instances."""
    form = UserChangeForm
    add_form = UserCreationForm

     
    """
    The fields to be used in displaying the User model.
    These override the definitions on the base UserAdmin
    that reference specific fields on auth.User.
    """
    list_display = ["first_name", "last_name", "email", 'is_active', 'is_staff', 'is_superuser', 'password']

    list_filter = ('is_staff',)
    fieldsets = (
        ('Personal info', {'fields': ('first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',)}),
        ('Login', {'fields': ('last_login', 'date_joined',)}),
    )
    """
    add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    overrides get_fieldsets to use this attribute when creating a user.
    """

    add_fieldsets = (
        ('Personal info', {'fields': ('first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',)}),
        ('Password', {'fields': ('password1', 'password2',)}),
    )
    search_fields = ('first_name', 'last_name')
    ordering = ('date_joined',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(User, MyUserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.