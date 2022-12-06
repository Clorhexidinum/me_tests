import allure
import pytest
from maximumtest.utils.requests import MyRequests
from maximumtest.utils.assertions.api_assert import Assertions
from maximumtest.test_resources import SurveysModule
from maximumtest.test_resources.json_schemas import schemas

data = SurveysModule.get_data()
schema = schemas
test_request = MyRequests()
test_assert = Assertions()


@allure.epic('Surveys module')
@allure.suite('Surveys positive')
@allure.tag('positive', 'api', 'surveys')
@allure.label("owner", "Murat Kubekov")
def test_generate_url_get_surveys():
    with allure.step(f'Отправляю POST запрос на {data["surveys/generate-url"]["url"]}'):
        response = test_request.post(data["surveys/generate-url"]["url"],
                                     data["surveys/generate-url"]["request"])
    with allure.step('Проверяю что пришел статус 201 и тело ответа соответствует схеме JSON'):
        test_assert.correct_response(response, 201)
    with allure.step('Сохраняю ID ответа'):
        surveys_id = response.text[59:]
    with allure.step(f'Отправляю GET запрос c сохраненным ID на {data["surveys"]["url"]}'):
        response = test_request.get(f'{data["surveys"]["url"]}?id={surveys_id}')
    with allure.step('Проверяю что пришел статус 200 и тело ответа соответствует схеме JSON'):
        test_assert.correct_response(response, 200, schema["surveys"])


@allure.epic('Surveys module')
@allure.feature('POST запросы')
@allure.suite('Surveys positive')
@allure.tag('positive', 'api', 'surveys')
@allure.label("owner", "Murat Kubekov")
@pytest.mark.skip(reason='Нет возможности динамически вытаскивать id')
def test_post_surveys_id():
    with allure.step(f'Отправляю POST запрос на {data["surveys/id"]["url"]}'):
        response = test_request.post(f'{data["surveys/id"]["url"]}/24004176985578021085',
                                     data["surveys/id"]["request"])
    with allure.step('Проверяю что пришел статус 201 и тело ответа соответствует схеме JSON'):
        test_assert.correct_response(response, 201)


@allure.epic('Surveys module')
@allure.suite('Surveys positive')
@allure.tag('positive', 'api', 'surveys')
@allure.label("owner", "Murat Kubekov")
def test_post_diagnostics():
    with allure.step(f'Отправляю POST запрос на {data["diagnostics"]["url"]}'):
        response = test_request.post(data["diagnostics"]["url"], data["diagnostics"]["request"])
    with allure.step('Проверяю что пришел статус 201 и тело ответа соответствует схеме JSON'):
        test_assert.correct_response(response, 201)

    with allure.step('Сохраняю код из ответа'):
        diagnostika_code = response.text
    with allure.step(f'Отправляю GET запрос c сохраненным кодом на {data["diagnostics"]["url"]}'):
        response = test_request.get(f'{data["diagnostics"]["url"]}?diagnostikaCode={diagnostika_code}')
    with allure.step('Проверяю что пришел статус 200 и тело ответа соответствует схеме JSON'):
        test_assert.correct_response(response, 200, schema["diagnostics"])
