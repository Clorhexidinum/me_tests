import datetime
import allure
import pytest
from maximumtest.utils.allure.attach import Attachments as attachments
from maximumtest.utils.assertions.api_assert import Assertions
from maximumtest.utils.requests.my_requests import MyRequests
from maximumtest.test_resources.json_schemas.crm_module import schemas
from maximumtest.test_resources.test_data.crm_module import CrmModuleData

data = CrmModuleData.get_data()
request = MyRequests()
schema = schemas
assertion = Assertions()
error = schema


@allure.epic('CRM module')
@allure.feature('POST запросы')
@allure.suite('CRM positive')
@allure.tag('negative', 'api', 'crm')
@allure.label("owner", "Murat Kubekov")
@pytest.mark.usefixtures('authorization')
def test_registrations():
    with allure.step(f'Отправляю POST запрос на {data["registrations"]["url"]}'):
        response = request.post(data["registrations"]["url"], data["registrations"]["request"])
    with allure.step('Проверяю что пришел статус 201 и тело ответа соответствует схеме JSON'):
        assertion.correct_response(response, 201, schema["registrations"])


@allure.epic('CRM module')
@allure.feature('POST запросы')
@allure.suite('CRM positive')
@allure.tag('positive', 'api', 'crm')
@allure.label("owner", "Murat Kubekov")
@pytest.mark.usefixtures('authorization')
def test_registration_proftest():
    with allure.step(f'Отправляю POST запрос с пустым телом на {data["proftest"]["url"]}'):
        response = request.post(data["proftest"]["url"], data["proftest"]["request"])
    with allure.step('Проверяю что пришел статус 201 и тело ответа соответствует схеме JSON'):
        assertion.correct_response(response, 201)


@allure.epic('CRM module')
@allure.feature('GET запросы')
@allure.suite('CRM positive')
@allure.tag('positive', 'api', 'crm')
@allure.label("owner", "Murat Kubekov")
@pytest.mark.usefixtures('authorization')
def test_get_all_groups():
    with allure.step(f'Отправляю GET запрос на {data["groups"]["url"]}'):
        response = request.get(data["groups"]["url"])
    with allure.step('Проверяю что пришел статус 200 и тело ответа соответствует схеме JSON'):
        assertion.correct_list_response(response, 200, schema["groups"])


@allure.epic('CRM module')
@allure.feature('GET запросы')
@allure.suite('CRM positive')
@allure.tag('positive', 'api', 'crm')
@allure.label("owner", "Murat Kubekov")
@pytest.mark.usefixtures('authorization')
def test_get_group_with_id():
    with allure.step('Отправляю GET запрос на получение всех групп'):
        response_group = request.get(data["groups"]["url"])
    response_as_dict = response_group.json()
    with allure.step('Сохраняю ID группы'):
        lms_id = ''
    for item in response_as_dict:
        for key, val in item.items():
            if item["lmsId"] and val is not None:
                lms_id = val
    with allure.step(f'Отправляю GET запрос с сохраненным ID на {data["groups"]["url"]}'):
        response = request.get(f'{data["groups"]["url"]}/{lms_id}')
    with allure.step('Проверяю что пришел статус 200 и тело ответа соответствует схеме JSON'):
        assertion.correct_response(response, 200, schema["groups"])


@allure.epic('CRM module')
@allure.feature('GET запросы')
@allure.suite('CRM positive')
@allure.tag('positive', 'api', 'crm')
@allure.label("owner", "Murat Kubekov")
@pytest.mark.usefixtures('authorization')
def test_filter_min_start_learning():
    with allure.step('Выбираю минимальную дату начала обучения'):
        today = f'minStartLearning={datetime.datetime.today().strftime("%Y-%m-%d")}'
    with allure.step(f'Отправляю GET запрос с выбранной датой на {data["groups"]["url"]}'):
        response = request.get(f'{data["groups"]["url"]}?{today}')
    with allure.step('Получаю группы подходящие по дате'):
        response_as_dict = response.json()
    with allure.step('Проверяю дату начала в пришедших группах'):
        result = True
    for item in response_as_dict:
        for key, val in item.items():
            if key == "learningStartDate" and val[:10] < today[17:]:
                result = False
    assert result is True
    attachments.curl(response)
    attachments.headers(response)
    attachments.json(response)


