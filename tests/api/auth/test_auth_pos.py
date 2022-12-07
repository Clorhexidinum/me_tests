import allure
import pytest
from maximumtest.utils.requests.my_requests import MyRequests
from maximumtest.utils.assertions.api_assert import Assertions
from maximumtest.test_resources.test_data.auth_module import data
from maximumtest.test_resources.json_schemas.auth_module import schemas
from maximumtest.utils.requests.request_data import RequestData

data = data
schema = schemas
request = MyRequests()
assertion = Assertions()
request_data = RequestData()


@allure.epic('Auth module')
@allure.suite('Auth positive')
@allure.tag('positive', 'api', 'auth')
@allure.label("owner", "Murat Kubekov")
@pytest.mark.usefixtures('authorization')
def test_get_user_requests():
    user_data = data["users"]
    with allure.step(f'Отправляю GET запрос на {user_data["url"]}'):
        response = request.get(user_data["url"], cookies=pytest.auth_cookie)
    with allure.step('Проверяю что пришел статус 200 и тело ответа соответствует схеме JSON'):
        assertion.correct_list_response(response, 200, schema["users"])


@allure.epic('Auth module')
@allure.suite('Auth positive')
@allure.tag('positive', 'api', 'auth')
@allure.label("owner", "Murat Kubekov")
@pytest.mark.usefixtures('authorization')
def test_post_path_del_user_requests():
    user_data = data["users"]
    with allure.step('Отправляю GET'):
        response = request.post(user_data["url"], user_data["request"], cookies=pytest.auth_cookie)
    with allure.step('Проверяю что пришел статус 201 и тело ответа соответствует схеме JSON'):
        assertion.correct_response(response, 201, schema["users"])
    with allure.step('Получаем ID юзера'):
        item_id = f"{user_data['url']}/{response.json().get('id')}"

    with allure.step('Отправляю PATCH с ID юзера'):
        response = request.patch(item_id, user_data["request"], cookies=pytest.auth_cookie)
    with allure.step('Проверяю что пришел статус 200 и тело ответа соответствует схеме JSON'):
        assertion.correct_response(response, 200, schema["users"])

    with allure.step('Отправляю DELETE с ID юзера'):
        response = request.delete(item_id, cookies=pytest.auth_cookie)
    with allure.step('Проверяю что пришел статус 204 и тело ответа соответствует схеме JSON'):
        assertion.correct_response(response, 204)


@allure.epic('Auth module')
@allure.suite('Auth positive')
@allure.tag('positive', 'api', 'auth')
@allure.label("owner", "Murat Kubekov")
def test_all_authorization_requests():
    auth = request_data.user_auth()
    with allure.step('Отправляю POST запрос на авторизацию'):
        response = request.post(auth["login_url"], auth["request"])
    with allure.step('Сохраняем Authentication cookie'):
        auth_cookie = {"Authentication": response.cookies['Authentication']}
    with allure.step('Сохраняем Refresh cookie'):
        refresh_cookie = {"Refresh": response.cookies['Refresh']}
    with allure.step('Проверяю что пришел статус 200 и тело ответа соответствует схеме JSON'):
        assertion.correct_response(response, 200, schema["auth/login"])

    with allure.step('Отправляю GET запрос на проверку авторизации с сохраненной cookie'):
        response = request.get(data["auth"]["url"], cookies=auth_cookie)
    with allure.step('Проверяю что пришел статус 200 и тело ответа соответствует схеме JSON'):
        assertion.correct_response(response, 200, schema["auth"])

    with allure.step('Отправляю GET запрос на рефреш авторизации с сохраненной cookie'):
        response = request.get(data["auth/refresh"]["url"], cookies=refresh_cookie)
    with allure.step('Проверяю что пришел статус 200 и тело ответа соответствует схеме JSON'):
        assertion.correct_response(response, 200, schema["auth/refresh"])

    with allure.step('Отправляю POST запрос на логаут с сохраненной cookie авторизаци'):
        response = request.post(auth["logout_url"], cookies=auth_cookie)
    with allure.step('Проверяю что пришел статус 200 и тело ответа соответствует схеме JSON'):
        assertion.correct_response(response, 200)
