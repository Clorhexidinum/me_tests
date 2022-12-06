FROM python

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY ./tests ./tests
COPY ./base ./base

RUN ls -la 

CMD pytest --alluredir="./allure-results" && ls -la ./allure-results
