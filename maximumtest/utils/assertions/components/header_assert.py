import allure
from selene.support.conditions import have
from selene.support.shared import browser


class Assertions:
    def city_btn_text(self, value):
        with allure.step(f'Проверить что выбранный город {value}'):
            assert browser.element('.header-layout__city').should(have.text(value))
        return self

    def url(self, value):
        with allure.step(f'Проверить что url {value}'):
            assert browser.should(have.url(f'https://maximumtest.ru/{value}'))
        return self

