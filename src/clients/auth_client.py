# src\clients\auth_client.py


from src.clients.base_client import BaseClient
from src.models.auth_model import AuthModel


class AuthClient(BaseClient):
    def __init__(self, base_url: str):
        super().__init__(base_url)
        self._endpoint_url = "auth"

    def login(self, username: str, password: str) -> str:
        payload = {"username": username, "password": password}
        auth_r = self._request(
            method="POST", endpoint=self._endpoint_url, json=payload
        ).json()
        auth_r_valid = AuthModel(**auth_r)
        return auth_r_valid.token
