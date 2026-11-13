import json
from urllib.error import HTTPError, URLError
from urllib.request import urlopen


POSTS_URL = "https://jsonplaceholder.typicode.com/posts"


def main():
    try:
        # urlopen отправляет GET-запрос, когда тело запроса не задано.
        with urlopen(POSTS_URL, timeout=10) as response:
            posts = json.load(response)
    except HTTPError as error:
        raise SystemExit(f"JSONPlaceholder вернул ошибку HTTP {error.code}.")
    except (URLError, TimeoutError):
        raise SystemExit("Не удалось подключиться к JSONPlaceholder.")
    except json.JSONDecodeError:
        raise SystemExit("JSONPlaceholder вернул некорректный JSON.")

    for number, post in enumerate(posts[:5], start=1):
        print(f"{number}. {post['title']}")
        print(post["body"])
        print()


if __name__ == "__main__":
    main()
