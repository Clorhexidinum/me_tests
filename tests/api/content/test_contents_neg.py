import allure
import pytest
from maximumtest.utils.requests.my_requests import MyRequests
from maximumtest.utils.assertions.api_assert import Assertions
from maximumtest.utils.helpers.base_case import BaseCase
from maximumtest.test_resources.test_data.content_module import ContentModuleData
from maximumtest.test_resources.json_schemas.error import schema
from maximumtest.test_resources.json_schemas import content_module
from maximumtest.utils.requests.request_data import RequestData


@allure.epic('Content module')
@allure.suite('Content negative')
@allure.tag('negative', 'api', 'content')
@allure.label("owner", "Murat Kubekov")
@pytest.mark.parametrize("module_name",
                         ["banners", "header", "header_banners", "header-category", "header-subcategory",
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
class TestContentsNeg(BaseCase):
    data = ContentModuleData.get_data()
    request = MyRequests()
    assertion = Assertions()
    error = schema
    request_data = RequestData()

    @allure.feature('POST запросы')
    def test_post_unauthorized_for(self, module_name):
        with allure.step(f'Отправляю POST запрос на {self.data[module_name]["url"]}'):
            response = self.request.post(self.data[module_name]["url"], self.data[module_name]['request'])
        with allure.step('Проверяю что пришел статус 401 и тело ответа соответствует схеме JSON'):
            self.assertion.correct_response(response, 401, self.error)

    @allure.feature('POST запросы')
    @pytest.mark.usefixtures('authorization')
    def test_post_empty_body_for(self, module_name):
        with allure.step(f'Отправляю POST запрос c пустым телом на {self.data[module_name]["url"]}'):
            response = self.request.post(self.data[module_name]["url"], {}, cookies=pytest.auth_cookie)
        if self.data[module_name]["url"] == "content/categories" or self.data[module_name][
            "url"] == "content/page-constructor/bullet-templates" \
                or self.data[module_name]["url"] == "content/page-constructor/first-screen-templates":
            with allure.step('Проверяю что пришел статус 500'):
                self.assertion.correct_response(response, 500)
        else:
            with allure.step('Проверяю что пришел статус 400 и тело ответа соответствует схеме JSON'):
                self.assertion.correct_response(response, 400, self.error)

    @allure.feature('PATCH запросы')
    def test_patch_unauthorized_for(self, module_name):
        if self.data[module_name]["url"] != "content/subjects" and self.data[module_name]["url"] \
                != "content/vacancy-areas" and self.data[module_name]["url"] != "content/vacancy-experiences" \
                and self.data[module_name]["url"] != "content/categories":
            with allure.step(f'Отправляю PATCH запрос на {self.data[module_name]["url"]}'):
                response = self.request.patch(f'{self.data[module_name]["url"]}/test_id',
                                              self.data[module_name]['request'])
            with allure.step('Проверяю что пришел статус 401 и тело ответа соответствует схеме JSON'):
                self.assertion.correct_response(response, 401, self.error)
        else:
            pytest.skip()

    @allure.feature('PATCH запросы')
    @pytest.mark.usefixtures('authorization')
    def test_patch_id_incorrect_for(self, module_name):
        if self.data[module_name]["url"] != "content/subjects" and self.data[module_name]["url"] \
                != "content/vacancy-areas" and \
                self.data[module_name][
                    "url"] != "content/vacancy-experiences" and self.data[module_name]["url"] != "content/categories":
            with allure.step(f'Отправляю PATCH запрос c неправильным ID на {self.data[module_name]["url"]}'):
                response = self.request.patch(f"{self.data[module_name]['url']}/{self.request_data.incorrect_id()}",
                                              self.data[module_name]['request'], cookies=pytest.auth_cookie)
            if self.data[module_name]["url"] == "content/header" or self.data[module_name]["url"] \
                    == "content/header-category" or \
                    self.data[module_name][
                        "url"] == "content/product-cards":
                pass
                # pytest.skip(reason='В API нет проверок на данные запросы, когда исправят уберем эту часть')
            else:
                with allure.step('Проверяю что пришел статус 404 и тело ответа соответствует схеме JSON'):
                    self.assertion.correct_response(response, 404, self.error)
        else:
            pass

    @allure.feature('DELETE запросы')
    def test_delete_unauthorized_for(self, module_name):
        with allure.step(f'Отправляю DELETE запрос без авторизации на {self.data[module_name]["url"]}'):
            response = self.request.delete(f"{self.data[module_name]['url']}/test_id",
                                           self.data[module_name]['request'])
        with allure.step('Проверяю что пришел статус 401 и тело ответа соответствует схеме JSON'):
            self.assertion.correct_response(response, 401, self.error)

    @allure.feature('DELETE запросы')
    @pytest.mark.usefixtures('authorization')
    def test_delete_id_incorrect_for(self, module_name):
        if self.data[module_name]["url"] != "content/subjects" and self.data[module_name]["url"] \
                != "content/vacancy-areas" and \
                self.data[module_name][
                    "url"] != "content/vacancy-experiences" and self.data[module_name]["url"] != "content/categories":
            with allure.step(f'Отправляю DELETE запрос c неправильным ID на {self.data[module_name]["url"]}'):
                response = self.request.delete(f"{self.data[module_name]['url']}/{self.request_data.incorrect_id()}",
                                               cookies=pytest.auth_cookie)
            if self.data[module_name]["url"] == "content/header" or self.data[module_name]["url"] \
                    == "content/header-category":
                pass
                # pytest.skip(reason='В API нет проверок на данные запросы, когда исправят уберем эту часть')
            else:
                with allure.step('Проверяю что пришел статус 404 и тело ответа соответствует схеме JSON'):
                    self.assertion.correct_response(response, 404, self.error)
        else:
            pytest.skip()


@allure.epic('Content module')
@allure.suite('Content negative')
@allure.tag('negative', 'api', 'content')
@allure.label("owner", "Murat Kubekov")
@pytest.mark.parametrize("test_module", ["accordion", "filters", "static-pages-first-screen", "static-pages-group-info",
                                         "static-pages-guarantee-info", "static-pages-course-program",
                                         "static-pages-benefits-info"])
class TestContentsNoUniqBody(BaseCase):
    data = ContentModuleData.get_data()
    schema = content_module.schemas["schemas"]
    request = MyRequests()
    assertion = Assertions()
    error = schema

    @allure.feature('POST запросы')
    @pytest.mark.usefixtures('authorization')
    def test_non_unique_body(self, test_module):
        with allure.step('Создаем элемент'):
            response = self.request.post(self.data[test_module]["url"], self.data[test_module]['request'],
                                         cookies=pytest.auth_cookie)
        with allure.step('Сохраняем ID созданного элемента'):
            item_id = f"{self.data[test_module]['url']}/{self.get_json_value(response, 'id')}"
            self.assertion.correct_response(response, 201, self.schema[test_module])

        with allure.step(f'Отправляю POST запрос с таким же телом на {self.data[test_module]["url"]}'):
            response = self.request.post(self.data[test_module]["url"], self.data[test_module]['request'],
                                         cookies=pytest.auth_cookie)
        with allure.step('Проверяю что пришел статус 409 и тело ответа соответствует схеме JSON'):
            self.assertion.correct_response(response, 409, self.error)
        with allure.step('Удаляем созданный элемент'):
            response = self.request.delete(item_id, cookies=pytest.auth_cookie)
            self.assertion.correct_response(response, 204)


@allure.epic('Content module')
@allure.suite('Content negative')
@allure.tag('negative', 'api', 'content')
@allure.label("owner", "Murat Kubekov")
@pytest.mark.parametrize("module_name", ["mass/product-card-labels", "mass/product-cards"])
class TestContentsMassNeg(BaseCase):
    data = ContentModuleData.get_mass_data()
    request = MyRequests()
    assertion = Assertions()
    error = schema
    request_data = RequestData()

    @allure.feature('POST запросы')
    def test_post_unauthorized_for(self, module_name):
        with allure.step(f'Отправляю POST запрос без авторизации на {self.data[module_name]["url"]}'):
            response = self.request.post(self.data[module_name]["url"], self.data[module_name]['request'])
        with allure.step('Проверяю что пришел статус 401 и тело ответа соответствует схеме JSON'):
            self.assertion.correct_response(response, 401, self.error)

    @allure.feature('POST запросы')
    def test_patch_unauthorized_for(self, module_name):
        with allure.step(f'Отправляю PATCH запрос без авторизации на {self.data[module_name]["url"]}'):
            response = self.request.patch(self.data[module_name]['url'], self.data[module_name]['request'])
        with allure.step('Проверяю что пришел статус 404 и тело ответа соответствует схеме JSON'):
            self.assertion.correct_response(response, 401, self.error)

    @allure.feature('PATCH запросы')
    @pytest.mark.usefixtures('authorization')
    def test_patch_incorrect_id_for(self, module_name):
        with allure.step(f'Отправляю PATCH запрос c неправильным ID на {self.data[module_name]["url"]}'):
            id_list = {"id": self.request_data.incorrect_id()}
            response = self.request.patch(self.data[module_name]['url'], [id_list], cookies=pytest.auth_cookie)
        with allure.step('Проверяю что пришел статус 404 и тело ответа соответствует схеме JSON'):
            self.assertion.correct_response(response, 404, self.error)

    @allure.feature('DELETE запросы')
    def test_delete_unauthorized_for(self, module_name):
        with allure.step(f'Отправляю DELETE запрос без авторизации на {self.data[module_name]["url"]}'):
            response = self.request.delete(self.data[module_name]['url'], self.data[module_name]['request'])
        with allure.step('Проверяю что пришел статус 401 и тело ответа соответствует схеме JSON'):
            self.assertion.correct_response(response, 401)

    @allure.feature('DELETE запросы')
    @pytest.mark.usefixtures('authorization')
    def test_delete_incorrect_id_for(self, module_name):
        with allure.step(f'Отправляю DELETE запрос c неправильным ID на {self.data[module_name]["url"]}'):
            response = self.request.delete(self.data[module_name]['url'], [self.request_data.incorrect_id()],
                                           cookies=pytest.auth_cookie)
        with allure.step('Проверяю что пришел статус 404 и тело ответа соответствует схеме JSON'):
            self.assertion.correct_response(response, 404, self.error)


@allure.epic('Content module')
@allure.suite('Content negative')
@allure.tag('negative', 'api', 'content')
@allure.label("owner", "Murat Kubekov")
class TestContentsFilesNeg(BaseCase):
    data = ContentModuleData.get_file_data()
    request = MyRequests()
    assertion = Assertions()
    error = schema

    @allure.feature('POST запросы')
    def test_post_unauthorized_for_files(self):
        with allure.step(f'Отправляю POST запрос без авторизации на {self.data["files"]["url"]}'):
            response = self.request.post(self.data['files']['url'], files=self.data['files']['request'])
        with allure.step('Проверяю что пришел статус 401 и тело ответа соответствует схеме JSON'):
            self.assertion.correct_response(response, 401)

    @allure.feature('PATCH запросы')
    @pytest.mark.usefixtures('authorization')
    def test_patch_incorrect_id_for_files(self):
        with allure.step(f'Отправляю PATCH запрос c неправильным ID на {self.data["files"]["url"]}'):
            response = self.request.patch(f'{self.data["files"]["url"]}/000', cookies=pytest.auth_cookie)
        with allure.step('Проверяю что пришел статус 404 и тело ответа соответствует схеме JSON'):
            self.assertion.correct_response(response, 404)

    @allure.feature('DELETE запросы')
    @pytest.mark.usefixtures('authorization')
    def test_delete_incorrect_id_for_files(self):
        with allure.step(f'Отправляю DELETE запрос c неправильным ID на {self.data["files"]["url"]}'):
            response = self.request.delete(f'{self.data["files"]["url"]}/000', cookies=pytest.auth_cookie)
        with allure.step('Проверяю что пришел статус 404 и тело ответа соответствует схеме JSON'):
            self.assertion.correct_response(response, 404, self.error)
