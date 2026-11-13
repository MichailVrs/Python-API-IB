import json
import os
import sys
from getpass import getpass
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import urlopen


OPENWEATHER_URL = "https://api.openweathermap.org"


def get_json(path, params, *, stage):
    # urlencode кодирует пробелы, кириллицу и другие символы в параметрах.
    url = f"{OPENWEATHER_URL}{path}?{urlencode(params)}"
    print(f"{stage}…", file=sys.stderr, flush=True)
    try:
        with urlopen(url, timeout=10) as response:
            return json.load(response)
    except HTTPError as error:
        if error.code == 401:
            raise SystemExit(f"{stage} — OpenWeather отклонил ключ (HTTP 401). Проверьте ключ и его активацию.")
        raise SystemExit(f"{stage} — OpenWeather вернул ошибку HTTP {error.code}.")
    except (URLError, TimeoutError) as error:
        reason = error.reason if isinstance(error, URLError) else error
        if isinstance(reason, TimeoutError):
            raise SystemExit(f"{stage} — истекло время ожидания ответа от OpenWeather.")
        raise SystemExit(f"{stage} — не удалось подключиться к api.openweathermap.org.")
    except json.JSONDecodeError:
        raise SystemExit(f"{stage} — OpenWeather вернул некорректный JSON.")


def main():
    city = input("Введите название города: ").strip()
    if not city:
        raise SystemExit("Введите непустое название города.")

    api_key = os.getenv("OPENWEATHER_API_KEY", "").strip()
    if not api_key:
        api_key = getpass("Введите API-ключ OpenWeather (символы скрыты) и нажмите Enter: ").strip()
    if not api_key:
        raise SystemExit("Для запроса нужен API-ключ OpenWeather.")

    locations = get_json("/geo/1.0/direct", {
        "q": city,
        "limit": 1,
        "appid": api_key,
    }, stage="Поиск города")
    if not locations:
        raise SystemExit(f"Город «{city}» не найден. Проверьте название.")

    location = locations[0]
    weather = get_json("/data/2.5/weather", {
        "lat": location["lat"],
        "lon": location["lon"],
        "appid": api_key,
        "units": "metric",
        "lang": "ru",
    }, stage="Запрос погоды")

    name = location.get("local_names", {}).get("ru", location["name"])
    country = location["country"]
    temperature = weather["main"]["temp"]
    description = weather["weather"][0]["description"]
    print(f"{name} ({country}) — {temperature} °C, {description}")


if __name__ == "__main__":
    main()
