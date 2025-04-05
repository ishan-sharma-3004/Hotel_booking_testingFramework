import random
import string
from datetime import datetime, timedelta


class DataGenerator:
    """Helper class for generating test data."""

    def generate_valid_credentials():
        """Returns a dictionary with valid credentials"""
        return {"username": "admin", "password": "password123"}

    def generate_invalid_credentials():
        """Returns a dictionary with invalid credentials"""
        return {"username": "invalid", "password": "wrongpassword"}

    def generate_valid_booking_data():
        """Returns a dictionary with valid booking data"""
        checkin = datetime.now() + timedelta(days=7)
        checkout = checkin + timedelta(days=3)
        return {
            "firstname": "John",
            "lastname": "Doe",
            "totalprice": random.randint(100, 1000),
            "depositpaid": True,
            "bookingdates": {
                "checkin": checkin.strftime("%Y-%m-%d"),
                "checkout": checkout.strftime("%Y-%m-%d"),
            },
            "additionalneeds": "Breakfast",
        }

    def generate_booking_with_missing_firstname():
        """Returns a dictionary with missing firstname"""
        data = DataGenerator.generate_valid_booking_data()
        del data["firstname"]
        return data

    def generate_booking_with_missing_lastname():
        """Returns a dictionary with missing lastname"""
        data = DataGenerator.generate_valid_booking_data()
        del data["lastname"]
        return data

    def generate_booking_with_invalid_dates():
        """Returns a dictionary with invalid dates"""
        data = DataGenerator.generate_valid_booking_data()
        data["bookingdates"]["checkin"] = "invalid-date"
        data["bookingdates"]["checkout"] = "invalid-date"
        return data

    def generate_booking_with_missing_dates():
        """Returns a dictionary with missing dates"""
        data = DataGenerator.generate_valid_booking_data()
        del data["bookingdates"]
        return data

    def generate_empty_booking_data():
        """Returns an empty dictionary"""
        return {}

    def generate_booking_with_long_names():
        """Returns a dictionary with long names"""
        data = DataGenerator.generate_valid_booking_data()
        data["firstname"] = "A" * 255
        data["lastname"] = "B" * 255
        return data

    def generate_booking_with_max_price():
        """Returns a dictionary with max price"""
        data = DataGenerator.generate_valid_booking_data()
        data["totalprice"] = int(2**31 - 1)  # Max 32-bit signed integer
        return data

    def generate_booking_with_min_price():
        """Returns a dictionary with min price"""
        data = DataGenerator.generate_valid_booking_data()
        data["totalprice"] = 0
        return data

    def generate_booking_with_special_chars():
        """Returns a dictionary with special characters"""
        data = DataGenerator.generate_valid_booking_data()
        data["firstname"] = "!$@n"
        data["lastname"] = "$@rm@"
        return data
