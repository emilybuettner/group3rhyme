from django.contrib import admin

from .models import Customer, Service, Product, Account


class CustomerList(admin.ModelAdmin):
    list_display = ( 'cust_name', 'organization', 'phone_number' )
    list_filter = ( 'cust_name', 'organization')
    search_fields = ('cust_name', )
    ordering = ['cust_name']


class ServiceList(admin.ModelAdmin):
    list_display = ( 'cust_name', 'service_category', 'setup_time')
    list_filter = ( 'cust_name', 'setup_time')
    search_fields = ('cust_name', )
    ordering = ['cust_name']

class ProductList(admin.ModelAdmin):
    list_display = ( 'cust_name', 'product', 'pickup_time')
    list_filter = ( 'cust_name', 'pickup_time')
    search_fields = ('cust_name', )
    ordering = ['cust_name']


class AccountList(admin.ModelAdmin):
    list_display = ( 'first_name', 'last_name', 'phone' )
    list_filter = ( 'first_name', 'last_name')
    search_fields = ('first_name', )
    ordering = ['first_name']




admin.site.register(Customer, CustomerList)
admin.site.register(Service, ServiceList)
admin.site.register(Product, ProductList)
admin.site.register(Account)

