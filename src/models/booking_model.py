# src\models\booking_model.py

from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date


class BookingDates(BaseModel):
    checkin: date
    checkout: date


class BookingModel(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: Optional[str]
