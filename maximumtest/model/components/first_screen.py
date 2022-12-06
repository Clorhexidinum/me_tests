import allure
from selene.support.conditions import have, be
from selene.support.shared import browser


class FirstScreen:
    def click_btn(self, value):
        with allure.step(f'Кликнуть на кнопку с текстом {value} на первом экране'):
            browser.all('.future__buttons-button').by(have.text(value)).first.click()
        return self
