# Работа с API на Python

Два скрипта для практики GET-запросов, передачи параметров и обработки JSON.

## 1. Первые пять постов

[`zadanie1.py`](zadanie1.py) отправляет GET-запрос к `/posts` и выводит заголовки и тексты первых пяти постов. [Документация JSONPlaceholder](https://jsonplaceholder.typicode.com/guide/)

```powershell
py zadanie1.py
```

## 2. Текущая погода по городу

[`zadanie2.py`](zadanie2.py) запрашивает название города, получает его координаты и выводит текущую температуру в °C и описание погоды на русском. [Геокодирование OpenWeather](https://openweathermap.org/api/geocoding-api) · [API текущей погоды](https://openweathermap.org/api/current)

```powershell
py zadanie2.py
```

Введи название города, например `Moscow,RU`. Затем вставь API-ключ и нажми Enter. При вводе ключа символы скрыты. Для обоих запросов подходит бесплатный ключ. [Ключи OpenWeather](https://home.openweathermap.org/api_keys) · [Бесплатный доступ](https://openweathermap.org/price)

В PyCharm для скрытого ввода запускай скрипт во вкладке **Terminal**. Для запуска кнопкой **Run** добавь `OPENWEATHER_API_KEY` в **Run → Edit Configurations → Environment variables**. Скрипт прочитает ключ из переменной окружения. Храни ключ вне репозитория. [Настройки запуска PyCharm](https://www.jetbrains.com/help/pycharm/run-debug-configuration-python.html)

Оба скрипта запускаются из папки репозитория на Python 3. Дополнительные библиотеки устанавливать не нужно.
