import json
import os
from datetime import datetime


class SelfHealing:
    """Class implementing self-healing mechanisms for tests"""

    DATA_FILE = "test_data.json"

    @classmethod
    def store_token(cls, token):
        """Store authentication token for recovery"""
        data = cls._load_data()
        data["token"] = token
        data["token_timestamp"] = str(datetime.now())
        cls._save_data(data)

    @classmethod
    def get_token(cls):
        """Retrieve stored token"""
        data = cls._load_data()
        return data.get("token")

    @classmethod
    def store_booking_id(cls, booking_id):
        """Store booking ID for recovery purposes"""
        data = cls._load_data()
        if "booking_ids" not in data:
            data["booking_ids"] = []
        if booking_id not in data["booking_ids"]:
            data["booking_ids"].append(booking_id)
        data["last_updated"] = str(datetime.now())
        cls._save_data(data)

    @classmethod
    def get_booking_ids(cls):
        """Retrieve all stored booking IDs"""
        data = cls._load_data()
        return data.get("booking_ids", [])

    @classmethod
    def remove_booking_id(cls, booking_id):
        """Remove a booking ID from storage"""
        data = cls._load_data()
        if "booking_ids" in data and booking_id in data["booking_ids"]:
            data["booking_ids"].remove(booking_id)
            cls._save_data(data)

    @classmethod
    def cleanup_test_data(cls):
        """Clean up any test data that might have been created"""
        data = cls._load_data()
        if "booking_ids" in data:
            # Implement cleanup logic if needed
            pass
        cls._save_data({})  # Clear all data

    @classmethod
    def _load_data(cls):
        """Load stored test data"""
        if not os.path.exists(cls.DATA_FILE):
            return {}

        with open(cls.DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}

    @classmethod
    def _save_data(cls, data):
        """Save test data to file"""
        with open(cls.DATA_FILE, "w") as f:
            json.dump(data, f)
