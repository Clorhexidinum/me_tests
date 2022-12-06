import os


class RequestData:
    @staticmethod
    def auth_key():
        auth_key = {"api-key": os.getenv('API_KEY')}
        return auth_key
    @staticmethod
    def user_auth():
        user_auth = {
            "login_url": "auth/login",
            "logout_url": "auth/logout",
            "request": {
                "email": "userForTest@DontRemove.com",
                "password": "userForTestDontRemove"
            }
        }
        return user_auth

    @staticmethod
    def incorrect_id():
        incorrect_id = "a111a1af-1a1a-111a-1aaa-f11111aa11a1"
        return incorrect_id

    @staticmethod
    def vacancy_id():
        vacancy_id = "bc6ad26d-aeb8-43a7-8883-1a7eed94583c"
        return vacancy_id

    @staticmethod
    def crm_id():
        crm_id = "CMP-000-000"
        return crm_id