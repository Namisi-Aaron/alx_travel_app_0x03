import os
import sys
from pathlib import Path
import django
from datetime import datetime, timedelta

project_root = Path(__file__).resolve().parent.parent.parent.parent
sys.path.append(str(project_root))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_travel_app.settings')
django.setup()

from listings.serializers import (
    ListingSerializer, BookingSerializer,
    ReviewSerializer, UserSerializer
)

def seed_users():
    """
    Seeds the database with sample user data.
    """
    user_data = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "password": "password123",
            "role": "host"
        },
        {
            "first_name": "Jane",
            "last_name": "Smith",
            "email": "jane.smith@example.com",
            "password": "password123",
            "role": "guest"
        },
        {
            "first_name": "Adam",
            "last_name": "Johnson",
            "email": "adam.johnson@example.com",
            "password": "password123",
            "role": "guest"
        },
        {
            "first_name": "Eve",
            "last_name": "Williams",
            "email": "eve.williams@example.com",
            "password": "password123",
            "role": "host"
        },
        {
            "first_name": "Michael",
            "last_name": "Jones",
            "email": "michael.jones@example.com",
            "password": "password123",
            "role": "guest"
        }
    ]

    for user in user_data:
        user_serializer = UserSerializer(data=user)
        if user_serializer.is_valid():
            user_serializer.save()
            print("Created user:", user_serializer.data)
        else:
            print("Failed to create user:", user_serializer.errors)

def seed_listings():
    """
    Seeds the database with sample listing data.
    """
    listing_data = [
        {
            "name": "Beachfront Villa",
            "description": "A beautiful beachfront villa with stunning ocean views.",
            "location": "Diani Beach, Kenya",
            "price_per_night": 100.00,
            "host_id": 1
        },
        {
            "name": "Cottage at the Lake",
            "description": "A cozy cottage located by the lake.",
            "location": "Lakeview, USA",
            "price_per_night": 80.00,
            "host_id": 4
        },
        {
            "name": "Cabin in the Woods",
            "description": "A secluded cabin surrounded by nature.",
            "location": "Woodland, USA",
            "price_per_night": 120.00,
            "host_id": 1
        },
        {
            "name": "Mountain Village",
            "description": "A picturesque mountain village with beautiful views.",
            "location": "Mountain Land, Africa",
            "price_per_night": 150.00,
            "host_id": 4
        }
    ]

    for listing in listing_data:
        listing_serializer = ListingSerializer(data=listing)
        if listing_serializer.is_valid():
            listing_serializer.save()
            print("Created listing:", listing_serializer.data)
        else:
            print("Failed to create listing:", listing_serializer.errors)

def seed_bookings():
    """
    Seed the database with sample booking data.
    """
    booking_data = [
        {
            "listing_id": 1,
            "user_id": 2,
            "start_date": datetime(2023, 10, 1).date(),
            "end_date": (datetime(2023, 10, 1) + timedelta(days=3)).date(),
            "total_price": 300.00,
            "status": "confirmed"
        },
        {
            "listing_id": 2,
            "user_id": 3,
            "start_date": datetime(2023, 9, 15).date(),
            "end_date": (datetime(2023, 9, 15) + timedelta(days=5)).date(),
            "total_price": 400.00,
            "status": "pending"
        },
        {
            "listing_id": 3,
            "user_id": 5,
            "start_date": datetime(2023, 10, 1).date(),
            "end_date": (datetime(2023, 10, 1) + timedelta(days=2)).date(),
            "total_price": 240.00,
            "status": "confirmed"
        },
        {
            "listing_id": 4,
            "user_id": 2,
            "start_date": datetime(2023, 10, 1).date(),
            "end_date": (datetime(2023, 10, 1) + timedelta(days=4)).date(),
            "total_price": 600.00,
            "status": "pending"
        }
    ]
    for booking in booking_data:
        booking_serializer = BookingSerializer(data=booking)
        if booking_serializer.is_valid():
            booking_serializer.save()
            print("Created booking:", booking_serializer.data)
        else:
            print("Failed to create booking:", booking_serializer.errors)

def seed_reviews():
    """
    Seed the database with sample review data.
    """
    review_data = [
        {
            "listing_id": 1,
            "user_id": 2,
            "rating": 5,
            "comment": "Amazing place! Highly recommend."
        },
        {
            "listing_id": 2,
            "user_id": 3,
            "rating": 4,
            "comment": "Very nice cottage, but a bit remote."
        },
        {
            "listing_id": 3,
            "user_id": 5,
            "rating": 3,
            "comment": "Decent cabin, but could use some updates."
        },
        {
            "listing_id": 4,
            "user_id": 2,
            "rating": 5,
            "comment": "Beautiful mountain village, loved it!"
        }
    ]
    for review in review_data:
        review_serializer = ReviewSerializer(data=review)
        if review_serializer.is_valid():
            review_serializer.save()
            print("Created review:", review_serializer.data)
        else:
            print("Failed to create review:", review_serializer.errors)

def run_seed():
    """
    Run the seeding process.
    """
    seed_users()
    seed_listings()
    seed_bookings()
    seed_reviews()
    print("Seeding completed.")


if __name__ == "__main__":
    run_seed()