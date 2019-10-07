#<---------Django Imported Libraries--------->
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import datetime
#</---------Django Imported Libraries--------->

#<---------External Libraries--------->
from model_utils.managers import InheritanceManager
#</---------Django Imported Libraries--------->


#---------Application Models---------

#<---------Custom User Model --------->
class CustomUser(AbstractUser):
    '''Overrides the custom django user model'''
    # Datafields
    SUPER_ADMIN = 1
    ADMIN = 2
    ROLE_CHOICES = (
      (ADMIN,'admin'),
      (SUPER_ADMIN,'super_admin')
    )
    OFFICE_LOCATION_CHOICES = (
      ('MUMBAI','MUMBAI'),
      ('DELHI','DELHI'),
      ('RUSSIA','RUSSIA'),
    )
    user_role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES,default=ADMIN,blank=True)
    office_location = models.CharField( max_length=920, choices=OFFICE_LOCATION_CHOICES, default = 'MUMBAI')
    user_short_name = models.CharField( max_length=920 )

#</---------Custom User Model --------->

#<---------Vendor Model --------->
class Vendor(models.Model):

    vendor_type_choices=(('Air Ticket Service','Air Ticket Service'),
                        ('Visa Cost Service','Visa Cost Service'),
                        ('Hotel Quatation Service','Hotel Quatation Service'),
                        ('Restuarant Quatation Service','Restuarant Quatation Service'),
                        ('Entrances Quatation Service','Entrances Quatation Service'),
                        ('SapSan Quatation Service','SapSan Quatation Service'),
                        ('Guide Service','Guide Service'),
                        ('Transport Service','Transport Service'))
    vendor_name = models.CharField(max_length=920)
    vendor_address = models.CharField(max_length=920)
    vendor_type = models.CharField(choices=vendor_type_choices,max_length=920,default="Air Ticket Service")
    vendor_mobile = models.CharField(max_length=920,default="")
    vendor_email = models.CharField(max_length=920,default="")
    vendor_remark = models.CharField(max_length=920,default="")

    def __str__(self):
        return str(self.pk)
#</---------Vendor Model --------->


#<---------Client Model --------->
class Client(models.Model):

    client_name = models.CharField(max_length=920)
    client_address = models.CharField(max_length=920)
    client_email = models.CharField(max_length=920,default="")
    client_telephone = models.CharField(max_length=920,default="")

    def __str__(self):
        return str(self.client_name)
#</---------Client Model --------->


#<--------- Group Description Model --------->
class Groupdescription(models.Model):
    PAYMENT_STATUS=(('Paid','Paid'), ('Pending','Pending'))
    groupdescription_vtrefNo = models.CharField(max_length=920)
    groupdescription_vtrefNo_short = models.IntegerField()
    groupdescription_client_Name = models.CharField(max_length=920)
    groupdescription_number_of_passengers_paid= models.IntegerField()
    groupdescription_number_of_passengers_free = models.IntegerField()
    groupdescription_number_of_days = models.IntegerField()
    groupdescription_volshebny_handle_person = models.CharField(max_length=920)
    groupdescription_client_handle_person = models.CharField(max_length=920)
    groupdescription_booking_date = models.DateField()
    groupdescription_confirmation_date = models.DateField()
    groupdescription_amount = models.IntegerField(default=0)
    groupdescription_start_date = models.DateTimeField(default=timezone.now)
    groupdescription_end_date = models.DateTimeField(default=timezone.now)
    groupdescription_destination = models.CharField(max_length=920,default="")
    groupdescription_payment_method = models.CharField(max_length=920)
    groupdescription_payment_status = models.CharField(choices=PAYMENT_STATUS,max_length=920,default="Pending")
    groupdescription_client_id = models.ForeignKey(Client, on_delete = models.CASCADE)
    groupdescription_date_time_added = models.DateTimeField(default=timezone.now)
    groupdescription_roe = models.FloatField(default=0)
    groupdescription_remark = models.CharField(max_length=920,default="")

    def __str__(self):
            return str(self.pk)

    class Meta:
            verbose_name_plural = "Group Description Elements"
            verbose_name = "GroupDescription"
#</--------- Group Description Model --------->


#<---------Service Model --------->
class Service(models.Model):
        payment_status=(('Pending','Pending'),('Done','Done'))
        service_vendor_id = models.ForeignKey(Vendor, on_delete = models.CASCADE,default="2")
        service_number_of_passengers =  models.CharField(max_length=920,blank=True)
        service_quote_per_head = models.FloatField(blank=True)
        service_roe = models.FloatField(blank=True)
        service_gst = models.FloatField(blank=True)
        service_total_amount =  models.FloatField(default=0.0,blank=True)
        service_payment_method = models.CharField(max_length=920,default="")
        service_vendor_payment_status = models.CharField(choices=payment_status,max_length=920,default="Pending")
        objects = InheritanceManager()
        service_id = models.ForeignKey(Groupdescription, on_delete = models.CASCADE,default="11")

        def __str__(self):
                return str(self.pk)
#</---------Service Model --------->

