'''
1) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена самых молодых.
б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
в) Посчитать среднее количество лет всех людей из списка.


persons = [
         {"name": "John", "age": 15},
         {"name": "Sam", "age": 10},
         {"name": "Michael", "age": 47},
         {"name": "Mal", "age": 12},
         {"name": "Jack", "age": 45}
]
'''

persons = [
         {"name": "John", "age": 10},
         {"name": "Sam", "age": 10},
         {"name": "Michael", "age": 43},
         {"name": "Mal", "age": 12},
         {"name": "Jack", "age": 45}
]
age_persons = [person['age'] for person in persons]
young_persons = [person['name'] for person in persons if person['age'] == min(age_persons)]
print('Имя самого молодого человека:', young_persons)

name_persons = [len(person['name']) for person in persons]
max_name_persons = [person['name'] for person in persons if len(person['name']) == max(name_persons)]
print('Самое длинное имя:', max_name_persons)

middle_age = sum(age_persons) // len(age_persons)
print('Средний возраст:', middle_age)

'''
2. Написать функцию которой передается два параметра - две строки.
Функция возвращает список в который поместить те символы,
которые есть в обеих строках хотя бы раз.
'''

def create_list(str_1, str_2):
    res_list = [symbol for symbol in set(str_1) if symbol in set(str_2)]
    return res_list


print(create_list(str_1="we met no one yesterday", str_2="we didn’t meet anyone yesterday"))


'''
3. Написать функцию которой передается два параметра - две строки.
Функция возвращает список в который поместить те символы, которые есть в обеих строках,
но в каждой только по одному разу.
'''

def create_list(str_1, str_2):
    res_list = [symbol for symbol in str_1 if str_1.count(symbol) == 1 and str_2.count(symbol) == 1]
    return res_list


print(create_list(str_1="we met no one yesterday", str_2="we didn’t meet anyone yesterday"))

'''
4. Даны списки names и domains (создать самостоятельно).
Написать функцию для генерирования e-mail в формате:
фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
Строку и число генерировать случайным образом.

Пример использования функции:
names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]
e_mail = create_email(domains, names)
print(e_mail)
>>>miller.249@sgdyyur.com
'''

import random
import string

def create_email(ls_1, ls_2):
    return random.choice(ls_2) + '.' + str(random.randint(100, 999)) + '@' + \
           ''.join(random.choice(string.ascii_lowercase) for _ in range(0, random.randint(5, 7))) + \
           '.' + random.choice(ls_1)


names = ["tourist", "flight", "stitch", "lobster"]
domains = ["ru", "gov", "dp.ua", "edu", "info"]
e_mail = create_email(domains, names)
print(e_mail)