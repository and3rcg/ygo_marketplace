from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from rest_framework_simplejwt.token_blacklist import models
from rest_framework_simplejwt.token_blacklist.admin import OutstandingTokenAdmin

from .models import User, CardOnSale, UserAddress, Orders


class NewOutstandingTokenAdmin(OutstandingTokenAdmin):

    def has_delete_permission(self, *args, **kwargs):
        return True


@admin.register(User)
class MyUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('wallet',)}),
    )
    list_display = UserAdmin.list_display + ('wallet',)


@admin.register(CardOnSale)
class CardOnSaleAdmin(admin.ModelAdmin):
    fields = ('card', 'seller', 'price', 'amount', 'is_visible')
    list_display = ('card', 'seller', 'price', 'amount', 'is_visible')


@admin.register(UserAddress)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'street', 'state_province', 'city', 'zip_code')


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('product', 'price', 'buyer_address', 'delivery_status', 'updated_at',
                    'created_at')


admin.site.unregister(models.OutstandingToken)
admin.site.register(models.OutstandingToken, NewOutstandingTokenAdmin)
