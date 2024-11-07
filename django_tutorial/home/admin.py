from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Departments, Doctors, Booking

# Customize the admin site header, title, and index title
class MyAdminSite(AdminSite):
    site_header = "City Hospital Admin"  # Header displayed at the top
    site_title = "City Hospital Admin Portal"  # Title in the browser tab
    index_title = "Welcome to City Hospital Admin Panel"  # Title on the main page

# Set the custom admin site
admin.site = MyAdminSite()

# Register your models with the custom admin site
admin.site.register(Departments)
admin.site.register(Doctors)

# Customize the Booking model admin
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'p_name', 'p_email', 'p_phone', 'doct_name', 'booking_date', 'booked_on')

# Register the Booking model with the custom admin site
admin.site.register(Booking, BookingAdmin)
