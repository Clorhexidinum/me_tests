import allure
import pytest
from maximumtest.utils.requests.my_requests import MyRequests
from maximumtest.utils.assertions.api_assert import Assertions
from maximumtest.test_resources.test_data.crm_module import CrmModuleData
from maximumtest.test_resources.json_schemas.error import schema
from maximumtest.utils.requests.request_data import RequestData

data = CrmModuleData.get_data()
request = MyRequests()
assertion = Assertions()
error = schema
request_data = RequestData()


@allure.epic('CRM module')
@allure.feature('POST запросы')
@allure.suite('CRM negative')
@allure.tag('negative', 'api', 'crm')
@allure.label("owner", "Murat Kubekov")
@pytest.mark.usefixtures('authorization')
def test_empty_registrations():
    with allure.step(f'Отправляю POST запрос с пустым телом на {data["registrations"]["url"]}'):
        response = request.post(data["registrations"]["url"])
    with allure.step('Проверяю что пришел статус 400 и тело ответа соответствует схеме JSON'):
        assertion.correct_response(response, 400, error)


@allure.epic('CRM module')
@allure.feature('POST запросы')
@allure.suite('CRM negative')
@allure.tag('negative', 'api', 'crm')
@allure.label("owner", "Murat Kubekov")
@pytest.mark.usefixtures('authorization')
def test_empty_registration_proftest():
    with allure.step(f'Отправляю POST запрос с пустым телом на {data["proftest"]["url"]}'):
        response = request.post(data["proftest"]["url"])
    with allure.step('Проверяю что пришел статус 400 и тело ответа соответствует схеме JSON'):
        assertion.correct_response(response, 400, error)


@allure.epic('CRM module')
@allure.feature('POST запросы')
@allure.suite('CRM negative')
@allure.tag('negative', 'api', 'crm')
@allure.label("owner", "Murat Kubekov")
@pytest.mark.usefixtures('authorization')
def test_incorrect_group_id():
    with allure.step(f'Отправляю POST запрос с несуществующим Group ID на {data["registrations"]["url"]}'):
        response = request.post(f'{data["groups"]["url"]}/{request_data.incorrect_id()}')
    with allure.step('Проверяю что пришел статус 404 и тело ответа соответствует схеме JSON'):
        assertion.correct_response(response, 404, error)
