import allure
import pytest
from maximumtest.utils.requests import MyRequests
from maximumtest.utils.assertions.api_assert import Assertions
from maximumtest.test_resources import PaymentsModuleData

# import datetime

data = PaymentsModuleData.get_data()
request = MyRequests()
assertion = Assertions()


@allure.epic('Payments module')
@allure.feature('GET запросы')
@allure.suite('Payments positive')
@allure.tag('positive', 'api', 'payments')
@allure.label("owner", "Murat Kubekov")
@pytest.mark.xfail(reason="Непонятная логика работы и сам запрос в свагере выкидывает 500 статус")
@pytest.mark.parametrize("payment_type", ["once", "recurrent"])
def test_payments_program(payment_type):
    # with allure.step('Создаем body с уникальным полем parentEmail'):
    #     request_body = data["payments/program"]["request"]
    #     request_body["parentEmail"] = f'{datetime.datetime.today().strftime("%Y%m%d%H%M%S%f")}@test.ru'
    with allure.step(f'Отправляю GET запрос на {data["payments"]["url"]}?paymentType={payment_type}'):
        response = request.post(f'{data["payments"]["url"]}?paymentType={payment_type}\
        &url=%2Foge%2Fstore', data["payments"]["request"])
    with allure.step('Проверяю что пришел статус 201 и тело ответа соответствует схеме JSON'):
        assertion.correct_response(response, 201)


@allure.epic('Payments module')
@allure.feature('GET запросы')
@allure.suite('Payments positive')
@allure.tag('positive', 'api', 'payments')
@allure.label("owner", "Murat Kubekov")
def test_payments_program_repeat():
    with allure.step(f'Отправляю GET запрос на {data["payments/repeat"]["url"]}'):
        response = request.post(f'{data["payments/repeat"]["url"]}',
                                data["payments/repeat"]["request"])
    with allure.step('Проверяю что пришел статус 201 и тело ответа соответствует схеме JSON'):
        assertion.correct_response(response, 201)


@allure.epic('Payments module')
@allure.feature('GET запросы')
@allure.suite('Payments positive')
@allure.tag('positive', 'api', 'payments')
@allure.label("owner", "Murat Kubekov")
def test_zero_contact():
    with allure.step(f'Отправляю GET запрос на {data["zero-contract"]["url"]}'):
        response = request.post(data["zero-contract"]["url"], data["zero-contract"]["request"])
    with allure.step('Проверяю что пришел статус 201 и тело ответа соответствует схеме JSON'):
        assertion.correct_response(response, 201)
