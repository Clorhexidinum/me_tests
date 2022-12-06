import allure
from selene.support.conditions import have, be
from selene.support.shared import browser


class Header:
    def open(self):
        browser.open('')
        return self

    def click_logo(self):
        with allure.step('Кликнуть на логотип в хедере'):
            browser.element('.header-layout__logo').click()
        return self

    def open_city_list(self):
        with allure.step('Открыть список городов'):
            browser.element('.header-city-v2__btn').click()
        return self

    def select_city(self, value: str):
        if not browser.element('.countries').matching(be.visible):
            self.open_city_list()

        with allure.step(f'Выбрать город {value}'):
            browser.all('.city-name').by(have.text(value.capitalize())).first.click()
        return self

    def open_popup(self):
        with allure.step('Кликнуть на кнопку в хедере'):
            browser.element('.header-layout__top-btn').click()
        return self

    def open_category(self, value):
        with allure.step(f'В меню выбрать категорию {value}'):
            browser.all('.desktop-menu__category-item').by(have.text(value)).first.hover()
        return self

    def click_category(self, value):
        with allure.step(f'Кликнуть на категорию {value}'):
            browser.all('.desktop-menu__category-item').by(have.text(value)).first.click()
        return self

    def select_subcategory(self, value):
        with allure.step(f'Выбрать подкатегорию {value}'):
            browser.all('.desktop-menu__link-item').by(have.text(value)).first.click()
        return self

    def open_promo(self, value):
        with allure.step(f'Выбрать промо {value}'):
            browser.all('.desktop-menu__promo').by(have.text(value)).first.click()
        return self

    def open_banner(self):
        with allure.step(f'Кликнуть на баннер'):
            browser.element('.desktop-menu__banner').click()
        return self
