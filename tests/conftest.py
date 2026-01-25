# tests\conftest.py

import pytest

@pytest.fixture(scope = "session")
def booking_client():
    url = "https://restful-booker.herokuapp.com"
    b_client = BookingClient(base_url=url)
    yield b_client