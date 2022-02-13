"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет.

Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}

Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""

import hashlib
import string
import secrets

url_bd = {'vk.com': '1ff232f32',
          'facebook.com': 'f12f12f1',
          'dodo.ru': 'somehash'}


def crypto_salt():
    return ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(5))


def cash_url(url):
    return hashlib.sha512(url.encode() + crypto_salt().encode()).hexdigest()


def main():
    url = input("Введите URl: ")
    if url_bd.get(url) is not None:
        print("Хеш данного URL: ", url_bd.get(url))
    else:
        url_bd.setdefault(url, cash_url(url))
    print(url_bd)


if __name__ == "__main__":
    main()
