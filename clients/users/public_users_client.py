from clients.api_client import APIClient
from typing import TypedDict
from httpx import Response


class CreateUserDict(TypedDict):
    """
    Структура запроса на создание пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    API клиент для публичных методов пользователя
    """

    def create_user_api(self, request: CreateUserDict) -> Response:
        """
        Метод создает нового пользователя.

        :param request:
            Данные для создания пользователя:
            email, password, firstName, lastName, middleName
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)
