# tests\conftest.py

import pytest
from src.clients.booking_client import BookingClient
from src.clients.auth_client import AuthClient
from src.config import Config


@pytest.fixture(scope="session")
def booking_client():
    b_client = BookingClient(base_url=Config.BASE_URL)
    yield b_client


@pytest.fixture(scope="session")
def auth_client():
    a_client = AuthClient(base_url=Config.BASE_URL)
    yield a_client


@pytest.fixture(scope="session")
def token(auth_client):
    login_token = auth_client.login(username=Config.USERNAME, password=Config.PASSWORD)
    return login_token
