from rest_framework import serializers
from .models import Listing, Booking, Review, User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    Converts model instances to JSON and validates input data.
    """
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'role']
        read_only_fields = ['id']

class ListingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Listing model.
    Converts model instances to JSON and validates input data.
    """
    
    class Meta:
        model = Listing
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Booking model.
    Converts model instances to JSON and validates input data.
    """
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['created_at']


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for the Review model.
    Converts model instances to JSON and validates input data.
    """
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['created_at']