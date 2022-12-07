import allure
from maximumtest.utils.requests.my_requests import MyRequests
from maximumtest.utils.assertions.api_assert import Assertions
from maximumtest.test_resources.test_data.surveys_module import SurveysModule
from maximumtest.test_resources.json_schemas.error import schema


data = SurveysModule.get_data()
request = MyRequests()
assertions = Assertions()
error = schema


@allure.epic('Surveys module')
@allure.feature('GET запросы')
@allure.suite('Surveys negative')
@allure.tag('negative', 'api', 'surveys')
@allure.label("owner", "Murat Kubekov")
def test_diagnostics_wrong_code():
    with allure.step(f'Отправляю GET запрос c несуществующим кодом диагностики на {data["diagnostics"]["url"]}'):
        response = request.get(f'{data["diagnostics"]["url"]}?diagnostikaCode=1312')
    with allure.step('Проверяю что пришел статус 404 и тело ответа соответствует схеме JSON'):
        assertions.correct_response(response, 404, error)


@allure.epic('Surveys module')
@allure.feature('GET запросы')
@allure.suite('Surveys negative')
@allure.tag('negative', 'api', 'surveys')
@allure.label("owner", "Murat Kubekov")
def test_diagnostics_not_number_code():
    with allure.step(f'Отправляю GET запрос c нецифровым кодом диагностики на {data["diagnostics"]["url"]}'):
        response = request.get(f'{data["diagnostics"]["url"]}?diagnostikaCode=qdqg')
    with allure.step('Проверяю что пришел статус 400 и тело ответа соответствует схеме JSON'):
        assertions.correct_response(response, 400, error)

