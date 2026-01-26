# src\clients\booking_client.py
from .base_client import BaseClient
from requests import Response
from src.models.booking_model import BookingModel
from typing import List


class BookingClient(BaseClient):
    def __init__(self, base_url: str) -> None:
        super().__init__(base_url)
        self._endpoint_url = "booking"

    def get_booking_ids(self) -> list[dict]:
        return super()._request("GET", self._endpoint_url).json()

    def get_booking(self, id: int) -> BookingModel:
        booking_id_endpoint = f"{self._endpoint_url}/{id}"
        json_dict = super()._request("GET", booking_id_endpoint).json()
        return BookingModel(**json_dict)

    def create_booking(self, booking_data: BookingModel) -> Response:
        create_booking_r = self._request(
            "POST",
            endpoint=self._endpoint_url,
            json=booking_data.model_dump(mode="json"),
        )
        return create_booking_r

    def delete_booking(self, id: int, token: str) -> Response:
        delete_endpoint = f"{self._endpoint_url}/{id}"
        headers = {"Cookie": f"token={token}"}
        delete_booking_r = self._request(
            "DELETE", endpoint=delete_endpoint, headers=headers
        )
        return delete_booking_r
