FROM openjdk

COPY ./utils/notifications ./utils/notifications
COPY ./allure-report ./allure-report

CMD java "-DconfigFile=notifications/telegram-config.json" -jar utils/notifications/allure-notifications-4.2.1.jar
