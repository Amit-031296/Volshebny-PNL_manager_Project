#External Imports
from django.views import generic
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import json
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from bootstrap_modal_forms.generic import (BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)

#Project Imports
from payment.models import Groupdescription, AirTicketsQuatation, VisaCostQuatation, HotelQuatation, RestaurantQuatation, EntrancesQuatation, SapSanQuatation,Transport, Client, Vendor, Service, CustomUser,Guide
from payment.forms import GroupdescriptionForm, GroupdescriptionForm_UpdateForm, Client_UpdateForm, Vendor_UpdateForm,AddAirticket, AddVisacost,AddHotel,AddRestaurant,AddEntrances,AddSapsan,AddGuide,AddTransport,DateForm,ServiceForm_UpdateForm,CustomUserForm    

from payment import count_values
from payment import functions



# ------ Authentication Views -----
# Login
def user_login(request):
    """Logs in a user if the credentials are valid and the user is active,
    else redirects to the same page and displays an error message."""
    if request.method == "POST":
        username =  request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('payment:group_description_form'))
        else:
            return render(request, 'payment/registration/sign_in.html',{'error_message': 'Username or Password Incorrect!'})

    else:
        return render(request, 'payment/registration/sign_in.html')

# Sign Up
def user_sign_up(request):
    """Registers a user"""
    if request.method == "POST":
        username =  request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            return render(request, 'payment/registration/sign_up.html',{'error_message':'Passwords do not match!'})
        if CustomUser.objects.filter(username = username).exists():
            return render(request, 'payment/registration/sign_up.html',{'error_message':'Username already exists!'})
        else:
            # Role 2 is for admin, 1 is for super admin.
            user = CustomUser.objects.create(username=username, password= make_password(password), user_role=2)
            login(request, user)
            return HttpResponseRedirect(reverse('payment:group_description_form'))
    else:
        return render(request, 'payment/registration/sign_up.html')

# Forget Password
def forgetpassword(request):
    """Hub Connect Survey Form Data Collected
    Parameters: HttpRequest objects
    Returns : All Data in Leads Table"""
    user_role = request.user.role
    leads = Leads.objects.all()
    page_active = 3
    data = { 'user_role': user_role,
            'leads': leads,
            'page_active': page_active }
    return render(request, 'payment/pnllist.html', data )

# Logout
def user_sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('payment:user_login'))

#Report Error Form
@login_required(login_url='/user_login')
def report_error(request):
    """Form for taking User Errors
    Parameters: HttpRequest object
    Returns : Nothing"""
    #user_role = request.user.user_role
    #data = { 'user_role': user_role}
    return render(request, 'payment/report_error.html' )

@login_required(login_url='/user_login')
def report_error_submit(request):
    
    if request.method == "POST":
        Subject = request.POST['subject']
        Message = request.POST['message']
    send_mail(Subject,Message,'amitv.mumbaii@gmail.com',['amitv.mumbaii@gmail.com'],fail_silently=False,)
    
    return HttpResponseRedirect(reverse('payment:report_error_success'))

@login_required(login_url='/user_login')
def report_error_success(request):
    return render(request, 'payment/report_error_success.html')


# </------ Authentication Views -----

#Experiment View
def experiment(request):
    clients = Client.objects.all()
    clients_dict = {}
    for client in clients:
        clients_dict[client.pk] = client.client_name
    tour_list = list(set(list(Groupdescription.objects.values_list('pk', 'groupdescription_vtrefNo',
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
    'groupdescription_client_id'))))
    tour_cost_list = [ functions.group_cost_list_generator(one_tour_detials) for one_tour_detials in tour_list ]
    pnl_dict = dict(zip(tour_list,tour_cost_list))
    data = { 'pnl_dict':pnl_dict,'clients_dict':clients_dict}
    return render(request,'payment/experiment.html',data)

# ------ Sidemenu Views -----
# Tour Details Form
@login_required(login_url='/user_login')
def group_description_form(request):
    group_description_latest = Groupdescription.objects.latest('groupdescription_date_time_added').groupdescription_vtrefNo
    user_office_location = request.user.office_location
    clients = Client.objects.all()
    js_data = json.dumps({ 'user_office_location':user_office_location })
    data_2 = { 'clients' : clients,
            'js_data':js_data,
            'group_description_latest':group_description_latest }
    return render(request,'payment/pnlstatement.html',data_2)

# Tour Details List
@login_required(login_url='/user_login')
def pnllist(request):
    clients = Client.objects.all()
    clients_dict = {}
    for client in clients:
        clients_dict[client.pk] = client.client_name
    tour_list = list(set(list(Groupdescription.objects.values_list('pk', 'groupdescription_vtrefNo',
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
    'groupdescription_client_id'))))
    tour_cost_list = [ functions.group_cost_list_generator(one_tour_detials) for one_tour_detials in tour_list ]
    pnl_dict = dict(zip(tour_list,tour_cost_list))
    data = { 'pnl_dict':pnl_dict,'clients_dict':clients_dict}
    return render(request,'payment/pnllist.html',data)

# Services - Add Services
@login_required(login_url='/user_login')
def add_services(request,pk):
    vendors = Vendor.objects.all()
    group_object = Groupdescription.objects.get(pk=pk)
    air_tickets = list(AirTicketsQuatation.objects.all().filter(service_id=pk))
    visa_costs = list(VisaCostQuatation.objects.all().filter(service_id=pk))
    hotel_quatations = list(HotelQuatation.objects.all().filter(service_id=pk))
    restaurant_quatations = list(RestaurantQuatation.objects.all().filter(service_id=pk))
    entrances_quatations = list(EntrancesQuatation.objects.all().filter(service_id=pk))
    sapsan_quatations = list(SapSanQuatation.objects.all().filter(service_id=pk))
    guide_names = list(Guide.objects.all().filter(service_id=pk))
    transport_names = list(Transport.objects.all().filter(service_id=pk))
    sum = 0
    for airticket in air_tickets:
        sum = sum + airticket.service_total_amount
    for visacost in visa_costs:
        sum = sum + visacost.service_total_amount
    for hotel in hotel_quatations:
        sum = sum + hotel.service_total_amount
    for restaurant in restaurant_quatations:
        sum = sum + restaurant.service_total_amount
    for entrance in entrances_quatations:
        sum = sum + entrance.service_total_amount
    for sapsan in sapsan_quatations:
        sum = sum + sapsan.service_total_amount
    for guide in guide_names:
        sum = sum + guide.service_total_amount
    for transport in transport_names:
        sum = sum + transport.service_total_amount
    payment_total = sum
    service_list = []
    service_list = air_tickets+visa_costs+hotel_quatations+restaurant_quatations+entrances_quatations+sapsan_quatations+guide_names+transport_names
    vendor_dict = {}
    for vendor in vendors:
        vendor_dict[vendor.pk] = vendor.vendor_name
    data = { 'grdes' : group_object,'service_list':service_list,'vendors':vendors,'payment_total':payment_total,'vendor_dict':vendor_dict}
    return render(request,'payment/add_services.html',data)

# Tour Summary Page
@login_required(login_url='/user_login')
def tour_summary(request,pk):
    # Get tour summary Object as per tour summary Id Passed
    vendors = Vendor.objects.all()
    clients = Client.objects.all()
    tour_order = Groupdescription.objects.get(pk=pk)
    air_tickets = list(AirTicketsQuatation.objects.all().filter(service_id=pk))
    visa_costs = list(VisaCostQuatation.objects.all().filter(service_id=pk))
    hotel_quatations = list(HotelQuatation.objects.all().filter(service_id=pk))
    restaurant_quatations = list(RestaurantQuatation.objects.all().filter(service_id=pk))
    entrances_quatations = list(EntrancesQuatation.objects.all().filter(service_id=pk))
    sapsan_quatations = list(SapSanQuatation.objects.all().filter(service_id=pk))
    guide_quatations = list(Guide.objects.all().filter(service_id=pk))
    transport_names = list(Transport.objects.all().filter(service_id=pk))
    sum = 0
    for airticket in air_tickets:
        sum = sum + airticket.service_total_amount
    for visacost in visa_costs:
        sum = sum + visacost.service_total_amount
    for hotel in hotel_quatations:
        sum = sum + hotel.service_total_amount
    for restaurant in restaurant_quatations:
        sum = sum + restaurant.service_total_amount
    for entrance in entrances_quatations:
        sum = sum + entrance.service_total_amount
    for sapsan in sapsan_quatations:
        sum = sum + sapsan.service_total_amount
    for guide in guide_quatations:
        sum = sum + guide.service_total_amount
    for transport in transport_names:
        sum = sum + transport.service_total_amount
    payment_total = sum
    client_dict = {}
    for client in clients:
        client_dict[client.client_name] = client.client_name
    client_name = client_dict[str(tour_order.groupdescription_client_id)]
    service_list = []
    pnlbalance = tour_order.groupdescription_amount - payment_total
    service_list = air_tickets+visa_costs+hotel_quatations+restaurant_quatations+entrances_quatations+sapsan_quatations+guide_quatations+transport_names
    vendor_dict = {}
    for vendor in vendors:
        vendor_dict[vendor.pk] = vendor.vendor_name
    data = {
        'tour_order': tour_order,
        'service_list': service_list,
        'payment_total':payment_total,
        'pnlbalance':pnlbalance,
        'client_name': client_name,
        'vendor_dict':vendor_dict
     }
    return render(request,'payment/tour_summary.html',data)

