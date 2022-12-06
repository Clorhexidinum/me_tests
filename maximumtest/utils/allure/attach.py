import json
import allure
import curlify
from allure import attachment_type
from requests import Response
import datetime

from selene.support.shared import browser


class Attachments:
    @staticmethod
    def curl(response: Response):
        curl_message = curlify.to_curl(response.request)
        allure.attach(body=f"{datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')}\n{curl_message.encode('utf8')}",
                      name="Curl", attachment_type=attachment_type.TEXT, extension='txt')

    @staticmethod
    def headers(response: Response):
        allure.attach(body=json.dumps(str(response.headers), indent=4, ensure_ascii=False).encode('utf8'),
                      name="Headers", attachment_type=attachment_type.TEXT, extension='txt')

    @staticmethod
    def json(response: Response):
        try:
            allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=False).encode('utf8'),
                          name="Response", attachment_type=attachment_type.JSON, extension='json')
        except ValueError as error:
            allure.attach(body=response.text.encode('utf8'),
                          name="Response", attachment_type=attachment_type.TEXT, extension='txt')

    @staticmethod
    def body(url: str, data: dict):
        if url != 'auth/logout':
            allure.attach(body=json.dumps(data, indent=4, ensure_ascii=False).encode('utf8'),
                          name="Body", attachment_type=attachment_type.JSON, extension='json')
        else:
            pass

    @staticmethod
    def screenshot(*, name='screenshot'):
        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG,
        )

    @staticmethod
    def logs(*, name='browser_logs'):
        log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
        allure.attach(log, name=name, attachment_type=allure.attachment_type.TEXT)

    @staticmethod
    def xml_dump(*, name='page xml dump'):
        allure.attach(
            browser.driver.page_source,
            name=name,
            attachment_type=allure.attachment_type.XML,
        )

    @staticmethod
    def html_dump(*, name='page html dump'):
        allure.attach(
            browser.driver.page_source,
            name=name,
            attachment_type=allure.attachment_type.HTML,
        )

    @staticmethod
    def video():
        video_url = "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
        html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
               + video_url \
               + "' type='video/mp4'></video></body></html>"
        allure.attach(html, 'video_' + browser.driver.session_id, attachment_type=allure.attachment_type.HTML)

