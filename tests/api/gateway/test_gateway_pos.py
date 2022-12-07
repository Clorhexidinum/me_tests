import allure
from maximumtest.utils.requests.my_requests import MyRequests
from maximumtest.utils.assertions.api_assert import Assertions
from maximumtest.test_resources.test_data.gateway import GatewayData
from maximumtest.test_resources.json_schemas.gateway import schemas
from maximumtest.utils.requests.request_data import RequestData

data = GatewayData.get_data()
schema = schemas
request = MyRequests()
assertion = Assertions()
request_data = RequestData()


@allure.epic('Gateway module')
@allure.feature('GET запросы')
@allure.suite('Gateway positive')
@allure.tag('positive', 'api', 'gateway')
@allure.label("owner", "Murat Kubekov")
def test_health():
    with allure.step('Отправляю GET запрос на проверку состояния'):
        response = request.get(data["health"]["url"])
    with allure.step('Проверяю что пришел статус 200 и тело ответа соответствует схеме JSON'):
        assertion.correct_response(response, 200, schema["health"])


@allure.epic('Gateway module')
@allure.feature('GET запросы')
@allure.suite('Gateway positive')
@allure.tag('positive', 'api', 'gateway')
@allure.label("owner", "Murat Kubekov")
def test_email_vacancy():
    with allure.step(f'Отправляю GET запрос на {data["email/vacancy"]["url"]}'):
        response = request.post(f'{data["email/vacancy"]["url"]}/{request_data.vacancy_id()}',
                                files=data["email/vacancy"]["request"])
    with allure.step('Проверяю что пришел статус 201 и тело ответа соответствует схеме JSON'):
        assertion.correct_response(response, 201, schema["email/vacancy"])


@allure.epic('Gateway module')
@allure.feature('GET запросы')
@allure.suite('Gateway positive')
@allure.tag('positive', 'api', 'gateway')
@allure.label("owner", "Murat Kubekov")
def test_get_registration():
    with allure.step(f'Отправляю GET запрос на {data["get_registrations"]["url"]}'):
        response = request.get(f'{data["get_registrations"]["url"]}?crmId={request_data.crm_id()}',
                               headers=request_data.auth_key())
    with allure.step('Проверяю что пришел статус 200 и тело ответа соответствует схеме JSON'):
        assertion.correct_list_response(response, 200, schema["get_registrations"])


@allure.epic('Gateway module')
@allure.feature('GET запросы')
@allure.suite('Gateway positive')
@allure.tag('positive', 'api', 'gateway')
@allure.label("owner", "Murat Kubekov")
def test_get_registration_report():
    with allure.step(f'Отправляю GET запрос на {data["get_registrations"]["url"]}/report'):
        response = request.get(f'{data["get_registrations"]["url"]}/report?crmId={request_data.crm_id()}',
                               headers=request_data.auth_key())
    with allure.step('Проверяю что пришел статус 200 и тело ответа соответствует схеме JSON'):
        assertion.correct_response(response, 200)


@allure.epic('Gateway module')
@allure.suite('Gateway positive')
@allure.tag('positive', 'api', 'gateway')
@allure.label("owner", "Murat Kubekov")
def test_post_del_registration():
    with allure.step(f'Отправляю POST запрос на {data["post_registrations"]["url"]}'):
        response = request.post(data["post_registrations"]["url"], data["post_registrations"]["request"])
    with allure.step('Проверяю что пришел статус 201 и тело ответа соответствует схеме JSON'):
        assertion.correct_response(response, 201, schema["post_registrations"])
    with allure.step('Сохраняю ID созданной регистрации'):
        reg_id = f"{data['post_registrations']['url']}/{response.json().get('registrationId')}"
    with allure.step('Удаляю созданную регистрацию с сохраненным ID'):
        response = request.delete(reg_id, headers=request_data.auth_key())
    with allure.step('Проверяю что пришел статус 204 и тело ответа соответствует схеме JSON'):
        assertion.correct_response(response, 204)
