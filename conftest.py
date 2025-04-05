import logging

import pytest

from helpers.api_client import BookingAPIClient
from helpers.data_generator import DataGenerator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def api_client():
    """Session-scoped API client with authentication"""
    client = BookingAPIClient()
    auth_response = client.authenticate()
    assert auth_response.status_code == 200, "Authentication failed"
    yield client
    client.cleanup_test_data()


@pytest.fixture
def booking_data():
    """Generate fresh booking data for each test"""
    return DataGenerator.generate_valid_booking_data()


@pytest.fixture
def created_booking(api_client, booking_data):
    """Create a booking and return its ID, with automatic cleanup"""
    response = api_client.create_booking(booking_data)
    assert response.status_code == 200, "Booking creation failed"
    booking_id = response.json()["bookingid"]
    yield booking_id
    api_client.delete_booking(booking_id)
