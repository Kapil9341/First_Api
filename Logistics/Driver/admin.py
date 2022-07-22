from django.contrib import admin

from .models import Driver_Detail
# Register your models here.

@admin.register(Driver_Detail)
class Driver_DetailAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','email','phone_number','address']