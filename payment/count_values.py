from payment import functions
from payment.models import Groupdescription, AirTicketsQuatation, VisaCostQuatation, HotelQuatation, RestaurantQuatation, EntrancesQuatation, SapSanQuatation, Client, Vendor

groupdescription_objects = Groupdescription.objects.all()
clients = Client.objects.all()
client_payment_status = ['Paid','Pending']
x = list(set(list(Client.objects.values_list('pk','client_name'))))
client_status_list = [functions.client_status_count(a,client_payment_status_one) for a in x for client_payment_status_one in client_payment_status ]
final = [client_status_list[i * 2:(i + 1) * 2] for i in range((len(client_status_list) + 2 - 1) // 2 )]
client_dict = dict(zip(x,final))

airticketobjects = AirTicketsQuatation.objects.all()
vendors = Vendor.objects.all()
vendor_payment_status = ['Pending','Done']
x = list(set(list(Vendor.objects.values_list('pk','vendor_name'))))
vendor_status_list = [functions.vendor_airticket_status_count(a,vendor_payment_status_one) for a in x for vendor_payment_status_one in vendor_payment_status ]
final = [vendor_status_list[i * 2:(i + 1) * 2] for i in range((len(vendor_status_list) + 2 - 1) // 2 )]
airticket_dict = dict(zip(x,final))

visacosttobjects = VisaCostQuatation.objects.all()
vendors = Vendor.objects.all()
vendor_payment_status = ['Pending','Done']
x = list(set(list(Vendor.objects.values_list('pk','vendor_name'))))
vendor_status_list = [functions.vendor_visacost_status_count(a,vendor_payment_status_one) for a in x for vendor_payment_status_one in vendor_payment_status ]
final = [vendor_status_list[i * 2:(i + 1) * 2] for i in range((len(vendor_status_list) + 2 - 1) // 2 )]
visacost_dict = dict(zip(x,final))

hotelquatationobjects = HotelQuatation.objects.all()
vendors = Vendor.objects.all()
vendor_payment_status = ['Pending','Done']
x = list(set(list(Vendor.objects.values_list('pk','vendor_name'))))
vendor_status_list = [functions.vendor_hotel_status_count(a,vendor_payment_status_one) for a in x for vendor_payment_status_one in vendor_payment_status ]
final = [vendor_status_list[i * 2:(i + 1) * 2] for i in range((len(vendor_status_list) + 2 - 1) // 2 )]
hotel_dict = dict(zip(x,final))

restaurantquatationobjects = RestaurantQuatation.objects.all()
vendors = Vendor.objects.all()
vendor_payment_status = ['Pending','Done']
x = list(set(list(Vendor.objects.values_list('pk','vendor_name'))))
vendor_status_list = [functions.vendor_restaurant_status_count(a,vendor_payment_status_one) for a in x for vendor_payment_status_one in vendor_payment_status ]
final = [vendor_status_list[i * 2:(i + 1) * 2] for i in range((len(vendor_status_list) + 2 - 1) // 2 )]
restaurant_dict = dict(zip(x,final))

entrancesquatationobjects = EntrancesQuatation.objects.all()
vendors = Vendor.objects.all()
vendor_payment_status = ['Pending','Done']
x = list(set(list(Vendor.objects.values_list('pk','vendor_name'))))
vendor_status_list = [functions.vendor_entrances_status_count(a,vendor_payment_status_one) for a in x for vendor_payment_status_one in vendor_payment_status ]
final = [vendor_status_list[i * 2:(i + 1) * 2] for i in range((len(vendor_status_list) + 2 - 1) // 2 )]
entrances_dict = dict(zip(x,final))

sapsanquatationobjects = SapSanQuatation.objects.all()
vendors = Vendor.objects.all()
vendor_payment_status = ['Pending','Done']
x = list(set(list(Vendor.objects.values_list('pk','vendor_name'))))
vendor_status_list = [functions.vendor_sapsan_status_count(a,vendor_payment_status_one) for a in x for vendor_payment_status_one in vendor_payment_status ]
final = [vendor_status_list[i * 2:(i + 1) * 2] for i in range((len(vendor_status_list) + 2 - 1) // 2 )]
sapsan_dict = dict(zip(x,final))

""" air_tickets = AirTicketsQuatation.objects.filter(service_id=pk)
service_list = []
for air_ticket in air_tickets:
        if(air_tickets):
            service_list.append(air_ticket.service_vendor_id)
            service_list.append(air_ticket.service_total_amount)

x = list(set(list(AirTicketsQuatation.objects.values_list('pk','service_id'))))
airticket_dict = dict(zip(x,service_list)) """


""" total = [ count_functions.Total_Count_LeadStatus(x) for x in lead_Status_list ]
week = [ count_functions.Weekly_Count_LeadStatus(x) for x in lead_Status_list ]
month = [ count_functions.Monthly_Count_LeadStatus(x) for x in lead_Status_list ]
mumbai = [ count_functions.City_Count(x,"Mumbai") for x in lead_Status_list ]
kochi = [ count_functions.City_Count(x,"Kochi") for x in lead_Status_list ]
pune = [ count_functions.City_Count(x,"Pune") for x in lead_Status_list ]
banglore = [ count_functions.City_Count(x,"Banglore") for x in lead_Status_list ]
hyderabad = [ count_functions.City_Count(x,"Hyderabad") for x in lead_Status_list ]
calcutta = [ count_functions.City_Count(x,"Calcutta") for x in lead_Status_list ]
mumbai_dict = dict(zip(lead_Status_list, mumbai))
kochi_dict = dict(zip(lead_Status_list, kochi))
pune_dict = dict(zip(lead_Status_list, pune))
banglore_dict = dict(zip(lead_Status_list, banglore))
calcutta_dict = dict(zip(lead_Status_list, calcutta))
hyderabad_dict = dict(zip(lead_Status_list, hyderabad))
total_dict = dict(zip(lead_Status_list, total))
week_dict = dict(zip(lead_Status_list, week))
month_dict = dict(zip(lead_Status_list, month))
total_city_collect = { 'mumbai_all' : count_functions.Total_City_Count('Mumbai'), 'kochi_all' : count_functions.Total_City_Count('Kochi'), 'pune_all' : count_functions.Total_City_Count('Pune'), 'hyderabad_all' : count_functions.Total_City_Count('Hyderabad'), 'banglore_all' : count_functions.Total_City_Count('Banglore'), 'calcutta_all' : count_functions.Total_City_Count('Calcutta')}
total_collect = { 'all': count_functions.Total_Count(), 'week': count_functions.Weekly_Count(), 'month': count_functions.Montly_Count(),}
routes = [ count_functions.Total_Routes_Count(a,lead_status) for a in x for lead_status in lead_Status_list ]
final = [routes[i * 4:(i + 1) * 4] for i in range((len(routes) + 4 - 1) // 4 )]
routes = [ count_functions.Total_Routes_Count(a,lead_status) for a in x for lead_status in lead_Status_list ]
final = [routes[i * 4:(i + 1) * 4] for i in range((len(routes) + 4 - 1) // 4 )]
routes_dict = dict(zip(x,final)) """