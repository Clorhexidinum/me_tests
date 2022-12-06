from requests import Response
from jsonschema import validate
from maximumtest.utils.allure.attach import Attachments as attachments


class Assertions:
    @staticmethod
    def correct_response(response: Response, status_code, data=None):
        assert response.status_code == status_code, f"Был отправлен запрос на {response.url[59:]}. " \
                                                    f"Пришедший статус {response.status_code}."
        attachments.curl(response)
        attachments.headers(response)
        if data is None:
            pass
        else:
            response_as_dict = response.json()
            validate(response_as_dict, data)
            attachments.json(response)

    @staticmethod
    def correct_list_response(response: Response, status_code, data=None):
        assert response.status_code == status_code, f"Был отправлен запрос на {response.url[59:]}. " \
                                                    f"Пришедший статус {response.status_code}."
        attachments.curl(response)
        attachments.headers(response)
        if data is None:
            pass
        else:
            response_as_dict = response.json()
            for item in response_as_dict:
                validate(item, data)
            attachments.json(response)

    @staticmethod
    def key_comparison(response: Response, key_name, val_request):
        response_as_dict = response.json()

        try:
            result = True
            if key_name == "grade":
                key_name == "class"
            for item in response_as_dict:
                for key, val in item.items():
                    if key == key_name and val_request != val:
                        result = False
                        val_response = val
            assert result is True, f"\nБыл отправлен запрос на {response[59:]}. В ответе JSON не сработал фильтр " \
                                   f"{val_request}, значение {key_name}: {val_response}"
        except Exception:
            print(
                f"\nБыл отправлен запрос на {response[59:]}. В ответе JSON не сработал фильтр {val_request}, "
                f"значение {key_name}: {val_response}")
