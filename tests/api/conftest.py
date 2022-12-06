import pytest
from maximumtest.utils.requests import MyRequests
from maximumtest.utils.requests.request_data import RequestData
import allure


@pytest.fixture(scope='function')
def authorization():
    data = RequestData.user_auth()
    with allure.step('Отправляем запрос на авторизацию'):
        response = MyRequests.post(data["login_url"], data["request"])
        pytest.auth_cookie = {"Authentication": response.cookies['Authentication']}
        pytest.refresh_cookie = {"Refresh": response.cookies['Refresh']}

    yield

    with allure.step('Отправляем запрос на логаут'):
        MyRequests.post(data["logout_url"], cookies=pytest.auth_cookie)


def pytest_runtest_call(item: pytest.Item):
    allure.dynamic.title(" ".join(item.name.split("_")[1:]).capitalize())
