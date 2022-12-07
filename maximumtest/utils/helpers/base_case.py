from requests import Response
import json.decoder


class BaseCase:

    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"В последнем запросе нет cookie с именем {cookie_name}"
        return response.cookies[cookie_name]

    def get_header(self, response: Response, headers_name):
        assert headers_name in response.headers, f"В последнем запросе нет заголовка с именем {headers_name}"
        return response.headers[headers_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Ответ пришел не в формате JSON. Текст ответа {response.text}"

        assert name in response_as_dict, f"В ответе JSON нет ключа {name}"

        return response_as_dict[name]

    def get_first_json_item(self, response: Response):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"\nБыл отправлен запрос на {response[59:]}. Ответ пришел не в формате JSON. Текст ответа {response.text}"
        return response_as_dict[0]
