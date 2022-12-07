<h1 align="center">Проект по тестированию страницы сайта <a href="https://maximumtest.ru/" target="_blank"><img src="/README/icons/ME.png" alt="Logo"/></a> 

## :open_book: Содержание:
- [Технологии и инструменты](#gear-проект-реализован-с-использованием)
- [Что проверяем](#heavy_check_mark-описание)
- [Запуск тестов из Jenkins](#-запуск-тестов-из-jenkins)
- [Запуск тестов из терминала](#computer-запуск-тестов-из-терминала)
- [Отчеты](#bar_chart-отчеты-о-прохождении-тестов)
  - [Allure](#-allure)
  - [Telegram](#-telegram)
- [Тестовые артефакты](#movie_camera-тестовые-артефакты)
- [Allure TestOps](#-проект-интегрирован-с-allure-testops)
- [Atlassian Jira](#-результаты-выполнения-тестов-интегрированы-с-atlassian-jira)

## :gear: Проект реализован с использованием
  <p align="center">
    <img src="/README/icons/python.svg" width="50" height="50"  alt="python"/>
    <img src="/README/icons/pycharm.svg" width="50" height="50"  alt="pycharm"/>
    <img src="/README/icons/pytest.svg" width="50" height="50"  alt="pytest"/>
    <img src="/README/icons/selene.png" width="50" height="50"  alt="selene"/>
    <img src="/README/icons/requsests.png" width="50" height="50"  alt="requsests"/>
    <img src="/README/icons/json.svg" width="50" height="50"  alt="json schema"/>
    <img src="/README/icons/selenoid.svg" width="50" height="50"  alt="selenoid"/>
    <img src="/README/icons/jenkins.svg" width="50" height="50"  alt="jenkins"/>
    <img src="/README/icons/allure.svg" width="50" height="50"  alt="allure"/>
    <img src="/README/icons/testops.svg" width="50" height="50"  alt="testops"/>
    <img src="/README/icons/github.svg" width="50" height="50"  alt="github"/>
    <img src="/README/icons/telegram.svg" width="50" height="50"  alt="telegram"/>
    <img src="/README/icons/jira.svg" width="50" height="50"  alt="jira"/>
 </p>


## :heavy_check_mark: Описание
В UI части автоматизирована проверка меню сайта Maximum Education, а также отображение попапа и изменения города. Использован паттерн проектирования автотестов PageObject.
В проверках API реализована проверка статусов и структуры ответов на соответствие схеме JSON.
  
## :heavy_check_mark: Что проверяем

> - Выбор города;
> - Открытие попапа в хедере;
> - Переход на предметные страницы;
> - Изменение заголовка первого экрана в зависимости от региона;
> - Открывание попапа на первом экране.

## <img src="/README/icons/jenkins.svg" width="50" height="50"  alt="jenkins"/> Запуск тестов из [Jenkins](https://jenkins.autotests.cloud/job/002_Clorhexidinum_diploma_python/)
  
  Для запуска тестов из Jenkins

  <details><summary>1. Необходимо нажать кнопку "Собрать с параметрами".</summary>
  <p align="center">
    <img src="/README/jenkins.png" alt="jenkins"/>
  </p>
  </details>
  
  <details><summary>2. Выбрать параметры.</summary>
  <p align="center">
    <img src="/README/jenkins2.png" alt="jenkins"/>
  </p>
  </details>
  
  <details><summary>3. Нажать кнопку "Собрать"</summary>
  <p align="center">
    <img src="/README/jenkins2.png" alt="jenkins2"/>
  </p>
  </details>
  
  ### :heavy_plus_sign: Параметры сборки

> - test_folder - выбор тестовой папки
> - browser_name - название браузера
> - browser_version - версия браузера
> - window_size - размер окна браузера
  
## :computer: Запуск тестов из терминала

Для локального запуска необходимо выполнить команду:
```
pytest *test_folder*
```
  
## :bar_chart: Отчеты о прохождении тестов 
  
### <img src="/README/icons/allure.svg" width="50" height="50"  alt="allure"/> Allure

После прохождения тестов формируется отчет в [Allure report](https://jenkins.autotests.cloud/job/002_Clorhexidinum_diploma_python/8/allure/)
  <p align="center">
    <img src="/README/report1.png" height="195" alt="allure"/>
    <img src="/README/report3.png" height="195" alt="allure"/>
    <img src="/README/report4.png" height="195" alt="allure"/>
  </p>
  


  

### <img src="/README/icons/telegram.svg" width="50" height="50"  alt="telegram"/> Telegram

И отправляется краткий отчет в Telegram

<img src="/README/notify.png" height="250" alt="notify"/>
  
## :movie_camera: Тестовые артефакты

В результате прохождения тестов собираются следующие артефакты:
  
   ### UI
  <details><summary>Скриншот страницы</summary>
  <p align="center">
    <img src="/README/screenshot.png" alt="screenshot"/>
  </p>
  </details>
  
  <details><summary>Логи браузера</summary>
  <p align="center">
    <img src="/README/logs.png" alt="logs"/>
  </p>
  </details>
  
  <details><summary>Дамп страницы</summary>
  <p align="center">
    <img src="/README/dump.png" alt="dump"/>
  </p>
  </details>
  
  <details><summary>Видео прохождения</summary>
  <p align="center">
    <img src="/README/selenoid.gif" alt="video"/>
  </p>
  </details>

  ### API

  <details><summary>Curl</summary>
  <p align="center">
    <img src="/README/curl.png" alt="curl"/>
  </p>
  </details>

  <details><summary>Headers</summary>
  <p align="center">
    <img src="/README/headers.png" alt="headers"/>
  </p>
  </details>

  <details><summary>Body</summary>
  <p align="center">
    <img src="/README/response.png" alt="png"/>
  </p>
  </details>
  

## <img src="/README/icons/testops.svg" width="50" height="50"  alt="testops"/> Проект интегрирован с Allure TestOps
  <p align="center">
    <img src="/README/test_ops2.png" height="250" alt="allure"/>
    <img src="/README/test_ops.png" height="250" alt="allure"/>
  </p>


## <img src="/README/icons/jira.svg" width="50" height="50"  alt="jira"/> Результаты выполнения тестов интегрированы с Atlassian Jira
  
  <img src="/README/jira.png" height="250" alt="jira"/>
  
  


  
  
