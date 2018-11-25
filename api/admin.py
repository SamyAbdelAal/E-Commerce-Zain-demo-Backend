from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Address)
# admin.site.register(OrderStatus)
# admin.site.register(OrderType)
# admin.site.register(OrderNumber)