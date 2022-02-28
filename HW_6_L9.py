import os
'''
1. В текстовом файле построчно извлечены имена и имена владельцев классов и их оценки.
    Вывести на экран всех учащихся, чей средний балл меньше 5, а также посчитать и получить низкий балл по классу. Так же,
    Записать в новый файл учащихся в формате "Фамилия И. Ср. балл":
    Выравнивание колонок - желательно!
'''

def short_name(full_name):
    return f"{full_name[1]} {full_name[0][0]}."


def average_rating(rating):
    return sum(rating) / len(rating)


def print_dict(_dict, rating=10):
    return [f"{key}".ljust(20) + f"{value}\n" for key, value in _dict.items() if value < rating]


def create_report_from_file(path):
    info = {}

    with open(path, encoding='utf-8') as f:
        for item in f.readlines():
            _key = short_name([x for x in item.split() if x.isalpha()])

            _value = average_rating([int(x)
                                     for x in item.split() if x.isdigit()])

            info[_key] = round(_value, 2)
    return info


def report_in_file(path, _dict):
    with open(path, 'w', encoding='utf-8') as f:
        for item in print_dict(_dict):
            f.write(item)


_report = create_report_from_file(r"file.txt")
print(f"Учащиеся, чей средний балл меньше 5 :\n{''.join(print_dict(_report, 5))}")
print(f"Cредний балл по классу :{round(average_rating(_report.values()), 2)}")
report_in_file(r"result.txt", _report)


'''
2. Создать текстовый файл, сохраняет в нем построчно данные, которые вводит пользователь. Окончание ввода пусть служителей
пустая строка. Каждая введенная строка, в файле, должна начинаться с новой строки.
'''

def user_info():
    while True:
        res = input('Введите текст: ')
        with open('input.txt', 'a') as new_file:
            new_file.writelines(res + '\n')
        if not res:
            break
    return


user_info()

