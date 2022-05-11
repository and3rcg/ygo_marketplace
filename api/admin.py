from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from rest_framework_simplejwt.token_blacklist import models
from rest_framework_simplejwt.token_blacklist.admin import OutstandingTokenAdmin

from .models import User, CardOnSale, UserAddress, Orders, OrderItem


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
    list_display = ('card', 'id', 'seller', 'price', 'amount', 'is_visible')


@admin.register(UserAddress)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'street', 'state_province', 'city', 'zip_code')


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'id', 'customer', 'seller', 'created_at', 'complete')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'amount', 'total_price', 'date_added')


admin.site.unregister(models.OutstandingToken)
admin.site.register(models.OutstandingToken, NewOutstandingTokenAdmin)
