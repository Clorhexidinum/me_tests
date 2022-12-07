import allure
import pytest
from maximumtest.utils.requests.my_requests import MyRequests
from maximumtest.utils.requests.request_data import RequestData
from maximumtest.utils.assertions.api_assert import Assertions
from maximumtest.test_resources.test_data.auth_module import data
from maximumtest.test_resources.json_schemas.error import schema


data = data
request = MyRequests()
assertion = Assertions()
error = schema
request_data = RequestData()


@allure.epic('Auth module')
@allure.suite('Auth negative')
@allure.tag('negative', 'api', 'auth')
@allure.label("owner", "Murat Kubekov")
@pytest.mark.parametrize("module_name", ["auth/login", "users", "auth", "auth/refresh"])
def test_unauthorized_for_(module_name):
    if data[module_name]["url"] == "auth/login" or data[module_name]["url"] == "users":
        with allure.step(f'Отправляю POST запрос на {data[module_name]["url"]}'):
            response = request.post(data[module_name]["url"])
        with allure.step('Проверяю что пришел статус 401 и правильное тело ответа'):
            assertion.correct_response(response, 401)

    if data[module_name]["url"] == "auth" or data[module_name]["url"] == "auth/refresh" or \
            data[module_name]["url"] == "users":
        with allure.step(f'Отправляю GET запрос на {data[module_name]["url"]}'):
            response = request.get(data[module_name]["url"])
        with allure.step('Проверяю что пришел статус 401 и правильное тело ответа'):
            assertion.correct_response(response, 401)

    if data[module_name]["url"] == "users":
        with allure.step(
                f'Отправляю PATCH запрос на {data[module_name]["url"]}/{request_data.incorrect_id()}'):
            response = request.patch(f'{data[module_name]["url"]}/{request_data.incorrect_id()}')
        with allure.step('Проверяю что пришел статус 401 и правильное тело ответа'):
            assertion.correct_response(response, 401)

    if data[module_name]["url"] == "users":
        with allure.step(
                f'Отправляю DELETE запрос на {data[module_name]["url"]}/{request_data.incorrect_id()}'):
            response = request.delete(f'{data[module_name]["url"]}/{request_data.incorrect_id()}')
        with allure.step('Проверяю что пришел статус 401 и правильное тело ответа'):
            assertion.correct_response(response, 401)


@allure.epic('Auth module')
@allure.suite('Auth negative')
@allure.tag('negative', 'api', 'auth')
@allure.label("owner", "Murat Kubekov")
def test_auth_wrong_user_data():
    with allure.step(f'Отправляю POST запрос c неправильными данными на {data["auth/login"]["url"]}'):
        response = request.post(data["auth/login"]["url"], data["auth/login"]["request"])
    with allure.step('Проверяю что пришел статус 400 и правильное тело ответа'):
        assertion.correct_response(response, 400, error)


@allure.epic('Auth module')
@allure.suite('Auth negative')
@allure.tag('negative', 'api', 'auth')
@allure.label("owner", "Murat Kubekov")
def test_auth_empty_user_data():
    with allure.step(f'Отправляю POST запрос c пустым body на {data["auth/login"]["url"]}'):
        response = request.post(data["auth/login"]["url"], {})
    with allure.step('Проверяю что пришел статус 401 и правильное тело ответа'):
        assertion.correct_response(response, 401, error)


@allure.epic('Auth module')
@allure.suite('Auth negative')
@allure.tag('negative', 'api', 'auth')
@allure.label("owner", "Murat Kubekov")
@pytest.mark.usefixtures('authorization')
def test_create_user_empty_data():
    with allure.step(f'Отправляю POST запрос c пустым body на {data["auth/login"]["url"]}'):
        response = request.post(data["users"]["url"], {}, cookies=pytest.auth_cookie)
    with allure.step('Проверяю что пришел статус 400 и правильное тело ответа'):
        assertion.correct_response(response, 400, error)


@allure.epic('Auth module')
@allure.suite('Auth negative')
@allure.tag('negative', 'api', 'auth')
@allure.label("owner", "Murat Kubekov")
@pytest.mark.usefixtures('authorization')
def test_create_user_repeated_data():
    repeated_user = {"email": "userForTest@DontRemove.com",
                     "name": "userForTestDontRemove",
                     "password": "userForTestDontRemove"}
    with allure.step(f'Отправляю POST запрос на создание существующего юзера на {data["auth/login"]["url"]}'):
        response = request.post(data["users"]["url"], repeated_user, cookies=pytest.auth_cookie)
    with allure.step('Проверяю что пришел статус 409 и правильное тело ответа'):
        assertion.correct_response(response, 409, error)


@allure.epic('Auth module')
@allure.suite('Auth negative')
@allure.tag('negative', 'api', 'auth')
@allure.label("owner", "Murat Kubekov")
@pytest.mark.usefixtures('authorization')
def test_patch_user_wrong_id():
    with allure.step(f'Отправляю PATCH запрос с неправильным ID на {data["auth/login"]["url"]}'):
        response = request.patch(f"{data['users']['url']}/{request_data.incorrect_id()}",
                                 data["auth/login"]["request"], cookies=pytest.auth_cookie)
    with allure.step('Проверяю что пришел статус 500 и правильное тело ответа'):
        assertion.correct_response(response, 500, error)


@allure.epic('Auth module')
@allure.suite('Auth negative')
@allure.tag('negative', 'api', 'auth')
@allure.label("owner", "Murat Kubekov")
@pytest.mark.usefixtures('authorization')
def test_delete_user_wrong_id():
    with allure.step(f'Отправляю DELETE запрос с неправильным ID на {data["auth/login"]["url"]}'):
        response = request.delete(f"{data['users']['url']}/{request_data.incorrect_id()}",
                                  data["auth/login"]["request"], cookies=pytest.auth_cookie)
    with allure.step('Проверяю что пришел статус 404 и правильное тело ответа'):
        assertion.correct_response(response, 404, error)


@allure.epic('Auth module')
@allure.suite('Auth negative')
@allure.tag('negative', 'api', 'auth')
@allure.label("owner", "Murat Kubekov")
@pytest.mark.usefixtures('authorization')
def test_self_delete_user():
    response = request.get(data["auth"]["url"], cookies=pytest.auth_cookie)
    with allure.step(f'Получаю ID юзера под которым авторизованы'):
        user_id = response.json().get('id')
    with allure.step(f'Отправляю DELETE запрос с полученным ID на {data["auth/login"]["url"]}'):
        del_user = request.delete(f'{data["users"]["url"]}/{user_id}', cookies=pytest.auth_cookie)
    with allure.step('Проверяю что пришел статус 400 и тело ответа соответствует схеме JSON'):
        assertion.correct_response(del_user, 400)
