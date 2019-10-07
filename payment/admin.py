from django.contrib import admin
from payment.models import Groupdescription,AirTicketsQuatation,VisaCostQuatation,HotelQuatation,RestaurantQuatation,EntrancesQuatation,SapSanQuatation,CustomUser,Vendor,Client,Service,Guide,Transport

# Register your models here.

class VendorAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "vendor_name",
        "vendor_type",
    ]

class AirTicketsQuatationAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "service_type",
    ]

class VisaCostQuatationAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "service_type",
    ]
class HotelQuatationAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "service_type",
    ]
class RestaurantQuatationAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "service_type",
    ]
class EntrancesQuatationAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "service_type",
    ]
class SapSanQuatationAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "service_type",
    ]

class TransportAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "service_type",
    ]
class ClientAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "client_name",
    ]

class GuideAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "service_type",
    ]

class GroupdescriptionAdmin(admin.ModelAdmin):
    search_fields = ["groupdescription_vtrefNo", "groupdescription_client_id"]
    list_filter = ["groupdescription_client_id", "groupdescription_payment_status"]
    list_display = [
        "pk",
        "groupdescription_vtrefNo",
        "groupdescription_client_id",
        "groupdescription_date_time_added",
        "groupdescription_payment_status",
        ]
    list_editable = ["groupdescription_payment_status"]
    

admin.site.register(Groupdescription,GroupdescriptionAdmin)
admin.site.register(AirTicketsQuatation,AirTicketsQuatationAdmin)
admin.site.register(VisaCostQuatation,VisaCostQuatationAdmin)
admin.site.register(HotelQuatation,HotelQuatationAdmin)
admin.site.register(RestaurantQuatation,RestaurantQuatationAdmin)
admin.site.register(EntrancesQuatation,EntrancesQuatationAdmin)
admin.site.register(SapSanQuatation,SapSanQuatationAdmin)
admin.site.register(Transport,TransportAdmin)
admin.site.register(Guide,GuideAdmin)
admin.site.register(CustomUser)
admin.site.register(Vendor,VendorAdmin)
admin.site.register(Client,ClientAdmin)
admin.site.register(Service)

