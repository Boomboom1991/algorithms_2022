"""
Задание 2.

Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""

# Импортируем библиотеку, соответствующую типу нашей базы данных
# from getpass import getpass
# import pymysql
import hashlib
import mysql.connector

# DROP DATABASE IF EXISTS algo2020;
# CREATE DATABASE IF NOT EXISTS algo2020;
#
# USE algo2020;
#
# CREATE TABLE users(
# 	id BIGINT NOT NULL AUTO_INCREMENT,
# 	user_name VARCHAR(150) NOT NULL UNIQUE,
# 	user_password VARCHAR(150) NOT NULL,
#     PRIMARY KEY (id)
# );


connection = mysql.connector.connect(host='localhost',
                                     user='root',
                                     password='12341234',
                                     database='algo2020')
cursor = connection.cursor()


def create_user():
    name = input("Введите логин: ")
    password = input("Введите пароль: ")
    hash_pass = hashlib.sha256(name.encode() + password.encode()).hexdigest()
    insert_user = "INSERT INTO users (user_name, user_password)" \
                  "VALUES ('{}','{}')".format(name, hash_pass)
    # 0d2e56b00e478e2a0795c56ce25ad636f774fdc1d5814e68d8db9eca59356790
    cursor.execute(insert_user)
    connection.commit()
    print("В базе данных хранится строка: {} ".format(hash_pass))
    return name


def check_password(login):
    password = input(f"Введите снова пароль для {login}: ")
    hash_pass = hashlib.sha256(login.encode() + password.encode()).hexdigest()
    check_hash = "SELECT user_password " \
                 "FROM users WHERE user_name = '{}'".format(login)
    cursor.execute(check_hash)
    if hash_pass == cursor.fetchone()[0]:
        print("Вы ввели правильный пароль")
    else:
        print("Неверный пароль")


if __name__ == "__main__":
    login = create_user()
    check_password(login)
