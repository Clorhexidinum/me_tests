import allure
from selene.support.conditions import have, be
from selene.support.shared import browser


class Assertions:
    def visible(self):
        with allure.step(f'Проверить что появился попап'):
            assert browser.element('.popup-content').should(be.visible)
        return self


