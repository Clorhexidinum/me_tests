import allure
from maximumtest.utils.requests import MyRequests
from maximumtest.utils.assertions.api_assert import Assertions
from maximumtest.test_resources import GatewayData
from maximumtest.test_resources import schema
from maximumtest.utils.requests.request_data import RequestData

data = GatewayData.get_data()
request = MyRequests()
assertion = Assertions()
error = schema
request_data = RequestData()


@allure.epic('Gateway module')
@allure.feature('POST запросы')
@allure.suite('Gateway negative')
@allure.tag('negative', 'api', 'gateway')
@allure.label("owner", "Murat Kubekov")
def test_email_vacancy_incorrect_id():
    with allure.step(f'Отправляю POST запрос с некорректным ID на {data["email/vacancy"]["url"]}'):
        response = request.post(f'{data["email/vacancy"]["url"]}/{request_data.incorrect_id()}',
                                files=data["email/vacancy"]["request"])
    with allure.step('Проверяю что пришел статус 404 и тело ответа соответствует схеме JSON'):
        assertion.correct_response(response, 404)


@allure.epic('Gateway module')
@allure.feature('POST запросы')
@allure.suite('Gateway negative')
@allure.tag('negative', 'api', 'gateway')
@allure.label("owner", "Murat Kubekov")
def test_email_vacancy_empty_body():
    with allure.step(f'Отправляю POST запрос с пустым body на {data["email/vacancy"]["url"]}'):
        response = request.post(f'{data["email/vacancy"]["url"]}/{request_data.incorrect_id()}')
    with allure.step('Проверяю что пришел статус 400 и тело ответа соответствует схеме JSON'):
        assertion.correct_response(response, 400)


@allure.epic('Gateway module')
@allure.feature('GET запросы')
@allure.suite('Gateway negative')
@allure.tag('negative', 'api', 'gateway')
@allure.label("owner", "Murat Kubekov")
def test_get_registration_unauthorized():
    with allure.step(f'Отправляю GET запрос без авторизации на {data["get_registrations"]["url"]}'):
        response = request.get(f'{data["get_registrations"]["url"]}?crmId={request_data.crm_id()}')
    with allure.step('Проверяю что пришел статус 401 и тело ответа соответствует схеме JSON'):
        assertion.correct_response(response, 401, error)


@allure.epic('Gateway module')
@allure.feature('GET запросы')
@allure.suite('Gateway negative')
@allure.tag('negative', 'api', 'gateway')
@allure.label("owner", "Murat Kubekov")
def test_get_registration_report_unauthorized():
    with allure.step(f'Отправляю GET запрос без авторизации на {data["get_registrations"]["url"]}'):
        response = request.get(
            f'{data["get_registrations"]["url"]}/report?crmId={request_data.crm_id()}')
    with allure.step('Проверяю что пришел статус 401 и тело ответа соответствует схеме JSON'):
        assertion.correct_response(response, 401, error)


@allure.epic('Gateway module')
@allure.feature('DELETE запросы')
@allure.suite('Gateway negative')
@allure.tag('negative', 'api', 'gateway')
@allure.label("owner", "Murat Kubekov")
def test_delete_registration_unauthorized():
    with allure.step(f'Отправляю DELETE запрос без авторизации на {data["get_registrations"]["url"]}'):
        response = request.delete(
            f'{data["get_registrations"]["url"]}/{request_data.incorrect_id()}')
    with allure.step('Проверяю что пришел статус 401 и тело ответа соответствует схеме JSON'):
        assertion.correct_response(response, 401, error)


@allure.epic('Gateway module')
@allure.feature('GET запросы')
@allure.suite('Gateway negative')
@allure.tag('negative', 'api', 'gateway')
@allure.label("owner", "Murat Kubekov")
def test_delete_registration_incorrect_id():
    with allure.step(f'Отправляю GET запрос с некорректным ID на {data["get_registrations"]["url"]}'):
        response = request.get(f'{data["get_registrations"]["url"]}/{request_data.incorrect_id()}',
                               headers=request_data.auth_key())
    with allure.step('Проверяю что пришел статус 404 и тело ответа соответствует схеме JSON'):
        assertion.correct_response(response, 404, error)
