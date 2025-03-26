from django.contrib import admin
from .models import Device, Customer, DeviceInField, Order

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'model')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_city')

@admin.register(DeviceInField)
class DeviceInFieldAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'customer', 'device', 'owner')
    list_filter = ('customer', 'device')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('device', 'customer', 'order_status', 'created_at')
    list_filter = ('order_status', 'customer')
    search_fields = ('device__serial_number', 'customer__customer_name')

