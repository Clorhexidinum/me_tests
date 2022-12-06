import os

import allure
import pytest
from selene.support.shared import browser
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from maximumtest.utils.allure.attach import Attachments as attach


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0',
    )
    parser.addoption(
        '--browser_name',
        default='chrome',
    )
    parser.addoption(
        '--window_size',
        default='1920x1080',
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    browser_name = request.config.getoption('--browser_name')
    browser_version = request.config.getoption('--browser_version')
    window_size = request.config.getoption('--window_size')

    options = Options()
    options.capabilities.update({
        "browserName": browser_name,
        "browserVersion": browser_version,
        "pageLoadStrategy": 'eager',
        "selenoid:options": {
            "screenResolution": f"{window_size}x24",
            "enableVNC": True,
            "enableVideo": True
        }
    })

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver
    browser.config.base_url = 'https://maximumtest.ru/'
    browser.config.timeout = 4.0
    with allure.step(f'Открыть главную страницу'):
        browser.open_url('')

    yield browser

    attach.screenshot()
    attach.logs()
    attach.html_dump()
    attach.video()
    browser.close()
