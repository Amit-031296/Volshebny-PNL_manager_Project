from django.contrib import admin
from django.urls import path,re_path
from django.urls import reverse_lazy
from payment import views

app_name = 'payment'

urlpatterns = [
# --- Pages Urls ---
# ------ Authentication URLs -----
# Login
path("" , views.user_login, name="index"),

path("user_login" , views.user_login, name="user_login"),

path("user_sign_up" , views.user_sign_up, name="user_sign_up"),

path("forgetpassword" , views.forgetpassword, name="forgetpassword"),

# Forget Password
path("forgetpassword" , views.forgetpassword, name="forgetpassword"),

# Logout
path('logout/', views.user_sign_out, name='logout'),

# url for report error page
path('report_error/', views.report_error, name ='report_error'),
path('report_error_submit/', views.report_error_submit, name ='report_error_submit'),
path('report_error_success/', views.report_error_success, name ='report_error_success'),

# </------ Authentication URLs -----

# ------ Sidemenu Urls ------
# Tour Details Form
path('group_description_form/', views.group_description_form, name = 'group_description_form'),

#Tour List Page URLs
# Tour List - Self
path('pnllist/', views.pnllist, name='pnllist'),
# Services - Add Services
path('add_services/<int:pk>',views.add_services, name='add_services'),
# Tour Summary Page
path('tour_summary/<int:pk>',views.tour_summary, name='tour_summary'),

# Client List
path('clientlist/', views.client_list, name='clientlist'),

# Vendors List
path('vendorlist/', views.vendor_list, name='vendorlist'),

# experiment
path('experiment/', views.experiment, name='experiment'),

# --All vendor accounts dropdown Urls --
# -- AirTickets Account Url---
path('vendor_accounts_airticket_quatation/', views.vendor_accounts_airticket_quatation, name='vendor_accounts_airticket_quatation'),

# -- Visacost Account Url---
path('vendor_accounts_visacost_quatation/', views.vendor_accounts_visacost_quatation, name='vendor_accounts_visacost_quatation'),

# -- Hotel Account Url---
path('vendor_accounts_hotel_quatation/', views.vendor_accounts_hotel_quatation, name='vendor_accounts_hotel_quatation'),

# -- Restuarant Account Url---
path('vendor_accounts_restaurant_quatation/', views.vendor_accounts_restaurant_quatation, name='vendor_accounts_restaurant_quatation'),

# -- Entrances Account Url---
path('vendor_accounts_entrances_quatation/', views.vendor_accounts_entrances_quatation, name='vendor_accounts_entrances_quatation'),

# -- SapSan Account Url---
path('vendor_accounts_sapsan_quatation/', views.vendor_accounts_sapsan_quatation, name='vendor_accounts_sapsan_quatation'),

# -- Guide Account Url---
path('vendor_accounts_guide/', views.vendor_accounts_guide, name='vendor_accounts_guide'),

# -- Transport Account Url---
path('vendor_accounts_transport/', views.vendor_accounts_transport, name='vendor_accounts_transport'),

# </------ Sidemenu Urls ------

# ------- Portal Users URls ---------
#< -----Users list Urls ------>
path('users/', views.user_list, name='userlist'),
#</-----Users list Urls------>


#< -----Add Users Urls ------>
path('add_users/',views.Add_UsersView.as_view(),name='add_users'),
#</-----Add Users Urls ------>

#< -----Delete Users Urls ------>
path('userdelete/<int:pk>',views.UserDeleteView.as_view(),name='userdelete'),
#</-----Delete Users Urls ------>

#< -----Update Users Urls ------>
path('userupdate/<int:pk>',views.UserUpdateView.as_view(),name='userupdate'),
#</-----Update Users Urls ------>
# </------- Portal Users URls ---------

# ----------Support Urls -------

# Report Error
#path('reporterror/', views.reporterror, name='reporterror'),

# </----------Support Urls -------

#------ All Form Submit Processing URL -----------

#----group_description_form_submit URLS ----
path('group_description_form_submit/', views.group_description_form_submit, name='group_description_form_submit'),

# -- AirTicketsQuatation form_submit Url---
path('add_service_airticket_form_submit/<int:service_id>', views.add_service_airticket_form_submit, name='add_service_airticket_form_submit'),

# -- VisaCostQuatation form_submit Url ---
path('add_service_visacost_form_submit/<int:service_id>', views.add_service_visacost_form_submit, name='add_service_visacost_form_submit'),

# -- HotelQuatation form_submit Url---
path('add_service_hotelquatation_form_submit/<int:service_id>', views.add_service_hotelquatation_form_submit, name='add_service_hotelquatation_form_submit'),

# -- RestaurantQuatation form_submit Url---
path('add_service_restaurantquatation_form_submit/<int:service_id>', views.add_service_restaurantquatation_form_submit, name='add_service_restaurantquatation_form_submit'),

# -- EntrancesQuatation form_submit Url---
path('add_service_entrancesquatation_form_submit/<int:service_id>', views.add_service_entrancesquatation_form_submit, name='add_service_entrancesquatation_form_submit'),

# -- SapSanQuatation form_submit Url---
path('add_service_sapsanquatation_form_submit/<int:service_id>', views.add_service_sapsanquatation_form_submit, name='add_service_sapsanquatation_form_submit'),

# -- Guide form_submit Url----
path('add_service_guide_form_submit/<int:service_id>', views.add_service_guide_form_submit, name='add_service_guide_form_submit'),

# -- Transport form_submit Url----
path('add_service_transport_form_submit/<int:service_id>', views.add_service_transport_form_submit, name='add_service_transport_form_submit'),

#</------ All Form Submit Processing URL ----------- 












# ------ Django Bootstrap Modal Urls ------

# --- Tours List CURD URLs ---
# Group - Update
path('update/<int:pk>',views.PNLstatementUpdateView.as_view(), name='group_update'),

# Group - Delete
path('delete/<int:pk>',views.PNLstatementDeleteView.as_view(), name='group_delete'),

# Group - Summary
path('summary/<int:pk>',views.PNLStatementSummary.as_view(), name='group_summary'),
# </--- Tours List CURD URLs ---

# -- clientpnlstatementupdateview URL --
path('clientpnlstatementupdate/<int:pk>', views.clientpnlstatementupdateview.as_view(), name='client_pnlstatement_update'),

# -- clientpnlstatementdeleteview URL --
 path('clientpnlstatementdelete/<int:pk>', views.clientpnlstatementdeleteview.as_view(), name='client_pnlstatement_delete'),

# --- Clients CURD URLs ---
# Client - Update
path('client_update/<int:pk>',views.ClientUpdateView.as_view(), name='client_update'),

# Client - Delete
path('client_delete/<int:pk>',views.ClientDeleteView.as_view(), name='client_delete'),

# Client - Summary
path('client_summary/<int:pk>',views.ClientSummary.as_view(), name='client_summary'),

# Client - Add a new client
path('add/', views.add_new_client_view.as_view(), name='add_new_client'),

# --- Client Payment Details List ---
re_path(r'^client/details/(?P<client_id>[\w\-\s\(\)]+)/(?P<payment_status>\w+)/$',views.client_payment_details_list,name='client_payment_list'),
# </--- Clients CURD URLs ---

# --- Vendors CURD URLs ---
# Vendor - Update
path('vendor_update/<int:pk>',views.VendorUpdateView.as_view(), name='vendor_update'),

# Vendor - Delete
path('vendor_delete/<int:pk>',views.VendorDeleteView.as_view(), name='vendor_delete'),

# Vendor - Summary
path('vendor_summary/<int:pk>',views.VendorSummary.as_view(), name='vendor_summary'),

# Vendor - Add a new vendor
path('add_new_vendor/', views.add_new_vendor_view.as_view(), name='add_new_vendor'),

# --- Vendor Payment Details List ---
re_path(r'^vendor/details/(?P<vendor_id>[\w\-\s\(\)]+)/(?P<payment_status>\w+)/$',views.vendor_payment_details_list,name='vendor_payment_list'),
# </--- Vendors CURD URLs ---

# -- vendorserviceupdateview URL --
path('vendorserviceupdate/<int:pk>', views.vendorserviceupdateview.as_view(), name='vendor_service_update'),

# -- vendorservicedeleteview URL --
 path('vendorservicedelete/<int:pk>', views.vendorservicedeleteview.as_view(), name='vendor_service_delete'),


# --- Addservices CURD URLs ---
# AddServiceAirTicket - Update
path('addservices_airticket_update/<int:pk>',views.AddServiceAirTicketUpdateView.as_view(), name='addservices_airticket_update'),

# AddServiceAirTicket - Delete
path('addservices_airticket_delete/<int:pk>',views.AddServiceAirTicketDeleteView.as_view(), name='addservices_airticket_delete'),

# AddServiceVisacost - Update
path('addservices_visacost_update/<int:pk>',views.AddServiceVisaCostUpdateView.as_view(), name='addservices_visacost_update'),

# AddServiceVisacost - Delete
path('addservices_visacost_delete/<int:pk>',views.AddServiceVisaCostDeleteView.as_view(), name='addservices_visacost_delete'),

# AddServiceHotel - Update
path('addservices_hotel_update/<int:pk>',views.AddServiceHotelUpdateView.as_view(), name='addservices_hotel_update'),

# AddServiceHotel - Delete
path('addservices_hotel_delete/<int:pk>',views.AddServiceHotelDeleteView.as_view(), name='addservices_hotel_delete'),

# AddServiceRestaurant - Update
path('addservices_restaurant_update/<int:pk>',views.AddServiceRestaurantUpdateView.as_view(), name='addservices_restaurant_update'),

# AddServiceRestaurant - Delete
path('addservices_restaurant_delete/<int:pk>',views.AddServiceRestaurantDeleteView.as_view(), name='addservices_restaurant_delete'),

# AddServiceEntrances - Update
path('addservices_entrances_update/<int:pk>',views.AddServiceEntrancesUpdateView.as_view(), name='addservices_entrances_update'),

# AddServiceEntrances - Delete
path('addservices_entrances_delete/<int:pk>',views.AddServiceEntrancesDeleteView.as_view(), name='addservices_entrances_delete'),

# AddServiceSapsan - Update
path('addservices_sapsan_update/<int:pk>',views.AddServiceSapSanUpdateView.as_view(), name='addservices_sapsan_update'),

# AddServiceSapsan - Delete
path('addservices_sapsan_delete/<int:pk>',views.AddServiceSapSanDeleteView.as_view(), name='addservices_sapsan_delete'),

# AddServiceGuide - Update
path('addservices_guide_update/<int:pk>',views.AddServiceGuideUpdateView.as_view(), name='addservices_guide_update'),

# AddServiceGuide - Delete
path('addservices_guide_delete/<int:pk>',views.AddServiceGuideDeleteView.as_view(), name='addservices_guide_delete'),

# AddServiceTransport - Update
path('addservices_transport_update/<int:pk>',views.AddServiceTransportUpdateView.as_view(), name='addservices_transport_update'),

# AddServiceTransport - Delete
path('addservices_transport_delete/<int:pk>',views.AddServiceTransportDeleteView.as_view(), name='addservices_transport_delete'),
# </--- Addservices CURD URLs ---


# --- vendor_accounts_airticket_quatation CURD URLs ---

# Airticket - Update
path('vendor_airticket_update/<int:pk>', views.VendorAirticketUpdateView.as_view(), name='vendor_airticket_update'),

# Airticket - Delete
path('vendor_airticket_delete/<int:pk>',views.VendorAirticketDeleteView.as_view(),name='vendor_airticket_delete'),

# Airticket - Add a new Airticket
path('add/airticket', views.add_new_airticket_view.as_view(), name='add_new_airticket'),

# Airticket detail - Update
path('vendor_airticket_detail_update/<int:pk>', views.VendorAirticketDetailUpdateView.as_view(), name='vendor_airticket_detail_update'),

# Airticket detail - Delete
path('vendor_airticket_detail_delete/<int:pk>',views.VendorAirticketDetailDeleteView.as_view(),name='vendor_airticket_detail_delete'),

# --- vendor_accounts_airticket_quatation_details Url ---
re_path(r'^vendor/details/airticket/(?P<vendor_id>[\w\-\s\(\)]+)/(?P<payment_status>\w+)/$',views.vendor_accounts_airticket_quatation_details,name='vendor_accounts_airticket_quatation_details'),


# </--- vendor_accounts_airticket_quatation CURD URLs ---

# --- vendor_accounts_visacost_quatation CURD URLs ---
# VisaCost - Update
path('vendor_visacost_update/<int:pk>',views.VendorVisaCostUpdateView.as_view(),name='vendor_visacost_update'),

# VisaCost - Delete
path('vendor_visacost_delete/<int:pk>',views.VendorVisaCostDeleteView.as_view(),name='vendor_visacost_delete'),

# VisaCost - Add a new VisaCost
path('add/visacost', views.add_new_visacost_view.as_view(), name='add_new_visacost'),

# VisaCost - Update
path('vendor_visacost_detail_update/<int:pk>',views.VendorVisaCostDetailUpdateView.as_view(),name='vendor_visacost_detail_update'),

# VisaCost - Delete
path('vendor_visacost_detail_delete/<int:pk>',views.VendorVisaCostDetailDeleteView.as_view(),name='vendor_visacost_detail_delete'),

# --- vendor_accounts_visacost_quatation_details Url ---
re_path(r'^vendor/details/visacost/(?P<vendor_id>[\w\-\s\(\)]+)/(?P<payment_status>\w+)/$',views.vendor_accounts_visacost_quatation_details,name='vendor_accounts_visacost_quatation_details'),
# </--- vendor_accounts_visacost_quatation CURD URLs ---

# --- vendor_accounts_hotel_quatation  CURD URLs ---
# Hotel - Update
path('vendor_hotel_update/<int:pk>',views.VendorHotelUpdateView.as_view(), name='vendor_hotel_update'),

# Hotel - Delete
path('vendor_hotel_delete/<int:pk>',views.VendorHotelDeleteView.as_view(), name='vendor_hotel_delete'),

# HotelQuatation - Add a new HotelQuatation
path('add/hotel', views.add_new_hotel_view.as_view(), name='add_new_hotel'),

# Hotel - Update
path('vendor_hotel_detail_update/<int:pk>',views.VendorHotelDetailUpdateView.as_view(), name='vendor_hotel_detail_update'),

# Hotel - Delete
path('vendor_hotel_detail_delete/<int:pk>',views.VendorHotelDetailDeleteView.as_view(), name='vendor_hotel_detail_delete'),

# --- vendor_accounts_hotel_quatation_details Url ---
re_path(r'^vendor/details/hotel/(?P<vendor_id>[\w\-\s\(\)]+)/(?P<payment_status>\w+)/$',views.vendor_accounts_hotel_quatation_details,name='vendor_accounts_hotel_quatation_details'),
# </--- vendor_accounts_hotel_quatation  CURD URLs ---

# --- vendor_accounts_restaurant_quatation  CURD URLs ---
# Restaurant - Update
path('vendor_restaurant_update/<int:pk>',views.VendorRestaurantUpdateView.as_view(), name='vendor_restaurant_update'),

# Restaurant - Delete
path('vendor_restaurant_delete/<int:pk>',views.VendorRestaurantDeleteView.as_view(), name='vendor_restaurant_delete'),

# RestaurantQuatation - Add a new RestaurantQuatation
path('add/restaurant', views.add_new_restaurant_view.as_view(), name='add_new_restaurant'),

# Restaurant - Update
path('vendor_restaurant_detail_update/<int:pk>',views.VendorRestaurantDetailUpdateView.as_view(), name='vendor_restaurant_detail_update'),

# Restaurant - Delete
path('vendor_restaurant_detail_delete/<int:pk>',views.VendorRestaurantDetailDeleteView.as_view(), name='vendor_restaurant_detail_delete'),

# --- vendor_accounts_restaurant_quatation_details Url ---
re_path(r'^vendor/details/restaurant/(?P<vendor_id>[\w\-\s\(\)]+)/(?P<payment_status>\w+)/$',views.vendor_accounts_restaurant_quatation_details,name='vendor_accounts_restaurant_quatation_details'),
# </--- vendor_accounts_restaurant_quatation  CURD URLs ---

# --- vendor_accounts_entrances_quatation  CURD URLs ---
# Entrances - Update
path('vendor_entrances_update/<int:pk>',views.VendorEntrancesUpdateView.as_view(), name='vendor_entrances_update'),

# Entrances - Delete
path('vendor_entrances_delete/<int:pk>',views.VendorEntrancesDeleteView.as_view(), name='vendor_entrances_delete'),

# EntrancesQuatation - Add a new EntrancesQuatation
path('add/entrances', views.add_new_entrances_view.as_view(), name='add_new_entrances'),

# Entrances - Update
path('vendor_entrances_detail_update/<int:pk>',views.VendorEntrancesDetailUpdateView.as_view(), name='vendor_entrances_detail_update'),

# Entrances - Delete
path('vendor_entrances_detail_delete/<int:pk>',views.VendorEntrancesDetailDeleteView.as_view(), name='vendor_entrances_detail_delete'),

# --- vendor_accounts_entrances_quatation_details Url ---
re_path(r'^vendor/details/entrances/(?P<vendor_id>[\w\-\s\(\)]+)/(?P<payment_status>\w+)/$',views.vendor_accounts_entrances_quatation_details,name='vendor_accounts_entrances_quatation_details'),

# </--- vendor_accounts_entrances_quatation  CURD URLs ---

# --- vendor_accounts_sapsan_quatation  CURD URLs ---
# Sapsan - Update
path('vendor_sapsan_update/<int:pk>',views.VendorSapSanUpdateView.as_view(), name='vendor_sapsan_update'),

# Sapsan - Delete
path('vendor_sapsan_delete/<int:pk>',views.VendorSapSanDeleteView.as_view(), name='vendor_sapsan_delete'),

# SapSanQuatation - Add a new SapSanQuatation
path('add/sapsan', views.add_new_sapsan_view.as_view(), name='add_new_sapsan'),

# Sapsan - Update
path('vendor_sapsan_detail_update/<int:pk>',views.VendorSapSanDetailUpdateView.as_view(), name='vendor_sapsan_detail_update'),

# Sapsan - Delete
path('vendor_sapsan_detail_delete/<int:pk>',views.VendorSapSanDetailDeleteView.as_view(), name='vendor_sapsan_detail_delete'),

# --- vendor_accounts_sapsan_quatation_details Url ---
re_path(r'^vendor/details/sapsan/(?P<vendor_id>[\w\-\s\(\)]+)/(?P<payment_status>\w+)/$',views.vendor_accounts_sapsan_quatation_details,name='vendor_accounts_sapsan_quatation_details'),

# </--- vendor_accounts_sapsan_quatation  CURD URLs ---

# --- vendor_accounts_guide  CURD URLs ---
# Guide - Update
path('vendor_guide_update/<int:pk>',views.VendorGuideUpdateView.as_view(), name='vendor_guide_update'),

# Guide - Delete
path('vendor_guide_delete/<int:pk>',views.VendorGuideDeleteView.as_view(), name='vendor_guide_delete'),

# Guide - Add a new Guide
path('add/guide', views.add_new_guide_view.as_view(), name='add_new_guide'),

# Guidedetail - Update
path('vendor_guide_detail_update/<int:pk>',views.VendorGuideDetailUpdateView.as_view(), name='vendor_guide_detail_update'),

# Guidedetail - Delete
path('vendor_guide_detail_delete/<int:pk>',views.VendorGuideDetailDeleteView.as_view(), name='vendor_guide_detail_delete'),

# --- vendor_accounts_guide_details Url ---
re_path(r'^vendor/details/guide/(?P<vendor_id>[\w\-\s\(\)]+)/(?P<payment_status>\w+)/$',views.vendor_accounts_guide_details,name='vendor_accounts_guide_details'),

# </--- vendor_accounts_guide  CURD URLs ---

# --- vendor_accounts_transport  CURD URLs ---
# Transport - Update
path('vendor_transport_update/<int:pk>',views.VendorTransportUpdateView.as_view(), name='vendor_transport_update'),

# Transport - Delete
path('vendor_transport_delete/<int:pk>',views.VendorTransportDeleteView.as_view(), name='vendor_transport_delete'),

# Transport - Add a new Guide
path('add/transport', views.add_new_transport_view.as_view(), name='add_new_transport'),

# Transportdetail - Update
path('vendor_transport_detail_update/<int:pk>',views.VendorTransportDetailUpdateView.as_view(), name='vendor_transport_detail_update'),

# Transportdetail - Delete
path('vendor_transport_detail_delete/<int:pk>',views.VendorTransportDetailDeleteView.as_view(), name='vendor_transport_detail_delete'),

# --- vendor_accounts_transport_details Url ---
re_path(r'^vendor/details/transport/(?P<vendor_id>[\w\-\s\(\)]+)/(?P<payment_status>\w+)/$',views.vendor_accounts_transport_details,name='vendor_accounts_transport_details'),

# </--- vendor_accounts_transport  CURD URLs ---

# --- Services URLs ---
#path('add_services/',views.add_services, name='add_services'),

# -- AirTicketsQuatation Url---
#path('createairticketquatation/',views.AirTicketCreateView.as_view(), name='createairticketquatation'),

# -- VisaCostQuatation Url ---
#path('createvisacostquatation/',views.VisaCostCreateView.as_view(), name='createvisacostquatation')",

# -- HotelQuatation Url---
#path('createhotelquatation/',views.HotelQuatationCreateView.as_view(), name='createhotelquatation')",

# -- RestaurantQuatation Url---
#path('createrestaurantquatation/',views.RestaurantQuatationCreateView.as_view(), name='createrestaurantquatation'),

# -- EntrancesQuatation Url---
#path('createentrancesquatation/',views.EntrancesQuatationCreateView.as_view(), name='createentrancesquatation'),

# -- SapSanQuatation Url---
#path('createsapsanquatation/',views.SapSanQuatationCreateView.as_view(), name='createsapsanquatation'),

]