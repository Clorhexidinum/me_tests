<h1 align="center">Проект по тестированию страницы сайта <a href="https://maximumtest.ru/" target="_blank">Поставить логотип</a> 

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


## :heavy_check_mark: Описание
В UI части автоматизирована проверка меню сайта Maximum Education, а также отображение попапа и изменения города. Использован паттерн проектирования автотестов PageObject.
В проверках API реализована проверка статусов и структуры ответов на соответствие схеме JSON.
  
## :heavy_check_mark: Что проверяем

> - Выбор города;
> - Открытие попапа в хедере;
> - Переход на предметные страницы;
> - Изменение заголовка первого экрана в зависимости от региона;
> - Открывание попапа на первом экране.

## <img width="5%" title="Jenkins" src="img/logo/Jenkins.svg"> Запуск тестов из [Jenkins](https://jenkins.autotests.cloud/job/002_Clorhexidinum_diploma_python/)
  
  Для запуска тестов из Jenkins

  1. Необходимо нажать кнопку "Собрать с параметрами".
  2. Выбрать параметры.
  3. Нажать кнопку "Собрать"
  
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
  
### <img width="3%" title="Allure" src="img/logo/Allure.svg"> Allure

После прохождения тестов формируется отчет в [Allure report](https://jenkins.autotests.cloud/job/002_Clorhexidinum_diploma_python/8/allure/)

<img src="img/screen/Bot.jpg" alt="Allure"/>
  

### <img width="3%" title="Telegram" src="img/logo/Telegram.svg"> Telegram

И отправляется краткий отчет в Telegram

<img src="img/screen/Bot.jpg" alt="Telegram"/>
  
## :movie_camera: Тестовые артефакты

В результате прохождения тестов собираются следующие артефакты:

- Скриншот страницы

- Логи браузера
  
- Dump страницы
  
- Видео прохождения

<p align="center">
  <img title="Video" src="img/gif/test.gif">
</p>

## <img width="3%" title="Allure" src="img/logo/Allure_TO.svg"> Проект интегрирован с Allure TestOps


## <img width="3%" title="JIRA" src="img/logo/"> Результаты выполнения тестов интегрированы с Atlassian Jira
  
  


  
  
