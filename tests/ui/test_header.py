import allure
import pytest

from maximumtest.model.components import header_block, first_screen
from maximumtest.utils.assertions.components import first_screen_assert
from maximumtest.utils.assertions.components import header_assert, popup_leadform

header = header_block.Header()
header_assert = header_assert.Assertions()
popup = popup_leadform.Assertions()
first_screen = first_screen.FirstScreen()
first_screen_assert = first_screen_assert.Assertions()


@allure.epic('Header')
@allure.suite('Content positive')
@allure.tag('positive', 'header', 'nav')
@allure.label("owner", "Murat Kubekov")
@allure.title('Выбор города')
def test_change_city():
    header.select_city("Москва")

    header_assert.city_btn_text("Москва")


@allure.epic('Header')
@allure.suite('Content positive')
@allure.tag('positive', 'header', 'nav')
@allure.label("owner", "Murat Kubekov")
@allure.title('Выбор города')
@pytest.mark.parametrize("value", ["Москва", "Абакан", "Белгород"])
def test_change_city(value):
    header.select_city(value)

    header_assert.city_btn_text(value)


@allure.epic('Header')
@allure.suite('Content positive')
@allure.tag('positive', 'header', 'nav')
@allure.title('Открытие попапа в хедере')
@allure.label("owner", "Murat Kubekov")
def test_open_popup_in_header():
    header.open_popup()

    popup.visible()


@allure.epic('Header')
@allure.suite('Content positive')
@allure.tag('positive', 'header', 'nav')
@allure.title('Открытие страницы из меню хедера')
@allure.label("owner", "Murat Kubekov")
def test_opening_page_from_the_opened_menu():
    header \
        .open_category('ЕГЭ') \
        .select_subcategory('Математика')

    first_screen_assert \
        .breadcrumbs('Математика') \
        .info_title(f'Сдайте ЕГЭ по математике и поступите на бюджет')


@allure.epic('Header')
@allure.suite('Content positive')
@allure.tag('positive', 'header', 'nav')
@allure.label("owner", "Murat Kubekov")
@allure.title('Открытие региональной страницы из меню хедера')
@pytest.mark.parametrize("value", ["Балашиха", "Архангельск", "Белгород"])
def test_opening_regional_page_from_the_opened_menu(value):
    header \
        .select_city(value) \
        .open_category('ЕГЭ') \
        .select_subcategory('Русский язык')

    first_screen_assert \
        .info_title(f'Сдайте ЕГЭ в г. {value} и поступите на бюджет без стресса')


@allure.epic('Header')
@allure.suite('Content positive')
@allure.tag('positive', 'header', 'nav')
@allure.title('Открытие страницы при клике на элемент меню')
@allure.label("owner", "Murat Kubekov")
def test_opening_page_from_the_menu():
    header \
        .click_category('Профориентация')

    first_screen_assert \
        .promo_title(f'Бесплатная профориентация')


@allure.epic('Header')
@allure.suite('Content positive')
@allure.tag('positive', 'header', 'nav')
@allure.title('Открытие промо страницы из меню хедера')
@allure.label("owner", "Murat Kubekov")
def test_opening_promo_from_the_menu():
    header \
        .open_category('5-8 класс') \
        .open_promo('Помощь с домашними заданиями для 5-9 классов')

    first_screen_assert \
        .breadcrumbs('Домашнее задание') \
        .promo_title('Помощь с домашними заданиями')


@allure.epic('Header')
@allure.suite('Content positive')
@allure.tag('positive', 'header', 'nav')
@allure.title('Открытие попапа с первого экрана')
@allure.label("owner", "Murat Kubekov")
def test_opening_popup_on_the_first_screen():
    header \
        .open_category('ОГЭ') \
        .select_subcategory('Курс на вуз')

    first_screen_assert \
        .promo_title('Курс на вуз')

    first_screen.click_btn('Получить курс')

    popup.visible()
