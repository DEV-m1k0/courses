from django.http import HttpRequest

import requests
from requests import Response

class JwtTokens:
    def __init__(self) -> None:
        self.__get_tokens_url = f"http://127.0.0.1:8000/api/token"
        self.__access = None
        self.__refresh = None

    def login(self, username: str, password: str) -> None:
        response: Response = requests.post(url=self.__get_tokens_url, json={
            "username": username,
            "password": password,
        })

        if response.status_code == 200:
            self.__access = response.json()['access']
            self.__refresh = response.json()['refresh']

    def get_tokens(self) -> dict[str, str]:
        return {
            "access": self.__access,
            "refresh": self.__refresh,
        }

tokens = JwtTokens()
tokens.ACCESS = 'sjdvn'
print(tokens.ACCESS)