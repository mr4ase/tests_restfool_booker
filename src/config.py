# src\config.py

import os

class Config:
    BASE_URL = os.getenv("BASE_URL_ENV", "https://restful-booker.herokuapp.com")
    USERNAME = os.getenv("USERNAME_ENV", "admin")
    PASSWORD = os.getenv("PASSWORD_ENV", "password123")
