# ---------------------------------- imports --------------------------------- #

from django.http import HttpRequest
from django.utils.translation import gettext as _
from django.contrib.auth import authenticate

from Subject.models import User

import requests
from requests import Response

# ----------------------------------- code ----------------------------------- #

class JwtTokens:
    def __init__(self, request: HttpRequest) -> None:
        
        self.request = request

        self.__get_tokens_url = f"http://{self.request.get_host()}/api/token"
        self.__access = None
        self.__refresh = None


    def login(self, username: str, password: str) -> bool:
        """Entrance to the account. With successful authorization and Access and Refresh tokens automatically
        Added to the user session.

        Args:
            username (str): User name
            password (str): user password

        Returns: 
            type: bool
        """
        response: Response = requests.post(url=self.__get_tokens_url, json={
            "username": username,
            "password": password,
        })

        if response.status_code == 200:
            self.__access = response.json()['access']
            self.__refresh = response.json()['refresh']
            self.tokens = self.__get_tokens()

            return True
        return False

    def __get_tokens(self) -> dict[str, str] | None:
        if self.__access is not None and self.__refresh is not None:
            return {
                "access": self.__access,
                "refresh": self.__refresh,
            }
        return None