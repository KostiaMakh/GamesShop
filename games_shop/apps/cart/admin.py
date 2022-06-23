from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['game']


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'city',
        'status',
        'paid',
        'created_at',
        'updated_at'
    )
    list_filter = (
        'paid',
        'created_at',
        'updated_at',
        'status'
    )
    readonly_fields = (
        'created_at',
        'updated_at',
        'user'
    )
    inlines = (OrderItemInline,)
    save_on_top = True


admin.site.register(Order, OrderAdmin)
