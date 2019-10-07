from django import forms
from payment.models import Groupdescription, AirTicketsQuatation, VisaCostQuatation, HotelQuatation, RestaurantQuatation, EntrancesQuatation, SapSanQuatation, Client, Vendor, Service, CustomUser,Guide,Transport
from bootstrap_modal_forms.forms import BSModalForm

class GroupdescriptionForm(forms.ModelForm):
    class Meta:
        model= Groupdescription
        fields= ('groupdescription_vtrefNo',
        'groupdescription_client_Name',
        'groupdescription_number_of_passengers_paid',
        'groupdescription_number_of_passengers_free',
        'groupdescription_number_of_days',
        'groupdescription_volshebny_handle_person',
        'groupdescription_client_handle_person',
        'groupdescription_booking_date',
        'groupdescription_confirmation_date',
        'groupdescription_amount',
        'groupdescription_start_date',
        'groupdescription_end_date',
        'groupdescription_destination',
        'groupdescription_payment_method',
        'groupdescription_payment_status',
        'groupdescription_client_id',
        'groupdescription_remark')

class CustomUserForm(BSModalForm):
    class Meta:
        model = CustomUser
        fields = ['user_role','username','email']


class GroupdescriptionForm_UpdateForm(BSModalForm):
    class Meta:
        model = Groupdescription
        fields = ('groupdescription_destination',
        'groupdescription_start_date',
        'groupdescription_end_date',
        'groupdescription_amount',
        'groupdescription_payment_status',
        'groupdescription_payment_method',
        'groupdescription_booking_date',
        'groupdescription_confirmation_date',
        'groupdescription_client_id',
        'groupdescription_volshebny_handle_person',
        'groupdescription_client_handle_person',
        'groupdescription_remark')

class ServiceForm_UpdateForm(BSModalForm):
    class Meta:
        model = Service
        fields = ('service_vendor_id',
        'service_number_of_passengers',
        'service_quote_per_head',
        'service_roe',
        'service_gst',
        'service_total_amount',
        'service_vendor_payment_status',
        'service_payment_method',
        'service_id')

class Client_UpdateForm(BSModalForm):
    class Meta:
        model = Client
        fields= ('client_name',
        'client_address',
        'client_email',
        'client_telephone')

class Vendor_UpdateForm(BSModalForm):
    class Meta:
        model = Vendor
        fields=('vendor_name',
        'vendor_address',
        'vendor_type',
        'vendor_mobile',
        'vendor_email',
        'vendor_remark')

class AddAirticket(BSModalForm):
    class Meta:
        model = AirTicketsQuatation
        fields=('airticket_airline_name',
        'airticket_date_and_time_of_depature',
        'airticket_date_and_time_of_arrival',
        'airticket_departure_from',
        'airticket_arrival_at',
        'airticket_booked_from',
        'service_roe',
        'service_gst',
        'service_quote_per_head',
        'service_number_of_passengers',
        'service_total_amount',
        'service_payment_method',
        'service_vendor_payment_status')

class AddVisacost(BSModalForm):
    class Meta:
        model = VisaCostQuatation
        fields=('visacost_type_of_Visa',
        'visacost_time_period',
        'service_roe',
        'service_gst',
        'service_quote_per_head',
        'service_number_of_passengers',
        'service_total_amount',
        'service_payment_method',
        'service_vendor_payment_status')

class AddHotel(BSModalForm):
    class Meta:
        model = HotelQuatation
        fields=('hotelquatation_hotel_name',
        'hotelquatation_number_of_rooms',
        'hotelquatation_type_of_room',
        'hotelquatation_breakfast_provided',
        'service_roe',
        'service_gst',
        'service_quote_per_head',
        'service_number_of_passengers',
        'service_total_amount',
        'service_payment_method',
        'service_vendor_payment_status')

class AddRestaurant(BSModalForm):
    class Meta:
        model = RestaurantQuatation
        fields=('restaurantquatation_resturant_name',
        'restaurantquatation_For',
        'service_roe',
        'service_gst',
        'service_quote_per_head',
        'service_number_of_passengers',
        'service_total_amount',
        'service_payment_method',
        'service_vendor_payment_status')

class AddEntrances(BSModalForm):
    class Meta:
        model = EntrancesQuatation
        fields=('entrancesquatation_name',
        'service_roe',
        'service_gst',
        'service_quote_per_head',
        'service_number_of_passengers',
        'service_total_amount',
        'service_payment_method',
        'service_vendor_payment_status')

class AddSapsan(BSModalForm):
    class Meta:
        model = SapSanQuatation
        fields=('sapsanquatation_From_Station',
        'sapsanquatation_To_Station',
        'service_roe',
        'service_gst',
        'service_quote_per_head',
        'service_number_of_passengers',
        'service_total_amount',
        'service_payment_method',
        'service_vendor_payment_status')

class AddGuide(BSModalForm):
    class Meta:
        model = Guide
        fields=('Guide_Name',
        'Guide_Destination',
        'service_roe',
        'service_gst',
        'service_quote_per_head',
        'service_number_of_passengers',
        'service_total_amount',
        'service_payment_method',
        'service_vendor_payment_status')

class AddTransport(BSModalForm):
    class Meta:
        model = Transport
        fields=('transport_type_of_vehicle',
        'service_roe',
        'service_gst',
        'service_quote_per_head',
        'service_number_of_passengers',
        'service_total_amount',
        'service_payment_method',
        'service_vendor_payment_status')

class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%Y/%m/%d %H:%M:%S'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': ['#datetimepicker1','#datetimepicker2']   
        })
    )

