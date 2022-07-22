from rest_framework import serializers
from .models import Driver_Detail

# from Logistics.Driver.views import driver_details
class Driver_DetailSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=50)
    phone_number = serializers.IntegerField()
    address = serializers.CharField(max_length=300)
    vehicle_registration_number = serializers.CharField(max_length=100)
    driving_licence_number = serializers.CharField(max_length=100)
    # registration_card_photo = serializers.ImageField()
    # driving_licence_photo = serializers.ImageField()
    # vehicle_registration_number = serializers.ImageField(upload_to='images/')
    # driving_licence_number = serializers.ImageField(upload_to='images/')


    def create(self, validate_data):
        return Driver_Detail.objects.create(**validate_data)