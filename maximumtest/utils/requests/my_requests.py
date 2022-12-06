import requests
from maximumtest.utils.allure.attach import Attachments as attachments


class MyRequests:
    @staticmethod
    def post(url: str, data: dict = None, headers: dict = None, cookies: dict = None, files: dict = None):
        attachments.body(url, data)
        return MyRequests._send(url, data, headers, cookies, "POST", files)

    @staticmethod
    def get(url: str, data: dict = None, headers: dict = None, cookies: dict = None, files: dict = None):
        return MyRequests._send(url, data, headers, cookies, "GET", files)

    @staticmethod
    def patch(url: str, data: dict = None, headers: dict = None, cookies: dict = None, files: dict = None):
        attachments.body(url, data)
        return MyRequests._send(url, data, headers, cookies, "PATCH", files)

    @staticmethod
    def delete(url: str, data: dict = None, headers: dict = None, cookies: dict = None, files: dict = None):
        return MyRequests._send(url, data, headers, cookies, "DELETE", files)

    @staticmethod
    def _send(url: str, data: dict, headers: dict, cookies: dict, method: str, files: dict):
        url = f"https://staging-ru.maximumtest.test01.maximumtest.ru/api/v3/{url}"

        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}
        if files is None:
            files = {}

        if method == "GET":
            response = requests.get(url, params=data, headers=headers, cookies=cookies)
        elif method == "POST":
            response = requests.post(url, json=data, headers=headers, cookies=cookies, files=files)
        elif method == "PATCH":
            response = requests.patch(url, json=data, headers=headers, cookies=cookies)
        elif method == "DELETE":
            response = requests.delete(url, json=data, headers=headers, cookies=cookies)
        else:
            raise Exception(f"Неправильный HTTP метод, '{method}' был получен.")

        return response
