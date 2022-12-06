FROM frankescobar/allure-docker-service

COPY ./allure-results ./allure-results

RUN allure generate -c ./allure-results -o /app/allure-docker-api/static/projects/default/reports/latest