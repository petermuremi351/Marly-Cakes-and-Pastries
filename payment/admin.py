# from django.contrib import admin
# from .models import ShippingAddress, Order, OrderItem

# admin.site.register(ShippingAddress)
# admin.site.register(OrderItem)

# # create OrderItem inline
# class OrderItemInline(admin.StackedInline):
#     model = OrderItem
#     extra = 0

# # extend our Order model
# class OrderAdmin(admin.ModelAdmin):
#     model = Order
#     readonly_fields = ["date_ordered"]
#     inlines = [OrderItemInline]


# # unregister order model
# # admin.site.unregister(Order)


# # reregister Order ONCE, correctly
# admin.site.register(Order, OrderAdmin)


from django.contrib import admin
from .models import ShippingAddress, Order, OrderItem

# Register models that stand alone
admin.site.register(ShippingAddress)
admin.site.register(OrderItem)

# Create OrderItem inline
class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 0

# Customize Order admin
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ("date_ordered",)
    fields = ["user", "full_name", "email", "shipping_address", "amount_paid", "date_ordered", "shipped"]
    inlines = [OrderItemInline]

# Register Order ONCE with its inline
admin.site.register(Order, OrderAdmin)