# tests\test_bookings\test_booking_crud.py

import pytest
from requests.exceptions import HTTPError
from src.models.booking_model import BookingModel
from datetime import date


def test_booking_crud_flow(booking_client, token):
    booking_dict = {
        "firstname": "Ivan",
        "lastname": "Zumbo",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {"checkin": date(2026, 5, 3), "checkout": date(2026, 5, 6)},
        "additionalneeds": "",
    }
    booking_record = BookingModel(**booking_dict)
    resp = booking_client.create_booking(booking_data=booking_record)
    resp_json = resp.json()
    booking_id = resp_json["bookingid"]
    assert resp.status_code == 200
    assert resp_json["booking"]["firstname"] == booking_dict["firstname"]

    get_booking_resp = booking_client.get_booking(booking_id)
    assert get_booking_resp.firstname == booking_dict["firstname"]

    del_booking_resp = booking_client.delete_booking(booking_id, token=token)
    assert del_booking_resp.status_code == 201

    with pytest.raises(HTTPError) as exc_info:
        get_new_booking_resp = booking_client.get_booking(booking_id)
    assert exc_info.value.response.status_code == 404
