import allure
from selene.support.conditions import have, be
from selene.support.shared import browser


class Assertions:
    def promo_title(self, value):
        with allure.step(f'Проверить заголовок'):
            assert browser.element('.promo__title').should(have.text(value))
        return self

    def info_title(self, value):
        with allure.step(f'Проверить заголовок'):
            assert browser.element('.intro__info-title').should(have.text(value))
        return self

    def breadcrumbs(self, value):
        with allure.step(f'Проверить последний элемент хлебных крошек'):
            assert browser.elements('.breadcrumbs__item')[-1].should(have.text(value))
        return self