@allure.epic('CRM module')
@allure.feature('GET запросы')
@allure.suite('CRM positive')
@allure.tag('positive', 'api', 'crm')
@allure.label("owner", "Murat Kubekov")
@pytest.mark.usefixtures('authorization')
def test_filter_max_start_learning():
    with allure.step('Выбираю максимальную дату начала обучения'):
        max_start = datetime.datetime.today() + datetime.timedelta(days=60)
    today = f'maxStartLearning={max_start.strftime("%Y-%m-%d")}'
    with allure.step(f'Отправляю GET запрос с выбранной датой на {data["groups"]["url"]}'):
        response = request.get(f'{data["groups"]["url"]}?{today}')
    with allure.step('Получаю группы подходящие по дате'):
        response_as_dict = response.json()
    with allure.step('Проверяю дату начала в пришедших группах'):
        result = True
    for item in response_as_dict:
        for key, val in item.items():
            if key == "learningStartDate" and val is not None and val[:10] > today[17:]:
                result = False
    assert result is True
    attachments.curl(response)
    attachments.headers(response)
    attachments.json(response)


@allure.epic('CRM module')
@allure.feature('GET запросы')
@allure.suite('CRM positive')
@allure.tag('positive', 'api', 'crm')
@allure.label("owner", "Murat Kubekov")
@pytest.mark.usefixtures('authorization')
@pytest.mark.parametrize("key_name, val_request",
                         [("territory", "Москва"),
                          ("brand", "Курсы IT и Digital"),
                          ("format", "Блендед_Групповой"),
                          ("grade", "11"),
                          ("discipline", "Курсы IT"),
                          ("courseId", "9c3e21f5-9ac8-e811-a97a-000d3ab20be2")])
def test_one_filter(key_name, val_request):
    with allure.step(f'Подготавливаю параметры фильтра: {key_name}={val_request}'):
        param = f'{key_name}={val_request}'
    with allure.step(f'Отправляю GET запрос с выбранными параметрами на {data["groups"]["url"]}'):
        response = request.get(f'{data["groups"]["url"]}?{param}')
    with allure.step('Проверяю выбранные параметры в пришедших группах'):
        assertion.key_comparison(response, key_name, val_request)
        attachments.curl(response)
        attachments.headers(response)
        attachments.json(response)


@allure.epic('CRM module')
@allure.feature('GET запросы')
@allure.suite('CRM positive')
@allure.tag('positive', 'api', 'crm')
@allure.label("owner", "Murat Kubekov")
@pytest.mark.usefixtures('authorization')
@pytest.mark.parametrize("key1, val1", [("territory", "Москва"), ("format", "Блендед_Групповой"), ])
@pytest.mark.parametrize("key2, val2", [("brand", "Курсы IT и Digital"), ("grade", "11")])
@pytest.mark.parametrize("key3, val3",
                         [("discipline", "Обществознание"), ("courseId", "c23e21f5-9ac8-e811-a97a-000d3ab20be2")])
def test_several_filters(key1, val1, key2, val2, key3, val3):
    with allure.step(f'Подготавливаю параметры фильтра: {key1}={val1}&{key2}={val2}'):
        param = f'{key1}={val1}&{key2}={val2}'
    with allure.step(f'Отправляю GET запрос с выбранными параметрами на {data["groups"]["url"]}'):
        response = request.get(f'{data["groups"]["url"]}?{param}')
        attachments.json(response)
    with allure.step('Получаю группы подходящие по параметрам'):
        response_as_dict = response.json()

    if response.status_code != 404:
        with allure.step('Проверяю выбранные параметры в пришедших группах'):
            result = True
        if key2 == "grade":
            key2 == "class"
        for item in response_as_dict:
            for key, val in item.items():
                if item[key1] != val1 and item[key2] != val2 and item[key3] != val3:
                    result = False
            assert result is True
    else:
        assertion.correct_response(response, 404, error)
    attachments.curl(response)
    attachments.headers(response)
    attachments.json(response)


@allure.epic('CRM module')
@allure.feature('GET запросы')
@allure.suite('CRM positive')
@allure.tag('positive', 'api', 'crm')
@allure.label("owner", "Murat Kubekov")
@pytest.mark.usefixtures('authorization')
def test_filters_no_group():
    with allure.step(
            f'Отправляю GET запрос c датой начала обучения через 100 лет на {data["groups"]["url"]}'):
        response = request.get(f'{data["groups"]["url"]}?minStartLearning=2222-12-31')
    with allure.step('Проверяю что не получили группы, статус 404 и тело ответа соответствует схеме JSON'):
        assertion.correct_response(response, 404, error)