#<--------- Air Ticket Service Model --------->
class AirTicketsQuatation(Service):
        #DataFields
        service_type = models.CharField(max_length=920,default="Air Ticket Service")
        airticket_airline_name = models.CharField(max_length=920)
        airticket_date_and_time_of_depature = models.DateTimeField()
        airticket_date_and_time_of_arrival = models.DateTimeField()
        airticket_departure_from = models.CharField(max_length=920,default="")
        airticket_arrival_at = models.CharField(max_length=920,default="")
        airticket_booked_from = models.CharField(max_length=920,blank=True)

        def __str__(self):
                return str(self.pk)

        class Meta:
                verbose_name_plural = "Air Ticket Quotation"
                verbose_name = "Air Ticket"
#</--------- Air Ticket Service Model --------->

#<--------- Visa Cost Service Model --------->
class VisaCostQuatation(Service):
        service_type = models.CharField(max_length=920,default="Visa Cost Service")
        TYPE_OF_VISA=(('Tourist single','Tourist single'),
                       ('Tourist Double','Tourist Double'),
                       ('Business','Business'))
        TIME_PERIOD=(('Normal','Normal'),
                      ('Urgent','Urgent'))
        visacost_date_and_time_of_generation = models.DateTimeField(default=timezone.now)
        visacost_type_of_Visa = models.CharField(choices=TYPE_OF_VISA,max_length=920,default="Tourist single")
        visacost_time_period = models.CharField(choices=TIME_PERIOD,max_length=920,default="Normal")

        def __str__(self):
                return str(self.pk )

        class Meta:
                verbose_name_plural = "Visa Cost Quatation"
                verbose_name = "Visa Cost"
#</--------- Visa Cost Service Model --------->

#<--------- Hotel Service Model --------->
class HotelQuatation(Service):
        service_type = models.CharField(max_length=920,default="Hotel Quatation Service")
        TYPE_OF_ROOM=(('Single Occupancy','Single Occupancy'),
                       ('Double Occupancy','Double Occupancy'),
                        ('Triple Occupancy','Triple Occupancy'))
        BREAKFAST_PROVIDES=(('Yes','Yes'),
                              ('No','No'))
        hotelquatation_hotel_name = models.CharField(max_length=920)
        hotelquatation_number_of_rooms = models.IntegerField()
        hotelquatation_type_of_room = models.CharField(choices=TYPE_OF_ROOM,max_length=920,default="Single Occupancy")
        hotelquatation_breakfast_provided = models.CharField(choices=BREAKFAST_PROVIDES,max_length=920,default="Yes")
        hotelquatation_check_in_datetime = models.DateTimeField(default=timezone.now)
        hotelquatation_check_out_datetime = models.DateTimeField(default=timezone.now)

        def __str__(self):
                return str(self.pk )

        class Meta:
                verbose_name_plural = "Hotel Quatation"
                verbose_name = "Hotel"
#</--------- Hotel Service Model --------->

#<--------- Restaurant Service Model --------->
class RestaurantQuatation(Service):
        service_type = models.CharField(max_length=920,default="Restuarant Quatation Service")
        RESTAURANT_FOR=(('Lunch','Lunch'),
                        ('Dinner','Dinner'))
        restaurantquatation_resturant_name= models.CharField(max_length=920)
        restaurantquatation_For = models.CharField(choices=RESTAURANT_FOR,max_length=920,default="Lunch")
        restaurantquatation_date = models.DateTimeField(default=timezone.now)

        def __str__(self):
                return str(self.pk )

        class Meta:
                verbose_name_plural = " Resturant Quatation"
                verbose_name = "Resturant"
#</--------- Restaurant Service Model --------->

#<--------- Entrances Service Model --------->
class EntrancesQuatation(Service):
        service_type = models.CharField(max_length=920,default="Entrances Quatation Service")
        entrancesquatation_name = models.CharField(max_length=920)
        entrancesquatation_date = models.DateTimeField(default=timezone.now)

        def __str__(self):
                return str(self.pk )

        class Meta:
                verbose_name_plural = "Entrances Quatation"
                verbose_name = "Entrances"
#</--------- Entrances Service Model --------->

#<--------- SapSan Service Model --------->
class SapSanQuatation(Service):
        service_type = models.CharField(max_length=920,default="SapSan Quatation Service")
        sapsanquatation_From_Station= models.CharField(max_length=920)
        sapsanquatation_To_Station = models.CharField(max_length=920)
        sapsanquatation_date = models.DateTimeField(default=timezone.now)

        def __str__(self):
                return str(self.pk )

        class Meta:
                verbose_name_plural = "SapSan Quatation"
                verbose_name = "SapSan"
#</--------- SapSan Service Model --------->

#<--------- Guide Service Model --------->
class Guide(Service):
        service_type = models.CharField(max_length=920,default="Guide Service")
        Guide_Name = models.CharField(max_length=920)
        Guide_Destination = models.CharField(max_length=920)
        guide_date = models.DateTimeField(default=timezone.now)

        def __str__(self):
                return str(self.pk)

        class Meta:
                verbose_name_plural = "Guide"
                verbose_name = "Guide"
#</--------- Guide Service Model --------->


#<------------Transport Service Model --------->
class Transport(Service):
        service_type = models.CharField(max_length=920,default="Transport Service")
        transport_type_of_vehicle = models.CharField(max_length=920,default="")
        transport_date = models.DateTimeField(default=timezone.now)

        def __str__(self):
                return str(self.pk)

        class Meta:
                verbose_name_plural = "Transport"
                verbose_name = "Transport"


#</------------Transport Service Model --------->