#Client List
@login_required(login_url='/user_login')
def client_list(request):
    clients = Client.objects.all()
    client_payment_status = ['Paid','Pending']
    x = list(set(list(Client.objects.values_list('pk','client_name'))))
    client_status_list = [functions.client_status_count(a,client_payment_status_one) for a in x for client_payment_status_one in client_payment_status ]
    final = [client_status_list[i * 2:(i + 1) * 2] for i in range((len(client_status_list) + 2 - 1) // 2 )]
    client_dict = dict(zip(x,final))
    clientlist = client_dict
    userrole = request.user.user_role
    return render(request,'payment/clientlist.html',{'clientlist':clientlist,'userrole':userrole })

# Vendor Tour List
@login_required(login_url='/user_login')
def vendor_list(request):
    vendorlist = Vendor.objects.all()
    vendor_payment_status = ['Pending','Done','Payment_Pending_Amonut','Payment_Done_Amount']
    x = list(set(list(Vendor.objects.values_list('pk','vendor_name'))))
    vendor_status_list = [ functions.vendor_payment_count(a,vendor_payment_status_one) for a in x for vendor_payment_status_one in vendor_payment_status ]
    final = [vendor_status_list[i * 4:(i + 1) * 4] for i in range((len(vendor_status_list) + 4 - 1) // 4 )]
    vendor_dict = dict(zip(x,final))
    vendorlist = vendor_dict
    return render(request,'payment/vendorlist.html',{'vendorlist':vendorlist})

# --All vendor accounts dropdown Views -- 
# -- vendor_accounts_airticket_quatation View---
@login_required(login_url='/user_login')
def vendor_accounts_airticket_quatation(request):
    airticket_list=functions.filtering_vendors("Air Ticket Service")
    userrole = request.user.user_role
    return render(request, 'payment/vendor_accounts_airticket_quatation.html',{'airticket_list':airticket_list,'userrole':userrole })

# -- vendor_accounts_visacost_quatation View---
@login_required(login_url='/user_login')
def vendor_accounts_visacost_quatation(request):
    visacost_list=functions.filtering_vendors("Visa Cost Service")
    userrole = request.user.user_role
    return render(request,'payment/vendor_accounts_visacost_quatation.html',{'visacost_list':visacost_list,'userrole':userrole })

# -- vendor_accounts_hotel_quatation View---
@login_required(login_url='/user_login')
def vendor_accounts_hotel_quatation(request):
    hotel_list=functions.filtering_vendors("Hotel Quatation Service")
    userrole = request.user.user_role
    return render(request,'payment/vendor_accounts_hotel_quatation.html',{'hotel_list':hotel_list,'userrole':userrole })

# -- vendor_accounts_restaurant_quatation View---
@login_required(login_url='/user_login')
def vendor_accounts_restaurant_quatation(request):
    restaurant_list=functions.filtering_vendors("Restuarant Quatation Service")
    userrole = request.user.user_role
    return render(request,'payment/vendor_accounts_restaurant_quatation.html',{'restaurant_list':restaurant_list,'userrole':userrole })

# -- vendor_accounts_entrances_quatation View---
@login_required(login_url='/user_login')
def vendor_accounts_entrances_quatation(request):
    entrances_list=functions.filtering_vendors("Entrances Quatation Service")
    userrole = request.user.user_role
    return render(request,'payment/vendor_accounts_entrances_quatation.html',{'entrances_list':entrances_list,'userrole':userrole })

# -- vendor_accounts_sapsan_quatation View---
@login_required(login_url='/user_login')
def vendor_accounts_sapsan_quatation(request):
    sapsan_list=functions.filtering_vendors("SapSan Quatation Service")
    userrole = request.user.user_role
    return render(request,'payment/vendor_accounts_sapsan_quatation.html',{'sapsan_list':sapsan_list,'userrole':userrole })

# -- vendor_accounts_guide View---
@login_required(login_url='/user_login')
def vendor_accounts_guide(request):
    guide_list=functions.filtering_vendors("Guide Service")
    userrole = request.user.user_role
    return render(request,'payment/vendor_accounts_guide.html',{'guide_list':guide_list,'userrole':userrole })

# -- vendor_accounts_transport View---
@login_required(login_url='/user_login')
def vendor_accounts_transport(request):
    transport_list=functions.filtering_vendors("Transport Service")
    userrole = request.user.user_role
    return render(request,'payment/vendor_accounts_transport.html',{'transport_list':transport_list,'userrole':userrole })

#< -----Users list Views ------>
@login_required(login_url='/user_login')
def user_list(request):
    users = CustomUser.objects.all()
    #userrole = request.user.user_role
    data = { 'users' : users }
    return render(request,'payment/userlist.html',data)
#</-----Users list Views------>

#< -----Add Users Views ------>
class Add_UsersView(BSModalCreateView):
    template_name = 'payment/add_new_user.html'
    form_class = CustomUserForm
    success_message = 'Success: User was added.'
    success_url = reverse_lazy('payment:userlist')
#</-----Add Users Views ------>    

#< -----Delete Users Views ------>
class UserDeleteView(BSModalDeleteView):
    model = CustomUser
    template_name = 'payment/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    success_url = reverse_lazy('payment:userlist')
#</-----Delete Users Views ------>

#< -----Update Users Views ------>
class UserUpdateView(BSModalUpdateView):
    model = CustomUser
    template_name = 'payment/update_entry.html'
    form_class = CustomUserForm
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('payment:userlist')
#</-----Update Users Views ------>

# </------ Sidemenu Views -----

#------ All Form Submit Processing Views -----------

#----group_description_form_submit Views ----
@login_required(login_url='/user_login')
def group_description_form_submit(request):
    if request.method == "POST":
        # Get all data relating to purchase order.
        groupdescription_vtrefNo = request.POST['groupdescription_vtrefNo']
        groupdescription_number_of_passengers_paid = request.POST['groupdescription_number_of_passengers_paid']
        groupdescription_number_of_passengers_free = request.POST['groupdescription_number_of_passengers_free']
        groupdescription_number_of_days = request.POST['groupdescription_number_of_days']
        groupdescription_amount = request.POST['groupdescription_amount']
        groupdescription_start_date = request.POST['groupdescription_start_date']
        groupdescription_end_date = request.POST['groupdescription_end_date']
        groupdescription_destination = request.POST['groupdescription_destination']
        groupdescription_volshebny_handle_person = request.POST['groupdescription_volshebny_handle_person']
        groupdescription_client_handle_person = request.POST['groupdescription_client_handle_person']
        groupdescription_booking_date = request.POST['groupdescription_booking_date']
        groupdescription_confirmation_date = request.POST['groupdescription_confirmation_date']
        groupdescription_payment_method = request.POST['groupdescription_payment_method']
        groupdescription_client_id = Client.objects.get(pk=request.POST['groupdescription_client_id'])
        groupdescription_vtrefNo_short = 121
        groupdescription_roe = request.POST['groupdescription_roe']
        Groupdescription.objects.create(groupdescription_vtrefNo = groupdescription_vtrefNo,
                                        groupdescription_client_id = groupdescription_client_id,
                                        groupdescription_number_of_passengers_paid = groupdescription_number_of_passengers_paid,
                                        groupdescription_number_of_passengers_free = groupdescription_number_of_passengers_free,
                                        groupdescription_number_of_days = groupdescription_number_of_days,
                                        groupdescription_amount = groupdescription_amount,
                                        groupdescription_start_date = groupdescription_start_date,
                                        groupdescription_end_date = groupdescription_end_date,
                                        groupdescription_destination = groupdescription_destination,
                                        groupdescription_volshebny_handle_person = groupdescription_volshebny_handle_person,
                                        groupdescription_client_handle_person = groupdescription_client_handle_person,
                                        groupdescription_booking_date = groupdescription_booking_date,
                                        groupdescription_confirmation_date = groupdescription_confirmation_date,
                                        groupdescription_payment_method = groupdescription_payment_method,
                                        groupdescription_vtrefNo_short=groupdescription_vtrefNo_short,
                                        groupdescription_roe=groupdescription_roe )
        group_latest_object = Groupdescription.objects.latest('groupdescription_date_time_added')
    return HttpResponseRedirect(reverse('payment:add_services',kwargs={'pk': group_latest_object.pk}))

#-----add_service_airticket_form_submit Views ------
@login_required(login_url='/user_login')
def add_service_airticket_form_submit(request,service_id):
    if request.method == "POST":

        airticket_airline_name = request.POST['airticket_airline_name']
        airticket_date_and_time_of_depature = request.POST['airticket_date_and_time_of_depature']
        airticket_date_and_time_of_arrival = request.POST['airticket_date_and_time_of_arrival']
        airticket_departure_from = request.POST['airticket_departure_from']
        airticket_arrival_at = request.POST['airticket_arrival_at']
        airticket_quote_per_head = request.POST['airticket_quote_per_head']
        airticket_number_of_passengers = request.POST['airticket_number_of_passengers']
        airticket_roe = request.POST['airticket_roe']
        airticket_type_of_GST = request.POST['airticket_type_of_GST']
        airticket_total_amount = request.POST['airticket_total_amount']
        vendor_id = request.POST['airticket_service_vendor_id']
        
        vendor_object = Vendor.objects.get(pk=vendor_id)
        group_object = Groupdescription.objects.get(pk=service_id)
        AirTicketsQuatation.objects.create(
                                        airticket_airline_name = airticket_airline_name,
                                        service_number_of_passengers = airticket_number_of_passengers,
                                        airticket_date_and_time_of_depature = airticket_date_and_time_of_depature,
                                        airticket_date_and_time_of_arrival = airticket_date_and_time_of_arrival,
                                        airticket_departure_from = airticket_departure_from,
                                        airticket_arrival_at = airticket_arrival_at,
                                        service_roe = airticket_roe,
                                        service_gst = airticket_type_of_GST,
                                        service_id = group_object,
                                        service_quote_per_head = airticket_quote_per_head,
                                        service_total_amount = airticket_total_amount,
                                        service_vendor_id=vendor_object)

    return HttpResponseRedirect(reverse('payment:add_services',kwargs={'pk': service_id }))

#-----add_service_visacost_form_submit Views ------
@login_required(login_url='/user_login')
def add_service_visacost_form_submit(request,service_id):
    if request.method == "POST":
        visacost_number_of_passengers = request.POST['visacost_number_of_passengers']
        visacost_type_of_Visa = request.POST['visacost_type_of_Visa']
        visacost_time_period = request.POST['visacost_time_period']
        visacost_quote_per_head = request.POST['visacost_quote_per_head']
        visacost_roe = request.POST['visacost_roe']
        visacost_type_of_GST = request.POST['visacost_type_of_GST']
        visacost_total_amount = request.POST['visacost_total_amount']
        vendor_id = request.POST['visacost_service_vendor_id']
        vendor_object = Vendor.objects.get(pk=vendor_id)
        group_object = Groupdescription.objects.get(pk=service_id)
        VisaCostQuatation.objects.create(visacost_type_of_Visa = visacost_type_of_Visa,
                                        service_number_of_passengers = visacost_number_of_passengers,
                                        visacost_time_period = visacost_time_period,
                                        service_roe = visacost_roe,
                                        service_gst = visacost_type_of_GST,
                                        service_id = group_object,
                                        service_quote_per_head = visacost_quote_per_head,
                                        service_total_amount = visacost_total_amount,
                                        service_vendor_id=vendor_object)

    return HttpResponseRedirect(reverse('payment:add_services',kwargs={'pk': service_id }))

#-----add_service_hotelquatation_form_submit Views ------
@login_required(login_url='/user_login')
def add_service_hotelquatation_form_submit(request,service_id):
     if request.method == "POST":
            hotelquatation_hotel_name = request.POST['hotelquatation_hotel_name']
            hotelquatation_number_of_rooms = request.POST['hotelquatation_number_of_rooms']
            hotelquatation_type_of_room = request.POST['hotelquatation_type_of_room']
            hotel_quote_per_room = request.POST['hotel_quote_per_room']
            hotel_roe = request.POST['hotel_roe']
            hotelquatation_breakfast_provided = request.POST['hotelquatation_breakfast_provided']
            hotel_type_of_GST = request.POST['hotel_type_of_GST']
            hotel_total_amount = request.POST['hotel_total_amount']
            vendor_id = request.POST['hotel_service_vendor_id']
            vendor_object = Vendor.objects.get(pk=vendor_id)
            group_object = Groupdescription.objects.get(pk=service_id)
            HotelQuatation.objects.create(hotelquatation_hotel_name = hotelquatation_hotel_name,
            hotelquatation_number_of_rooms = hotelquatation_number_of_rooms,
                                        hotelquatation_type_of_room = hotelquatation_type_of_room,
                                        hotelquatation_breakfast_provided = hotelquatation_breakfast_provided,
                                        service_roe = hotel_roe,
                                        service_gst = hotel_type_of_GST,
                                        service_id = group_object,
                                        service_quote_per_head = hotel_quote_per_room,
                                        service_total_amount = hotel_total_amount,
                                        service_vendor_id=vendor_object)
                                        
     return HttpResponseRedirect(reverse('payment:add_services',kwargs={'pk': service_id }))

#-----add_service_restaurantquatation_form_submit Views ------
@login_required(login_url='/user_login')
def add_service_restaurantquatation_form_submit(request,service_id):
    if request.method == "POST":
            restaurantquatation_resturant_name = request.POST['restaurantquatation_resturant_name']
            restaurantquatation_number_of_passengers = request.POST['restaurantquatation_number_of_passengers']
            restaurantquatation_For = request.POST['restaurantquatation_For']
            restaurant_quote_per_head = request.POST['restaurant_quote_per_head']
            restaurant_roe = request.POST['restaurant_roe']
            restaurant_type_of_GST = request.POST['restaurant_type_of_GST']
            restaurant_total_amount = request.POST['restaurant_total_amount']
            vendor_id = request.POST['restaurant_service_vendor_id']
            vendor_object = Vendor.objects.get(pk=vendor_id)
            group_object = Groupdescription.objects.get(pk=service_id)
            RestaurantQuatation.objects.create(restaurantquatation_resturant_name = restaurantquatation_resturant_name,
            restaurantquatation_For = restaurantquatation_For,
                                        service_number_of_passengers = restaurantquatation_number_of_passengers,
                                        service_roe = restaurant_roe,
                                        service_gst = restaurant_type_of_GST,
                                        service_id = group_object,
                                        service_quote_per_head = restaurant_quote_per_head,
                                        service_total_amount = restaurant_total_amount,
                                        service_vendor_id=vendor_object)
    
    return HttpResponseRedirect(reverse('payment:add_services',kwargs={'pk': service_id }))

#-----add_service_entrancesquatation_form_submit Views ------
@login_required(login_url='/user_login')
def add_service_entrancesquatation_form_submit(request,service_id):
    if request.method == "POST":
            entrancesquatation_name = request.POST['entrancesquatation_name']
            entrances_quote_per_head = request.POST['entrances_quote_per_head']
            entrances_number_of_passengers = request.POST['entrances_number_of_passengers']
            entrances_roe = request.POST['entrances_roe']
            entrances_type_of_GST = request.POST['entrances_type_of_GST']
            entrances_total_amount = request.POST['entrances_total_amount']
            vendor_id = request.POST['entrances_service_vendor_id']
            vendor_object = Vendor.objects.get(pk=vendor_id)
            group_object = Groupdescription.objects.get(pk=service_id)
            EntrancesQuatation.objects.create(entrancesquatation_name = entrancesquatation_name,
            service_number_of_passengers = entrances_number_of_passengers,
                                        service_roe = entrances_roe,
                                        service_gst = entrances_type_of_GST,
                                        service_id = group_object,
                                        service_quote_per_head = entrances_quote_per_head,
                                        service_total_amount = entrances_total_amount,
                                        service_vendor_id=vendor_object)
    
    return HttpResponseRedirect(reverse('payment:add_services',kwargs={'pk': service_id }))
 
#-----add_service_sapsanquatation_form_submit Views ------
@login_required(login_url='/user_login')
def add_service_sapsanquatation_form_submit(request,service_id):
    if request.method == "POST":
            sapsanquatation_From_Station = request.POST['sapsanquatation_From_Station']
            sapsanquatation_To_Station = request.POST['sapsanquatation_To_Station']
            sapsan_number_of_passengers = request.POST['sapsan_number_of_passengers']
            sapsan_quote_per_head = request.POST['sapsan_quote_per_head']
            sapsan_roe = request.POST['sapsan_roe']
            sapsan_type_of_GST = request.POST['sapsan_type_of_GST']
            sapsan_total_amount = request.POST['sapsan_total_amount']
            vendor_id = request.POST['sapsan_service_vendor_id']
            vendor_object = Vendor.objects.get(pk=vendor_id)
            group_object = Groupdescription.objects.get(pk=service_id)
            SapSanQuatation.objects.create(sapsanquatation_From_Station = sapsanquatation_From_Station,
                                        sapsanquatation_To_Station = sapsanquatation_To_Station,
                                        service_number_of_passengers = sapsan_number_of_passengers,
                                        service_roe = sapsan_roe,
                                        service_gst = sapsan_type_of_GST,
                                        service_id = group_object,
                                        service_quote_per_head = sapsan_quote_per_head,
                                        service_total_amount = sapsan_total_amount,
                                        service_vendor_id=vendor_object)
    
    return HttpResponseRedirect(reverse('payment:add_services',kwargs={'pk': service_id }))

#-----add_service_guide_form_submit Views ------
@login_required(login_url='/user_login')
def add_service_guide_form_submit(request,service_id):
    if request.method == "POST":

        guide_name = request.POST['guide_name']
        guide_number_of_passengers = request.POST['guide_number_of_passengers']
        guide_destination = request.POST['guide_destination']
        guide_quote_per_hour = request.POST['guide_quote_per_hour']
        guide_roe = request.POST['guide_roe']
        guide_type_of_GST = request.POST['guide_type_of_GST']
        guide_total_amount = request.POST['guide_total_amount']
        vendor_id = request.POST['guide_service_vendor_id']
        
        vendor_object = Vendor.objects.get(pk=vendor_id)
        group_object = Groupdescription.objects.get(pk=service_id)
        Guide.objects.create(Guide_Name = guide_name,
                                Guide_Destination = guide_destination,
                                service_number_of_passengers = guide_number_of_passengers,
                                service_roe = guide_roe,
                                service_gst = guide_type_of_GST,
                                service_id = group_object,
                                service_quote_per_head = guide_quote_per_hour,
                                service_total_amount = guide_total_amount,
                                service_vendor_id=vendor_object)

    return HttpResponseRedirect(reverse('payment:add_services',kwargs={'pk': service_id }))

#-----add_service_transport_form_submit Views ------
@login_required(login_url='/user_login')
def add_service_transport_form_submit(request,service_id):
    if request.method == "POST":

        transport_type_of_vehicle = request.POST['transport_type_of_vehicle']
        transport_quote_per_head = request.POST['transport_quote_per_head']
        transport_roe = request.POST['transport_roe']
        transport_type_of_GST = request.POST['transport_type_of_GST']
        transport_total_amount = request.POST['transport_total_amount']
        vendor_id = request.POST['transport_service_vendor_id']
        
        vendor_object = Vendor.objects.get(pk=vendor_id)
        group_object = Groupdescription.objects.get(pk=service_id)
        Transport.objects.create(transport_type_of_vehicle = transport_type_of_vehicle,
                                service_roe = transport_roe,
                                service_gst = transport_type_of_GST,
                                service_id = group_object,
                                service_quote_per_head = transport_quote_per_head,
                                service_total_amount = transport_total_amount,
                                service_vendor_id=vendor_object)

    return HttpResponseRedirect(reverse('payment:add_services',kwargs={'pk': service_id }))


#</------ All Form Submit Processing Views -----------


# ------ Django Bootstrap Modal Views ------


# --- Tours List CURD Views ---
# Group - Update View
@method_decorator(login_required, name='dispatch')
class PNLstatementUpdateView(BSModalUpdateView):
    model = Groupdescription
    template_name = 'payment/update_entry.html'
    form_class = GroupdescriptionForm_UpdateForm
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('payment:pnllist')

# Group - Delete View
@method_decorator(login_required, name='dispatch')
class PNLstatementDeleteView(BSModalDeleteView):
    model = Groupdescription
    template_name = 'payment/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    success_url = reverse_lazy('payment:pnllist')

# Group - Summary view
@method_decorator(login_required, name='dispatch')
class PNLStatementSummary(BSModalReadView):
    model = Groupdescription
    context_object_name = 'groupdesc'
    template_name = 'payment/read_entry.html'

# -- clientpnlstatementupdateview View --
@method_decorator(login_required, name='dispatch')
class clientpnlstatementupdateview(BSModalUpdateView):
    model = Groupdescription
    template_name = 'payment/update_entry.html'
    form_class = GroupdescriptionForm_UpdateForm
    success_message = 'Success: pnlstatement was updated.'
    
    def get_success_url(self,**kwargs):
        group_object = Groupdescription.objects.get(pk=self.kwargs['pk'])
        client_data_from_groupdescription=group_object.groupdescription_client_id
        client=Client.objects.get(client_name=client_data_from_groupdescription)
        group_clientid = client.pk
        group_paymentstatus = group_object.groupdescription_payment_status
        return reverse_lazy('payment:client_payment_list', kwargs={'client_id':group_clientid, 'payment_status':group_paymentstatus})

# -- clientpnlstatementdeleteview View --
@method_decorator(login_required, name='dispatch')
class clientpnlstatementdeleteview(BSModalDeleteView):
    model = Groupdescription
    template_name = 'payment/delete_entry.html'
    success_message = 'Success: pnlstatement was deleted.'
    success_url = reverse_lazy('payment:pnllist')

# --- Clients CURD Views ---
#Update View
@method_decorator(login_required, name='dispatch')
class ClientUpdateView(BSModalUpdateView):
    model = Client
    template_name = 'payment/update_entry.html'
    form_class = Client_UpdateForm
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('payment:clientlist')


# Delete View
@method_decorator(login_required, name='dispatch')
class ClientDeleteView(BSModalDeleteView):
    model = Client
    template_name = 'payment/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    success_url = reverse_lazy('payment:clientlist')

#Client Summary view
@method_decorator(login_required, name='dispatch')
class ClientSummary(BSModalReadView):
    model = Client
    context_object_name = 'clientlist'
    template_name = 'payment/client_summary.html'

#Client Create View
@method_decorator(login_required, name='dispatch')
class add_new_client_view(BSModalCreateView):
    template_name = 'payment/add_new_client.html'
    form_class = Client_UpdateForm
    success_message = 'Success: Client was added.'
    success_url = reverse_lazy('payment:clientlist')

# --- Client Payment Details List ---
@login_required(login_url='/user_login')
def client_payment_details_list(request,client_id,payment_status):
    clients = Client.objects.all()
    clients_dict = {}
    for client in clients:
        clients_dict[client.client_name] = client.client_name
    userrole = request.user.user_role
    client_name = Client.objects.get(pk=client_id).client_name
    client_object = Client.objects.get(pk=client_id)
    client_pending = Groupdescription.objects.filter(groupdescription_client_id=client_object,groupdescription_payment_status=payment_status).all()
    data = {"userrole":userrole, "groupdesc": client_pending,"payment_status":payment_status,"client_name":client_name,"clients_dict":clients_dict }
    return render(request, 'payment/client_payment_details.html',data)
# </--- Clients CURD Views ---



# ---- Vendors CURD views ----
#Update View
@method_decorator(login_required, name='dispatch')
class VendorUpdateView(BSModalUpdateView):
    model = Vendor
    template_name = 'payment/update_entry.html'
    form_class = Vendor_UpdateForm
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('payment:vendorlist')

# Delete View
@method_decorator(login_required, name='dispatch')
class VendorDeleteView(BSModalDeleteView):
    model = Vendor
    template_name = 'payment/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    success_url = reverse_lazy('payment:vendorlist')

#Vendor Summary view
@method_decorator(login_required, name='dispatch')
class VendorSummary(BSModalReadView):
    model = Vendor
    context_object_name = 'vendorlist'
    template_name = 'payment/vendor_summary.html'

#Vendor Create View
@method_decorator(login_required, name='dispatch')
class add_new_vendor_view(BSModalCreateView):
    template_name = 'payment/add_new_vendor.html'
    form_class = Vendor_UpdateForm
    success_message = 'Success: Vendor was added.'
    success_url = reverse_lazy('payment:vendorlist')

# --- Vendor Payment Details List ---
@login_required(login_url='/user_login')
def vendor_payment_details_list(request,vendor_id,payment_status):
    group_objects = Groupdescription.objects.all()
    group_dict = {}
    for group_object in group_objects:
        group_dict[group_object.pk] = group_object.groupdescription_vtrefNo 

    vendor_name = Vendor.objects.get(pk=vendor_id).vendor_name
    vendor_object = Vendor.objects.get(pk=vendor_id)
    vendor_pending = Service.objects.filter(service_vendor_id=vendor_object,service_vendor_payment_status=payment_status).all()
    air_tickets = AirTicketsQuatation.objects.all().filter(service_vendor_id=vendor_object,service_vendor_payment_status=payment_status)
    visa_costs = VisaCostQuatation.objects.all().filter(service_vendor_id=vendor_object,service_vendor_payment_status=payment_status)
    hotel_quatations = HotelQuatation.objects.all().filter(service_vendor_id=vendor_object,service_vendor_payment_status=payment_status)
    restaurant_quatations = RestaurantQuatation.objects.all().filter(service_vendor_id=vendor_object,service_vendor_payment_status=payment_status)
    entrances_quatations = EntrancesQuatation.objects.all().filter(service_vendor_id=vendor_object,service_vendor_payment_status=payment_status)
    sapsan_quatations = SapSanQuatation.objects.all().filter(service_vendor_id=vendor_object,service_vendor_payment_status=payment_status)
    guide_names = Guide.objects.all().filter(service_vendor_id=vendor_object,service_vendor_payment_status=payment_status)
    sum = 0
    for airticket in air_tickets:
        sum = sum + airticket.service_total_amount
    for visacost in visa_costs:
        sum = sum + visacost.service_total_amount
    for hotel in hotel_quatations:
        sum = sum + hotel.service_total_amount
    for restaurant in restaurant_quatations:
        sum = sum + restaurant.service_total_amount
    for entrance in entrances_quatations:
        sum = sum + entrance.service_total_amount
    for sapsan in sapsan_quatations:
        sum = sum + sapsan.service_total_amount
    for guide in guide_names:
        sum = sum + guide.service_total_amount
    payment_total = sum
    data = {"vendor_pending": vendor_pending,"payment_status":payment_status,"vendor_name":vendor_name,'payment_total':payment_total,'group_dict':group_dict }
    return render(request, 'payment/vendor_payment_details.html',data)

# </---- Vendors CURD views ----

# -- vendorserviceupdateview View --
@method_decorator(login_required, name='dispatch')
class vendorserviceupdateview(BSModalUpdateView):
    model = Service
    template_name = 'payment/update_entry.html'
    form_class = ServiceForm_UpdateForm
    success_message = 'Success: Service was updated.'
    
    def get_success_url(self,**kwargs):
        service_object = Service.objects.get(pk=self.kwargs['pk'])
        vendor_data_from_service=service_object.service_vendor_id
        vendor= Vendor.objects.get(vendor_name=vendor_data_from_service)
        service_vendorid = vendor.pk
        service_paymentstatus = service_object.service_vendor_payment_status
        return reverse_lazy('payment:vendor_payment_list', kwargs={'vendor_id':service_vendorid, 'payment_status':service_paymentstatus })

# -- vendorservicedeleteview View --
@method_decorator(login_required, name='dispatch')
class vendorservicedeleteview(BSModalDeleteView):
    model = Service
    template_name = 'payment/delete_entry.html'
    success_message = 'Success: Service was deleted.'

    def get_success_url(self,**kwargs):
        service_object = Service.objects.get(pk=self.kwargs['pk'])
        vendor_data_from_service=service_object.service_vendor_id
        vendor= Vendor.objects.get(vendor_name=vendor_data_from_service)
        service_vendorid = vendor.pk
        service_paymentstatus = service_object.service_vendor_payment_status
        return reverse_lazy('payment:vendor_payment_list', kwargs={'vendor_id':service_vendorid, 'payment_status':service_paymentstatus})

# ---- Addservices CURD views ----
#-----add_services airticket----- 
#Update View
@method_decorator(login_required, name='dispatch')
class AddServiceAirTicketUpdateView(BSModalUpdateView):
    model = AirTicketsQuatation
    template_name = 'payment/update_entry.html'
    form_class = AddAirticket
    success_message = 'Success: Entry was updated.'
    def get_success_url(self,**kwargs):
        Airticket_Model_Object = AirTicketsQuatation.objects.get(pk=self.kwargs['pk'])
        group_description_pk = Airticket_Model_Object.service_id
        return reverse_lazy('payment:add_services', kwargs={'pk': group_description_pk })

# Delete View
@method_decorator(login_required, name='dispatch')
class AddServiceAirTicketDeleteView(BSModalDeleteView):
    model = AirTicketsQuatation
    template_name = 'payment/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    success_url = reverse_lazy('payment:add_services')
    def get_success_url(self,**kwargs):
        Airticket_Model_Object = AirTicketsQuatation.objects.get(pk=self.kwargs['pk'])
        group_description_pk = Airticket_Model_Object.service_id
        return reverse_lazy('payment:add_services', kwargs={'pk': group_description_pk })
#</-----add_services airticket-----
#-----add_services visacost----- 
#Update View
@method_decorator(login_required, name='dispatch')
class AddServiceVisaCostUpdateView(BSModalUpdateView):
    model = VisaCostQuatation
    template_name = 'payment/update_entry.html'
    form_class = AddVisacost
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('payment:add_services')
    def get_success_url(self,**kwargs):
        VisaCost_Model_Object = VisaCostQuatation.objects.get(pk=self.kwargs['pk'])
        group_description_pk = VisaCost_Model_Object.service_id
        return reverse_lazy('payment:add_services', kwargs={'pk': group_description_pk })

# Delete View
@method_decorator(login_required, name='dispatch')
class AddServiceVisaCostDeleteView(BSModalDeleteView):
    model = VisaCostQuatation
    template_name = 'payment/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    success_url = reverse_lazy('payment:add_services')
    def get_success_url(self,**kwargs):
        VisaCost_Model_Object = VisaCostQuatation.objects.get(pk=self.kwargs['pk'])
        group_description_pk = VisaCost_Model_Object.service_id
        return reverse_lazy('payment:add_services', kwargs={'pk': group_description_pk })
#</-----add_services visacost -----
#-----add_services hotel----- 
#Update View
@method_decorator(login_required, name='dispatch')
class AddServiceHotelUpdateView(BSModalUpdateView):
    model = HotelQuatation
    template_name = 'payment/update_entry.html'
    form_class = AddHotel
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('payment:add_services')
    def get_success_url(self,**kwargs):
        Hotel_Model_Object = HotelQuatation.objects.get(pk=self.kwargs['pk'])
        group_description_pk = Hotel_Model_Object.service_id
        return reverse_lazy('payment:add_services', kwargs={'pk': group_description_pk })

# Delete View
@method_decorator(login_required, name='dispatch')
class AddServiceHotelDeleteView(BSModalDeleteView):
    model = HotelQuatation
    template_name = 'payment/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    success_url = reverse_lazy('payment:add_services')
    def get_success_url(self,**kwargs):
        Hotel_Model_Object = HotelQuatation.objects.get(pk=self.kwargs['pk'])
        group_description_pk = Hotel_Model_Object.service_id
        return reverse_lazy('payment:add_services', kwargs={'pk': group_description_pk })
#</-----add_services hotel -----
#-----add_services restaurant----- 
#Update View
@method_decorator(login_required, name='dispatch')
class AddServiceRestaurantUpdateView(BSModalUpdateView):
    model = RestaurantQuatation
    template_name = 'payment/update_entry.html'
    form_class = AddRestaurant
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('payment:add_services')
    def get_success_url(self,**kwargs):
        Restaurant_Model_Object = RestaurantQuatation.objects.get(pk=self.kwargs['pk'])
        group_description_pk = Restaurant_Model_Object.service_id
        return reverse_lazy('payment:add_services', kwargs={'pk': group_description_pk })

# Delete View
@method_decorator(login_required, name='dispatch')
class AddServiceRestaurantDeleteView(BSModalDeleteView):
    model = RestaurantQuatation
    template_name = 'payment/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    success_url = reverse_lazy('payment:add_services')
    def get_success_url(self,**kwargs):
        Restaurant_Model_Object = RestaurantQuatation.objects.get(pk=self.kwargs['pk'])
        group_description_pk = Restaurant_Model_Object.service_id
        return reverse_lazy('payment:add_services', kwargs={'pk': group_description_pk })
#</-----add_services restaurant -----

#-----add_services entrances----- 
#Update View
@method_decorator(login_required, name='dispatch')
class AddServiceEntrancesUpdateView(BSModalUpdateView):
    model = EntrancesQuatation
    template_name = 'payment/update_entry.html'
    form_class = AddEntrances
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('payment:add_services')
    def get_success_url(self,**kwargs):
        Entrance_Model_Object = EntrancesQuatation.objects.get(pk=self.kwargs['pk'])
        group_description_pk = Entrance_Model_Object.service_id
        return reverse_lazy('payment:add_services', kwargs={'pk': group_description_pk })

# Delete View
@method_decorator(login_required, name='dispatch')
class AddServiceEntrancesDeleteView(BSModalDeleteView):
    model = EntrancesQuatation
    template_name = 'payment/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    success_url = reverse_lazy('payment:add_services')
    def get_success_url(self,**kwargs):
        Entrance_Model_Object = EntrancesQuatation.objects.get(pk=self.kwargs['pk'])
        group_description_pk = Entrance_Model_Object.service_id
        return reverse_lazy('payment:add_services', kwargs={'pk': group_description_pk })
#</-----add_services entrances -----

#-----add_services sapsan----- 
#Update View
@method_decorator(login_required, name='dispatch')
class AddServiceSapSanUpdateView(BSModalUpdateView):
    model = SapSanQuatation
    template_name = 'payment/update_entry.html'
    form_class = AddSapsan
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('payment:add_services')
    def get_success_url(self,**kwargs):
        Sapsan_Model_Object = SapSanQuatation.objects.get(pk=self.kwargs['pk'])
        group_description_pk = Sapsan_Model_Object.service_id
        return reverse_lazy('payment:add_services', kwargs={'pk': group_description_pk })

# Delete View
@method_decorator(login_required, name='dispatch')
class AddServiceSapSanDeleteView(BSModalDeleteView):
    model = SapSanQuatation
    template_name = 'payment/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    success_url = reverse_lazy('payment:add_services')
    def get_success_url(self,**kwargs):
        Sapsan_Model_Object = SapSanQuatation.objects.get(pk=self.kwargs['pk'])
        group_description_pk = Sapsan_Model_Object.service_id
        return reverse_lazy('payment:add_services', kwargs={'pk': group_description_pk })
#</-----add_services sapsan -----

#-----add_services guide----- 
#Update View
@method_decorator(login_required, name='dispatch')
class AddServiceGuideUpdateView(BSModalUpdateView):
    model = Guide
    template_name = 'payment/update_entry.html'
    form_class = AddGuide
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('payment:add_services')
    def get_success_url(self,**kwargs):
        Guide_Model_Object = Guide.objects.get(pk=self.kwargs['pk'])
        group_description_pk = Guide_Model_Object.service_id
        return reverse_lazy('payment:add_services', kwargs={'pk': group_description_pk })

# Delete View
@method_decorator(login_required, name='dispatch')
class AddServiceGuideDeleteView(BSModalDeleteView):
    model = Guide
    template_name = 'payment/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    success_url = reverse_lazy('payment:add_services')
    def get_success_url(self,**kwargs):
        Guide_Model_Object = Guide.objects.get(pk=self.kwargs['pk'])
        group_description_pk = Guide_Model_Object.service_id
        return reverse_lazy('payment:add_services', kwargs={'pk': group_description_pk })
#</-----add_services guide -----

#-----add_services transport----- 
#Update View
@method_decorator(login_required, name='dispatch')
class AddServiceTransportUpdateView(BSModalUpdateView):
    model = Transport
    template_name = 'payment/update_entry.html'
    form_class = AddTransport
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('payment:add_services')
    def get_success_url(self,**kwargs):
        Transport_Model_Object = Transport.objects.get(pk=self.kwargs['pk'])
        group_description_pk = Transport_Model_Object.service_id
        return reverse_lazy('payment:add_services', kwargs={'pk': group_description_pk })

# Delete View
@method_decorator(login_required, name='dispatch')
class AddServiceTransportDeleteView(BSModalDeleteView):
    model = Transport
    template_name = 'payment/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    success_url = reverse_lazy('payment:add_services')
    def get_success_url(self,**kwargs):
        Transport_Model_Object = Transport.objects.get(pk=self.kwargs['pk'])
        group_description_pk = Transport_Model_Object.service_id
        return reverse_lazy('payment:add_services', kwargs={'pk': group_description_pk })
#</-----add_services transport -----
#</--- Addservices CURD Views ---

# --- vendor_accounts_airticket_quatation CURD Views ---
#Update View
@method_decorator(login_required, name='dispatch')
class VendorAirticketUpdateView(BSModalUpdateView):
    model = Vendor
    template_name = 'payment/update_entry.html'
    form_class = Vendor_UpdateForm
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('payment:vendor_accounts_airticket_quatation')

# Delete View
@method_decorator(login_required, name='dispatch')
class VendorAirticketDeleteView(BSModalDeleteView):
    model =  Vendor
    template_name = 'payment/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    success_url = reverse_lazy('payment:vendor_accounts_airticket_quatation')

#Airticket Create View
@method_decorator(login_required, name='dispatch')
class add_new_airticket_view(BSModalCreateView):
    template_name = 'payment/add_new_airticket.html'
    form_class = Vendor_UpdateForm
    success_message = 'Success: New Airticket was added.'
    success_url = reverse_lazy('payment:vendor_accounts_airticket_quatation')

#Update View
@method_decorator(login_required, name='dispatch')
class VendorAirticketDetailUpdateView(BSModalUpdateView):
    model = AirTicketsQuatation
    template_name = 'payment/update_entry.html'
    form_class = AddAirticket
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('payment:vendor_accounts_airticket_quatation_details')
    def get_success_url(self,**kwargs):
        Airticket_Model_Object = AirTicketsQuatation.objects.get(pk=self.kwargs['pk'])
        vendor_id = int(str(Airticket_Model_Object.service_vendor_id))
        payment_status = Airticket_Model_Object.service_vendor_payment_status
        return reverse_lazy('payment:vendor_accounts_airticket_quatation_details', kwargs={'vendor_id': vendor_id,'payment_status':payment_status })


# Delete View
@method_decorator(login_required, name='dispatch')
class VendorAirticketDetailDeleteView(BSModalDeleteView):
    model =  AirTicketsQuatation
    template_name = 'payment/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    def get_success_url(self,**kwargs):
        Airticket_Model_Object = AirTicketsQuatation.objects.get(pk=self.kwargs['pk'])
        vendor_id = int(str(Airticket_Model_Object.service_vendor_id))
        payment_status = Airticket_Model_Object.service_vendor_payment_status
        return reverse_lazy('payment:vendor_accounts_airticket_quatation_details', kwargs={'vendor_id': vendor_id,'payment_status':payment_status })


# --- vendor_accounts_airticket_quatation_details View ---
@login_required(login_url='/user_login')
def vendor_accounts_airticket_quatation_details(request,vendor_id,payment_status):
    userrole = request.user.user_role
    vendor_pending = AirTicketsQuatation.objects.filter(service_vendor_id=vendor_id,service_vendor_payment_status=payment_status).all()
    data = {"userrole":userrole, "airtickets": vendor_pending }
    return render(request, 'payment/vendor_accounts_airticket_quatation_details.html',data)


# </--- vendor_accounts_airticket_quatation CURD Views ---


# --- vendor_accounts_visacost_quatation CURD Views ---
#Update View
@method_decorator(login_required, name='dispatch')
class VendorVisaCostUpdateView(BSModalUpdateView):
    model = Vendor
    template_name = 'payment/update_entry.html'
    form_class = Vendor_UpdateForm
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('payment:vendor_accounts_visacost_quatation')

# Delete View
@method_decorator(login_required, name='dispatch')
class VendorVisaCostDeleteView(BSModalDeleteView):
    model = Vendor
    template_name = 'payment/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    success_url = reverse_lazy('payment:vendor_accounts_airticket_quatation')

#visacost Create View
@method_decorator(login_required, name='dispatch')
class add_new_visacost_view(BSModalCreateView):
    template_name = 'payment/add_new_visacost.html'
    form_class = Vendor_UpdateForm
    success_message = 'Success: New Visacost was added.'
    success_url = reverse_lazy('payment:vendor_accounts_visacost_quatation')

#Update View
@method_decorator(login_required, name='dispatch')
class VendorVisaCostDetailUpdateView(BSModalUpdateView):
    model = VisaCostQuatation
    template_name = 'payment/update_entry.html'
    form_class = AddVisacost
    success_message = 'Success: Entry was updated.'
    
    def get_success_url(self,**kwargs):
        Visacost_Model_Object = VisaCostQuatation.objects.get(pk=self.kwargs['pk'])
        vendor_id = int(str(Visacost_Model_Object.service_vendor_id))
        payment_status = Visacost_Model_Object.service_vendor_payment_status
        return reverse_lazy('payment:vendor_accounts_visacost_quatation_details', kwargs={'vendor_id': vendor_id,'payment_status':payment_status })


# Delete View
@method_decorator(login_required, name='dispatch')
class VendorVisaCostDetailDeleteView(BSModalDeleteView):
    model =  VisaCostQuatation
    template_name = 'payment/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    def get_success_url(self,**kwargs):
        Visacost_Model_Object = VisaCostQuatation.objects.get(pk=self.kwargs['pk'])
        vendor_id = int(str(Visacost_Model_Object.service_vendor_id))
        payment_status = Visacost_Model_Object.service_vendor_payment_status
        return reverse_lazy('payment:vendor_accounts_visacost_quatation_details', kwargs={'vendor_id': vendor_id,'payment_status':payment_status })


# --- vendor_accounts_visacost_quatation_details View ---
@login_required(login_url='/user_login')
def vendor_accounts_visacost_quatation_details(request,vendor_id,payment_status):
    userrole = request.user.user_role
    vendor_pending = VisaCostQuatation.objects.filter(service_vendor_id=vendor_id,service_vendor_payment_status=payment_status).all()
    data = {"userrole":userrole, "visacosts": vendor_pending }
    return render(request, 'payment/vendor_accounts_visacost_quatation_details.html',data)
# </--- vendor_accounts_visacost_quatation CURD Views ---

#------vendor_accounts_hotel_quatation Curd Views
#vendor_hotel Update View
@method_decorator(login_required, name='dispatch')
class VendorHotelUpdateView(BSModalUpdateView):
    model = Vendor
    template_name = 'payment/update_entry.html'
    form_class = Vendor_UpdateForm 
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('payment:vendor_accounts_hotel_quatation')

#vendor_hotel Delete View
@method_decorator(login_required, name='dispatch')
class VendorHotelDeleteView(BSModalDeleteView):
    model = Vendor
    template_name = 'payment/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    success_url = reverse_lazy('payment:vendor_accounts_hotel_quatation')

#hotelquatation Create View
@method_decorator(login_required, name='dispatch')
class add_new_hotel_view(BSModalCreateView):
    template_name = 'payment/add_new_hotel.html'
    form_class = Vendor_UpdateForm
    success_message = 'Success: New Hotel was added.'
    success_url = reverse_lazy('payment:vendor_accounts_hotel_quatation')

#Update View
@method_decorator(login_required, name='dispatch')
class VendorHotelDetailUpdateView(BSModalUpdateView):
    model = HotelQuatation
    template_name = 'payment/update_entry.html'
    form_class = AddHotel
    success_message = 'Success: Entry was updated.'
    
    def get_success_url(self,**kwargs):
        Hotel_Model_Object = HotelQuatation.objects.get(pk=self.kwargs['pk'])
        vendor_id = int(str(Hotel_Model_Object.service_vendor_id))
        payment_status = Hotel_Model_Object.service_vendor_payment_status
        return reverse_lazy('payment:vendor_accounts_hotel_quatation_details', kwargs={'vendor_id': vendor_id,'payment_status':payment_status })


# Delete View
@method_decorator(login_required, name='dispatch')
class VendorHotelDetailDeleteView(BSModalDeleteView):
    model =  HotelQuatation
    template_name = 'payment/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    
    def get_success_url(self,**kwargs):
        Hotel_Model_Object = HotelQuatation.objects.get(pk=self.kwargs['pk'])
        vendor_id = int(str(Hotel_Model_Object.service_vendor_id))
        payment_status = Hotel_Model_Object.service_vendor_payment_status
        return reverse_lazy('payment:vendor_accounts_hotel_quatation_details', kwargs={'vendor_id': vendor_id,'payment_status':payment_status })



# --- vendor_accounts_hotel_quatation_details View ---
@login_required(login_url='/user_login')
def vendor_accounts_hotel_quatation_details(request,vendor_id,payment_status):
    userrole = request.user.user_role
    vendor_pending = HotelQuatation.objects.filter(service_vendor_id=vendor_id,service_vendor_payment_status=payment_status).all()
    data = {"userrole":userrole, "hotels": vendor_pending }
    return render(request, 'payment/vendor_accounts_hotel_quatation_details.html',data)
#</------vendor_accounts_hotel_quatation Curd Views


# --- vendor_accounts_restaurant_quatation CURD Views ---
#vendor_restaurant update
@method_decorator(login_required, name='dispatch')
class VendorRestaurantUpdateView(BSModalUpdateView):
    model = Vendor
    template_name = 'payment/update_entry.html'
    form_class = Vendor_UpdateForm 
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('payment:vendor_accounts_restaurant_quatation')

#vendor_restaurant delete
@method_decorator(login_required, name='dispatch')
class VendorRestaurantDeleteView(BSModalDeleteView):
    model = Vendor
    template_name = 'payment/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    success_url = reverse_lazy('payment:vendor_accounts_restaurant_quatation')

#RestaurantQuatation Create View
@method_decorator(login_required, name='dispatch')
class add_new_restaurant_view(BSModalCreateView):
    template_name = 'payment/add_new_restaurant.html'
    form_class = Vendor_UpdateForm
    success_message = 'Success: New Restaurant was added.'
    success_url = reverse_lazy('payment:vendor_accounts_restaurant_quatation')


@method_decorator(login_required, name='dispatch')
class VendorRestaurantDetailUpdateView(BSModalUpdateView):
    model = RestaurantQuatation
    template_name = 'payment/update_entry.html'
    form_class = AddRestaurant 
    success_message = 'Success: Entry was updated.'
    
    def get_success_url(self,**kwargs):
        Restaurant_Model_Object = RestaurantQuatation.objects.get(pk=self.kwargs['pk'])
        vendor_id = int(str(Restaurant_Model_Object.service_vendor_id))
        payment_status = Restaurant_Model_Object.service_vendor_payment_status
        return reverse_lazy('payment:vendor_accounts_restaurant_quatation_details', kwargs={'vendor_id': vendor_id,'payment_status':payment_status })


#vendor_restaurant delete
@method_decorator(login_required, name='dispatch')
class VendorRestaurantDetailDeleteView(BSModalDeleteView):
    model = RestaurantQuatation
    template_name = 'payment/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    def get_success_url(self,**kwargs):
        Restaurant_Model_Object = RestaurantQuatation.objects.get(pk=self.kwargs['pk'])
        vendor_id = int(str(Restaurant_Model_Object.service_vendor_id))
        payment_status = Restaurant_Model_Object.service_vendor_payment_status
        return reverse_lazy('payment:vendor_accounts_restaurant_quatation_details', kwargs={'vendor_id': vendor_id,'payment_status':payment_status })

# --- vendor_accounts_restaurant_quatation_details View ---

@login_required(login_url='/user_login')
def vendor_accounts_restaurant_quatation_details(request,vendor_id,payment_status):
    userrole = request.user.user_role
    vendor_pending = RestaurantQuatation.objects.filter(service_vendor_id=vendor_id,service_vendor_payment_status=payment_status).all()
    data = {"userrole":userrole, "restaurants": vendor_pending }
    return render(request, 'payment/vendor_accounts_restaurant_quatation_details.html',data)
# </--- vendor_accounts_restaurant_quatation CURD Views ---

# --- vendor_accounts_entrances_quatation CURD Views ---
#vendor_entrances update
@method_decorator(login_required, name='dispatch')
class VendorEntrancesUpdateView(BSModalUpdateView):
    model = Vendor
    template_name = 'payment/update_entry.html'
    form_class = Vendor_UpdateForm 
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('payment:vendor_accounts_entrances_quatation')

#vendor_entrances delete
@method_decorator(login_required, name='dispatch')
class VendorEntrancesDeleteView(BSModalDeleteView):
    model = Vendor
    template_name = 'payment/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    success_url = reverse_lazy('payment:vendor_accounts_entrances_quatation')

#EntrancesQuatation Create View
@method_decorator(login_required, name='dispatch')
class add_new_entrances_view(BSModalCreateView):
    template_name = 'payment/add_new_entrances.html'
    form_class = Vendor_UpdateForm
    success_message = 'Success: New Entrances was added.'
    success_url = reverse_lazy('payment:vendor_accounts_entrances_quatation')

@method_decorator(login_required, name='dispatch')
class VendorEntrancesDetailUpdateView(BSModalUpdateView):
    model = EntrancesQuatation
    template_name = 'payment/update_entry.html'
    form_class = AddEntrances 
    success_message = 'Success: Entry was updated.'
    
    def get_success_url(self,**kwargs):
        Entrances_Model_Object = EntrancesQuatation.objects.get(pk=self.kwargs['pk'])
        vendor_id = int(str(Entrances_Model_Object.service_vendor_id))
        payment_status = Entrances_Model_Object.service_vendor_payment_status
        return reverse_lazy('payment:vendor_accounts_entrances_quatation_details', kwargs={'vendor_id': vendor_id,'payment_status':payment_status })


#vendor_entrances delete
@method_decorator(login_required, name='dispatch')
class VendorEntrancesDetailDeleteView(BSModalDeleteView):
    model = EntrancesQuatation
    template_name = 'payment/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    def get_success_url(self,**kwargs):
        Entrances_Model_Object = EntrancesQuatation.objects.get(pk=self.kwargs['pk'])
        vendor_id = int(str(Entrances_Model_Object.service_vendor_id))
        payment_status = Entrances_Model_Object.service_vendor_payment_status
        return reverse_lazy('payment:vendor_accounts_entrances_quatation_details', kwargs={'vendor_id': vendor_id,'payment_status':payment_status })


# --- vendor_accounts_entrances_quatation_details View ---
@login_required(login_url='/user_login')
def vendor_accounts_entrances_quatation_details(request,vendor_id,payment_status):
    userrole = request.user.user_role
    vendor_pending = EntrancesQuatation.objects.filter(service_vendor_id=vendor_id,service_vendor_payment_status=payment_status).all()
    data = {"userrole":userrole, "entrances": vendor_pending }
    return render(request, 'payment/vendor_accounts_entrances_quatation_details.html',data)
# </--- vendor_accounts_entrances_quatation CURD Views ---

# --- vendor_accounts_sapsan_quatation CURD Views ---
#vendor_sapsan update
@method_decorator(login_required, name='dispatch')
class VendorSapSanUpdateView(BSModalUpdateView):
    model = Vendor
    template_name = 'payment/update_entry.html'
    form_class = Vendor_UpdateForm 
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('payment:vendor_accounts_sapsan_quatation')

#vendor_sapsan delete
@method_decorator(login_required, name='dispatch')
class VendorSapSanDeleteView(BSModalDeleteView):
    model = Vendor
    template_name = 'payment/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    success_url = reverse_lazy('payment:vendor_accounts_sapsan_quatation')

#SapSanQuatation Create View
@method_decorator(login_required, name='dispatch')
class add_new_sapsan_view(BSModalCreateView):
    template_name = 'payment/add_new_sapsan.html'
    form_class = Vendor_UpdateForm
    success_message = 'Success: New Sapsan was added.'
    success_url = reverse_lazy('payment:vendor_accounts_sapsan_quatation')

@method_decorator(login_required, name='dispatch')
class VendorSapSanDetailUpdateView(BSModalUpdateView):
    model = SapSanQuatation
    template_name = 'payment/update_entry.html'
    form_class = AddSapsan 
    success_message = 'Success: Entry was updated.'
    def get_success_url(self,**kwargs):
        Sapsan_Model_Object = SapSanQuatation.objects.get(pk=self.kwargs['pk'])
        vendor_id = int(str(Sapsan_Model_Object.service_vendor_id))
        payment_status = Sapsan_Model_Object.service_vendor_payment_status
        return reverse_lazy('payment:vendor_accounts_sapsan_quatation_details', kwargs={'vendor_id': vendor_id,'payment_status':payment_status })


#vendor_sapsan delete
@method_decorator(login_required, name='dispatch')
class VendorSapSanDetailDeleteView(BSModalDeleteView):
    model = SapSanQuatation
    template_name = 'payment/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    def get_success_url(self,**kwargs):
        Sapsan_Model_Object = SapSanQuatation.objects.get(pk=self.kwargs['pk'])
        vendor_id = int(str(Sapsan_Model_Object.service_vendor_id))
        payment_status = Sapsan_Model_Object.service_vendor_payment_status
        return reverse_lazy('payment:vendor_accounts_sapsan_quatation_details', kwargs={'vendor_id': vendor_id,'payment_status':payment_status })


# --- vendor_accounts_sapsan_quatation_details View ---
@login_required(login_url='/user_login')
def vendor_accounts_sapsan_quatation_details(request,vendor_id,payment_status):
    userrole = request.user.user_role
    vendor_pending = SapSanQuatation.objects.filter(service_vendor_id=vendor_id,service_vendor_payment_status=payment_status).all()
    data = {"userrole":userrole, "sapsans": vendor_pending }
    return render(request, 'payment/vendor_accounts_sapsan_quatation_details.html',data)
# </--- vendor_accounts_sapsan_quatation CURD Views ---

# <--- vendor_accounts_guide CURD Views ---
#vendor_guide update
@method_decorator(login_required, name='dispatch')
class VendorGuideUpdateView(BSModalUpdateView):
    model = Vendor
    template_name = 'payment/update_entry.html'
    form_class = Vendor_UpdateForm 
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('payment:vendor_accounts_guide')

#vendor_guide delete
@method_decorator(login_required, name='dispatch')
class VendorGuideDeleteView(BSModalDeleteView):
    model = Vendor
    template_name = 'payment/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    success_url = reverse_lazy('payment:vendor_accounts_guide')

#Guide Create View
@method_decorator(login_required, name='dispatch')
class add_new_guide_view(BSModalCreateView):
    template_name = 'payment/add_new_guide.html'
    form_class = Vendor_UpdateForm
    success_message = 'Success: New Guide was added.'
    success_url = reverse_lazy('payment:vendor_accounts_guide')


#vendor_guide_detail update
@method_decorator(login_required, name='dispatch')
class VendorGuideDetailUpdateView(BSModalUpdateView):
    model = Guide
    template_name = 'payment/update_entry.html'
    form_class = AddGuide 
    success_message = 'Success: Entry was updated.'
    def get_success_url(self,**kwargs):
        Guide_Model_Object = Guide.objects.get(pk=self.kwargs['pk'])
        vendor_id = int(str(Guide_Model_Object.service_vendor_id))
        payment_status = Guide_Model_Object.service_vendor_payment_status
        return reverse_lazy('payment:vendor_accounts_guide_details', kwargs={'vendor_id': vendor_id,'payment_status':payment_status })


#vendor_guide_detail delete
@method_decorator(login_required, name='dispatch')
class VendorGuideDetailDeleteView(BSModalDeleteView):
    model = Guide
    template_name = 'payment/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    success_url = reverse_lazy('payment:vendor_accounts_guide_details')
    def get_success_url(self,**kwargs):
        Guide_Model_Object = Guide.objects.get(pk=self.kwargs['pk'])
        vendor_id = int(str(Guide_Model_Object.service_vendor_id))
        payment_status = Guide_Model_Object.service_vendor_payment_status
        return reverse_lazy('payment:vendor_accounts_guide_details', kwargs={'vendor_id': vendor_id,'payment_status':payment_status })


# --- vendor_accounts_guide_details View ---
@login_required(login_url='/user_login')
def vendor_accounts_guide_details(request,vendor_id,payment_status):
    userrole = request.user.user_role
    vendor_pending = Guide.objects.filter(service_vendor_id=vendor_id,service_vendor_payment_status=payment_status).all()
    data = {"userrole":userrole, "guides": vendor_pending }
    return render(request, 'payment/vendor_accounts_guide_details.html',data)

# </--- vendor_accounts_transport CURD Views ---

# <--- vendor_accounts_transport CURD Views ---
#vendor_transport update
@method_decorator(login_required, name='dispatch')
class VendorTransportUpdateView(BSModalUpdateView):
    model = Vendor
    template_name = 'payment/update_entry.html'
    form_class = Vendor_UpdateForm 
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('payment:vendor_accounts_transport')

#vendor_transport delete
@method_decorator(login_required, name='dispatch')
class VendorTransportDeleteView(BSModalDeleteView):
    model = Vendor
    template_name = 'payment/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    success_url = reverse_lazy('payment:vendor_accounts_transport')

#Transport Create View
@method_decorator(login_required, name='dispatch')
class add_new_transport_view(BSModalCreateView):
    template_name = 'payment/add_new_guide.html'
    form_class = Vendor_UpdateForm
    success_message = 'Success: New Guide was added.'
    success_url = reverse_lazy('payment:vendor_accounts_transport')


#vendor_transport_detail update
@method_decorator(login_required, name='dispatch')
class VendorTransportDetailUpdateView(BSModalUpdateView):
    model = Transport
    template_name = 'payment/update_entry.html'
    form_class = AddTransport 
    success_message = 'Success: Entry was updated.'
    def get_success_url(self,**kwargs):
        Transport_Model_Object = Transport.objects.get(pk=self.kwargs['pk'])
        vendor_id = int(str(Transport_Model_Object.service_vendor_id))
        payment_status = Transport_Model_Object.service_vendor_payment_status
        return reverse_lazy('payment:vendor_accounts_transport_details', kwargs={'vendor_id': vendor_id,'payment_status':payment_status })

#vendor_transport_detail delete
@method_decorator(login_required, name='dispatch')
class VendorTransportDetailDeleteView(BSModalDeleteView):
    model = Transport
    template_name = 'payment/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    success_url = reverse_lazy('payment:vendor_accounts_transport_details')
    def get_success_url(self,**kwargs):
        Transport_Model_Object = Transport.objects.get(pk=self.kwargs['pk'])
        vendor_id = int(str(Transport_Model_Object.service_vendor_id))
        payment_status = Transport_Model_Object.service_vendor_payment_status
        return reverse_lazy('payment:vendor_accounts_transport_details', kwargs={'vendor_id': vendor_id,'payment_status':payment_status })

# --- vendor_accounts_transport_details View ---
@login_required(login_url='/user_login')
def vendor_accounts_transport_details(request,vendor_id,payment_status):
    userrole = request.user.user_role
    vendor_pending = Transport.objects.filter(service_vendor_id=vendor_id,service_vendor_payment_status=payment_status).all()
    data = {"userrole":userrole, "transports": vendor_pending }
    return render(request, 'payment/vendor_accounts_transport_details.html',data)


# </--- vendor_accounts_transport CURD Views ---

#Create airticketquatation
""" class AirTicketCreateView(BSModalCreateView):
    template_name = 'payment/create_airticket.html'
    form_class = AirTicketFormSubmit
    context_object_name = 'airticket'
    success_message = 'Success: Air Ticket Quatation was created.'
    success_url = reverse_lazy('add_services') """

#Create vissacostquatation
""" class VisaCostCreateView(BSModalCreateView):
    template_name = 'payment/create_visacost.html'
    form_class = VisaCostFormSubmit
    success_message = 'Success: Visa Cost Quatation was created.'
    success_url = reverse_lazy('add_services')  """

#Create hotelquatation
""" class HotelQuatationCreateView(BSModalCreateView):
    template_name = 'payment/create_hotelquatation.html'
    form_class = HotelQuatationForm
    success_message = 'Success: Hotel Quatation was created.'
    success_url = reverse_lazy('add_services') """


#Create restaurantquatation
""" class RestaurantQuatationCreateView(BSModalCreateView):
    template_name = 'payment/create_restaurantquatation.html'
    form_class = RestaurantQuatationForm
    success_message = 'Success: Restaurant Quatation was created.'
    success_url = reverse_lazy('add_services') """

#Create airticketquatation
""" class EntrancesQuatationCreateView(BSModalCreateView):
    template_name = 'payment/create_entrancesquatation.html'
    form_class = EntrancesQuatationForm
    success_message = 'Success: Entrances Quatation was created.'
    success_url = reverse_lazy('add_services') """


#Create airticketquatation
""" class SapSanQuatationCreateView(BSModalCreateView):
    template_name = 'payment/create_sapsanquatation.html'
    form_class = SapSanQuatationForm
    success_message = 'Success: SapSan Quatation was created.'
    success_url = reverse_lazy('add_services') """


def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request,'registration/sign_in.html', data)














