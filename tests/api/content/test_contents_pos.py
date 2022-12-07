import allure
import pytest
from maximumtest.utils.requests.my_requests import MyRequests
from maximumtest.utils.assertions.api_assert import Assertions
from maximumtest.utils.helpers.base_case import BaseCase
from maximumtest.test_resources.test_data.content_module import ContentModuleData
from maximumtest.test_resources.json_schemas import content_module


@allure.epic('Content module')
@allure.suite('Content positive')
@allure.tag('positive', 'api', 'content')
@allure.label("owner", "Murat Kubekov")
@pytest.mark.usefixtures('authorization')
@pytest.mark.parametrize("module_name",
                         ["banners", "header", "header-banners", "header-category", "header-subcategory",
                          "product-card-labels", "product-cards", "summer-product-cards", "store-subject-templates",
                          "store-text-templates", "store-page-templates", "store-thanks-page-templates", "filters",
                          "teachers", "trial-lessons", "free-lessons", "vacancies", "accordion", "info-about-course",
                          "lead-forms", "regions", "catalog", "page-constructor/bullet-templates",
                          "page-constructor/first-screen-templates", "page-constructor/iframe-templates",
                          "page-constructor/text-block-templates", "page-constructor/html-block-templates",
                          "page-constructor/why-us-block-templates", "web-events", "web-event-filters",
                          "webhooks/marquiz", "handbooks", "footer", "footer-sections", "static-pages-first-screen",
                          "static-pages-group-info", "static-pages-guarantee-info", "static-pages-course-program",
                          "static-pages-benefits-info", "cities", "uchebnik/seo-settings"
                          ])
class TestContentsPos(BaseCase):
    data = ContentModuleData.get_data()
    schema = content_module.schemas["schemas"]
    request = MyRequests()
    assertion = Assertions()

    @allure.feature('GET запросы')
    def test_get_for(self, module_name):
        with allure.step(f'Отправляю GET запрос на {self.data[module_name]["url"]}'):
            response = self.request.get(self.data[module_name]["url"])
        with allure.step('Проверяю что пришел статус 200 и тело ответа соответствует схеме JSON'):
            self.assertion.correct_list_response(response, 200, self.schema[module_name])

    @allure.feature('POST запросы')
    def test_post_for(self, module_name):
        with allure.step(f'Отправляю POST запрос на {self.data[module_name]["url"]}'):
            response = self.request.post(self.data[module_name]["url"], self.data[module_name]['request'],
                                         cookies=pytest.auth_cookie)

        with allure.step('Проверяю что пришел статус 201 и тело ответа соответствует схеме JSON'):
            self.assertion.correct_response(response, 201, self.schema[module_name])

        with allure.step('Удаляю созданный элемент'):
            item_id = f"{self.data[module_name]['url']}/{self.get_json_value(response, 'id')}"
            self.request.delete(item_id, cookies=pytest.auth_cookie)

    @allure.feature('PATCH запросы')
    def test_patch_for(self, module_name):
        with allure.step('Создаю элемент'):
            response = self.request.post(self.data[module_name]["url"], self.data[module_name]['request'],
                                         cookies=pytest.auth_cookie)

        with allure.step('Сохраняю ID созданного элемента'):
            item_id = f"{self.data[module_name]['url']}/{self.get_json_value(response, 'id')}"

        if self.data[module_name] == "handbooks":
            with allure.step(f'Отправляю PATCH запрос c сохраненным ранее ID на {self.data[module_name]["url"]}'):
                response = self.request.patch(item_id, self.data[module_name]['request'],
                                              cookies=pytest.auth_cookie)

            with allure.step(f'Проверяю что пришел статус 200 и тело ответа соответствует схеме JSON'):
                self.assertion.correct_response(response, 200)
        else:
            pass

        with allure.step('Удаляю созданный элемент'):
            self.request.delete(item_id, cookies=pytest.auth_cookie)

    @allure.feature('DELETE запросы')
    def test_delete_for(self, module_name):
        with allure.step(f'Создаю элемент'):
            response = self.request.post(self.data[module_name]["url"], self.data[module_name]['request'],
                                         cookies=pytest.auth_cookie)
        with allure.step(f'Сохраняю ID созданного элемента'):
            item_id = f"{self.data[module_name]['url']}/{self.get_json_value(response, 'id')}"

        with allure.step(f'Отправляю DELETE запрос на {self.data[module_name]["url"]} с сохраненным ID'):
            self.request.delete(item_id, cookies=pytest.auth_cookie)


@allure.epic('Content module')
@allure.suite('Content positive')
@allure.tag('positive', 'api', 'content')
@allure.label("owner", "Murat Kubekov")
@pytest.mark.parametrize("module_name",
                         ["web-event-page", "static-pages-content"])
class TestNoPostRequest(BaseCase):
    data = ContentModuleData.get_data()
    schema = content_module.schemas["schemas"]
    request = MyRequests()
    assertion = Assertions()

    @allure.feature('GET запросы')
    def test_get_for(self, module_name):
        with allure.step(f'Отправляю GET запрос на {module_name}'):
            response = self.request.get(self.data[module_name]["url"])
        with allure.step('Проверяю что пришел статус 200 и тело ответа соответствует схеме JSON'):
            self.assertion.correct_response(response, 200, self.schema[module_name])


