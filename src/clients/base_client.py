# src\clients\base_client.py
import requests
from loguru import logger
from requests import Response
import urllib.parse


class BaseClient:
    def __init__(self, base_url: str) -> None:
        self._base_url = base_url
        self._session = requests.Session()
        self._allowed_methods = ["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD"]

    def _request(self, method: str, endpoint: str, **kwargs) -> Response:

        endpath = urllib.parse.urljoin(self._base_url.strip("/"), endpoint.strip("/"))
        request_method = method.upper()
        logger.info(f"Request: [{request_method}][{endpath}]")
        if method not in self._allowed_methods:
            logger.error(f"The method {method} is not allowed")
            raise Exception(f"The method {method} is not allowed")

        r = self._session.request(method=method, url=endpath, **kwargs)
        r.raise_for_status()
        return r
