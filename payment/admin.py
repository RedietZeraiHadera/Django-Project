from django.contrib import admin
from .models import Payment

# Register your models here.

class PaymentAdmin(admin.ModelAdmin):
    list_display = ("name","amount","order_number","status","payment","date_of_payment")

admin.site.register(Payment,PaymentAdmin)