@allure.epic('Content module')
@allure.suite('Content positive')
@allure.tag('positive', 'api', 'content')
@allure.label("owner", "Murat Kubekov")
@pytest.mark.usefixtures('authorization')
@pytest.mark.parametrize("module_name", ["mass/product-card-labels", "mass/product-cards"])
class TestContentsMassPos(BaseCase):
    data = ContentModuleData.get_mass_data()
    schema = content_module.schemas["mass_schemas"]
    request = MyRequests()
    assertion = Assertions()

    @allure.feature('POST запросы')
    def test_post_for(self, module_name):
        with allure.step(f'Отправляю POST запрос на {self.data[module_name]["url"]}'):
            response = self.request.post(self.data[module_name]["url"], self.data[module_name]['request'],
                                         cookies=pytest.auth_cookie)

        with allure.step('Проверяю что пришел статус 201 и тело ответа соответствует схеме JSON'):
            self.assertion.correct_list_response(response, 201, self.schema[module_name])

        with allure.step('Удаляю созданную карточку'):
            first_item = self.get_first_json_item(response)
            item_id = first_item['id']
            self.request.delete(self.data[module_name]["url"], [item_id], cookies=pytest.auth_cookie)

    @allure.feature('PATCH запросы')
    def test_patch_for(self, module_name):
        with allure.step('Создаю элемент'):
            response = self.request.post(self.data[module_name]["url"], self.data[module_name]['request'],
                                         cookies=pytest.auth_cookie)

        with allure.step('Сохраняю ID созданного элемента'):
            first_item = self.get_first_json_item(response)
            item_id = first_item['id']

        with allure.step('Меняю данные в карточке'):
            without_id = self.data[module_name]['request'][0]
            with_id = {"id": item_id}
            without_id, with_id = with_id, without_id
            with_id.update(without_id)

        with allure.step(f'Отправляю PATCH запрос c сохраненным ранее ID на {self.data[module_name]["url"]}'):
            response = self.request.patch(self.data[module_name]["url"], [without_id], cookies=pytest.auth_cookie)
        with allure.step(f'Проверяю что пришел статус 200 и тело ответа соответствует схеме JSON'):
            self.assertion.correct_response(response, 200)

        with allure.step('Удаляю созданную карточку'):
            self.request.delete(self.data[module_name]["url"], [item_id], cookies=pytest.auth_cookie)

    @allure.feature('DELETE запросы')
    def test_delete_for(self, module_name):
        with allure.step('Создаю элемент'):
            response = self.request.post(self.data[module_name]["url"], self.data[module_name]['request'],
                                         cookies=pytest.auth_cookie)

        with allure.step(f'Получаю ID карточки'):
            first_item = self.get_first_json_item(response)
            item_id = first_item['id']

        with allure.step(f'Отправляю DELETE запрос c сохраненным ранее ID на {self.data[module_name]["url"]}'):
            response = self.request.delete(self.data[module_name]["url"], [item_id], cookies=pytest.auth_cookie)
        with allure.step(f'Проверяю что пришел статус 204 и тело ответа соответствует схеме JSON'):
            self.assertion.correct_response(response, 204)


@allure.epic('Content module')
@allure.suite('Content positive')
@allure.tag('positive', 'api', 'content')
@allure.label("owner", "Murat Kubekov")
@pytest.mark.usefixtures('authorization')
class TestContentsFilesPos(BaseCase):
    data = ContentModuleData.get_file_data()
    schema = content_module.schemas["file_schemas"]
    request = MyRequests()
    assertions = Assertions()

    @allure.feature('GET запросы')
    def test_get_for_files(self):
        with allure.step('Отправляю GET запрос на content/files/for_test_dont_remove'):
            response = self.request.get(self.data["files"]["url"], cookies=pytest.auth_cookie)
        with allure.step(f'Проверяю что пришел статус 200 и тело ответа соответствует схеме JSON'):
            self.assertions.correct_list_response(response, 200, self.schema["files"])

    @allure.feature('POST запросы')
    @pytest.mark.skip(reason="в запрос добавили поле filename, не знаю как его отправить")
    def test_post_for_files(self):
        with allure.step('Отправляю POST запрос c файлом на content/files/for_test_dont_remove'):
            response = self.request.post(url=self.data['files']['url'], cookies=pytest.auth_cookie,
                                         files=self.data['files']['request'])
        with allure.step('Проверяю что пришел статус 201 и тело ответа соответствует схеме JSON'):
            self.assertions.correct_response(response, 201, self.schema['files'])

        with allure.step('Удаляю созданный элемент'):
            item_id = f"{self.data['files']['url']}/{self.get_json_value(response, 'id')}"
            self.request.delete(item_id, cookies=pytest.auth_cookie)

    @allure.feature('DELETE запросы')
    @pytest.mark.skip(reason="в запрос добавили поле filename, не знаю как его отправить")
    def test_del_for_files(self):
        with allure.step('Создаю элемент'):
            response = self.request.post(url=self.data['files']['url'], cookies=pytest.auth_cookie,
                                         files=self.data['files']['request'])
        with allure.step('Сохраняю ID созданного элемента]'):
            item_id = f"{self.data['files']['url']}/{self.get_json_value(response, 'id')}"

        with allure.step(f'Отправляю DELETE запрос c сохраненным ранее ID на content/files/for_test_dont_remove'):
            response = self.request.delete(item_id, cookies=pytest.auth_cookie)
        with allure.step(f'Проверяю что пришел статус 204 и тело ответа соответствует схеме JSON'):
            self.assertions.correct_response(response, 204)
