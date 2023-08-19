from django.contrib import admin
from django.urls import path
from account import views
from django.contrib.auth.views import LoginView,LogoutView

app_name = "account"

urlpatterns = [
    path('truck_ticket_order/',views.truck_ticket_order,name='truck_ticket_order'),
    path('profile/',views.profile,name="profile"),
    ]