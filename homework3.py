##### ДЗ 3 #####
##### Задача 1 #####

# def text_converter():
#     text = str(input())
#     snake_case = ''
#     if text.count('_') > 0:
#         text = text.title().replace('_', '')
#         print(text)
#     else:
#         for i in text:
#             if i.isupper() == True:
#                 snake_case += '_'
#             snake_case += i.lower()
#     print(snake_case.replace('_', '',1))
#
# text_converter()


##### Задача 2 #####


# def is_leap(year: int) -> bool:
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# def date_check(date: str) -> bool:
#     if len(list_date := date.split(".")) != 3:
#         return False
#     day, month, year = map(int, list_date)
#     months = {
#         1: 31,
#         2: 29 if is_leap(year) else 28,
#         3: 31, 4: 30, 5: 31, 6: 30, 7: 31,
#         8: 31, 9: 30, 10: 31, 11: 30, 12: 31,
#     }
#     return year > 0 and month in months and 1 <= day <= months[month]

# print(date_check('30.02.2023'))


##### Задача 3 #####
#
# from math import sqrt
#
# def prime(num: int) -> bool:
#     if num == 2:
#         return True
#     if num in (0, 1) and not num % 2:
#         return False
#     for dev in range(3, int(sqrt(num)) + 1):
#         if not num % dev:
#             return False
#     return True
#
#
# print(prime(23))


#### Задача 4 #####

# def data_card():
#     users_data = dict()
#     while data := input().split():
#         name, surname, age, identificator = data
#         if name.isalpha() == True and surname.isalpha() == True and 18 < int(age) < 60:
#             value = name.capitalize(), surname.capitalize(), age
#             users_data.setdefault(identificator.zfill(8), value)
#             print('Добавлено')
#         else:
#             print("Ошибка, введены некорректные данные")
#     # print(users_data)
#     return users_data
# def table_output(users_data: object) -> object:
#     print('ID        | Имя      | Фамилия  | Возраст')
#     print('_________________________________________')
#     for key in users_data.keys():
#         print(f'{key: <10} {users_data[key][0]: <10} {users_data[key][1]: <10} {users_data[key][2]: <10}')
#
#
# table_output(data_card())