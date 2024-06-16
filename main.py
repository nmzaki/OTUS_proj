##### ДЗ 1 #####
##### Задача 1 #####
##### Вариант 1 #####

# figure = int(input('Введите пятизначное число \n'))
# if len(str(figure)) > 5:
#     print('Введено больше 5-ти цифр')
# elif  len(str(figure)) < 5:
#     print('Введено меньше 5-ти цифр')
# sub_fig1 = figure // 10000 * 10000
# sub_fig2 = figure // 1000 % 10 * 1000
# sub_fig3 = figure // 100 % 10 * 100
# sub_fig4 = figure // 10 % 10 * 10
# sub_fig5 = figure % 10
# print(int(sub_fig1 + (sub_fig4 * 100) + sub_fig3 + (sub_fig2 / 100) + sub_fig5))

##### Вариант 2 #####

# figure = str(input('Введите пятизначное число \n'))
# if len(str(figure)) > 5:
#     print('Введено больше 5-ти цифр')
# elif  len(str(figure)) < 5:
#     print('Введено меньше 5-ти цифр')
# new_figure = figure[0] + figure[3] + figure[2] + figure[1] + figure[4]
# print(new_figure)



##### Задача 2 #####

# work_days = int(input('Введите количество дней до ближайшего отпуска \n'))
# weeks = work_days // 7
# if work_days < 5:
#     print('0')
# elif 5 < work_days < 7:
#     print(7 - work_days)
# elif work_days > 7 and (work_days - weeks * 7) < 5:
#     print(weeks * 2)
# else:
#     print((weeks * 2) + (work_days - (weeks * 7) - 5))

##### Задача 3 #####

# length, width, size = (
#     int(input("Введите длинну: ")),
#     int(input("Введите ширину: ")),
#     int(input("Введите размер куска: ")),
# )
# if size % length == 0 or size % width == 0:
#     print(True)
# else:
#     print(False)

##### Задача 4 #####

# ar_num = int(input())
# if ar_num < 4000:
#     thousands = ar_num // 1000
#     houndreds = ar_num // 100 % 10
#     tens = ar_num // 10 % 10
#     units = ar_num % 10
#     if ar_num < 4000:
#         if thousands < 4:
#             rome_thousands = 'M' * thousands
#         elif thousands == 0:
#             rome_thousands = ''
#         else:
#             print('В римской нумерации нет чисел больше 3999!')
#         if houndreds != 0:
#             if houndreds < 4:
#                 rome_houndreds = 'C' * houndreds
#             elif houndreds == 4:
#                 rome_houndreds = 'CD'
#             elif houndreds == 5:
#                 rome_houndreds = 'D'
#             elif houndreds > 5 and houndreds < 9:
#                 rome_houndreds = 'D' + ('C' * (houndreds - 5))
#             elif houndreds == 9:
#                 rome_houndreds = 'CM'
#         else:
#             rome_houndreds = ''
#         if tens != 0:
#             if tens < 4:
#                 rome_tens = 'X' * tens
#             elif tens == 4:
#                 rome_tens = 'XL'
#             elif tens == 5:
#                 rome_tens = 'L'
#             elif tens > 5 and tens < 9:
#                 rome_tens = 'L' + ('X' * (tens - 5))
#             elif tens == 9:
#                 rome_tens = 'XC'
#         else:
#             rome_tens = ''
#         if units != 0:
#             if units < 4:
#                 rome_units = 'I' * units
#             elif units == 4:
#                 rome_units = 'IV'
#             elif units == 5:
#                 rome_units = 'V'
#             elif units > 5 and units < 9:
#                 rome_units = 'V' + ('I' * (units - 5))
#             elif units == 9:
#                 rome_units = 'IX'
#         else:
#             rome_units = ''
#     rome_number = rome_thousands + rome_houndreds + rome_tens + rome_units
#     print(rome_number)
# else:
#     print('В римской нумерации нет чисел больше 3999!')

# Задача 5
# data = input('Введите данные: \n')
# if data.count('.') <= 1 and data.isdigit == True and '.' not in data[-1]:
#     print(f'{float(data)} -> {True}')
# else:
#     print(f'{data} -> {False}')


##### ДЗ 2 #####
##### Задача 1 #####

# number = int(input())
# new_number = 0
# new_new_number = 0
# for i in range(len(str(number))):
#     figure = number // (10 ** i) % 10
#     new_number += figure
# for i in range(len(str(new_number))):
#     figure = new_number // (10 ** i) % 10
#     new_new_number += figure
# print(new_new_number)


##### Задача 2 #####

# bucked_seats = [[0,1,1,0], [1, 0, 0, 0], [0,1,0,0]]
# quantity = int(input())
# for i in range(len(bucked_seats)):
#     # print(bucked_seats[i])
#     for j in range(len(bucked_seats[i])):
#         # print(bucked_seats[i][j])
#         bucked_seats[i][j] = str(bucked_seats[i][j])
#     bucked_seats[i] = ''.join(bucked_seats[i])
# print(bucked_seats)
# for i, row in enumerate(bucked_seats):
#     if '0' * quantity in row:
#         print(i)
#         break

##### Задача 3 #####

# non_rle_str = str(input())
# rle_str = ''
# counter = 1
# for i in range(len(non_rle_str) - 1):
#     if non_rle_str[i] == non_rle_str[i + 1]:
#         counter += 1
#     else:
#         rle_str += f'{counter}{non_rle_str[i]}'
#         counter = 1
# rle_str += f'{counter}{non_rle_str[-1]}'
# print(rle_str)



##### Задача 4 #####

# non_encrypted_line, key = str(input()), int(input())
# encrypted_line = str()
# alphabet_list_lower = ['', 'a', 'b', 'c', 'd', 'e',
#                     'f', 'g', 'h', 'i', 'j',
#                     'k', 'l', 'm', 'n', 'o',
#                     'p', 'q', 'r', 's', 't', 
#                     'u', 'v', 'w', 'x', 'y', 'z']
# alphabet_list_upper = ['', 'A', 'B', 'C', 'D', 'E',
#                     'F', 'G', 'H', 'I', 'J',
#                     'K', 'L', 'M', 'N', 'O',
#                     'P', 'Q', 'R', 'S', 'T', 
#                     'U', 'V', 'W', 'X', 'Y', 'Z']
# for i in non_encrypted_line:
#     if i == ' ':
#         encrypted_line += ' '
#         continue
#     if i in alphabet_list_lower:
#         nel_index = alphabet_list_lower.index(i)                              #nel_index - non_encrypted_line_index
#         if nel_index + key > 26:
#             encrypted_letter = alphabet_list_lower[nel_index + key - 26]
#             encrypted_line += encrypted_letter
#         else:    
#             encrypted_letter = alphabet_list_lower[nel_index + key]
#             encrypted_line += encrypted_letter
#     else:
#         nel_index = alphabet_list_upper.index(i)                              #nel_index - non_encrypted_line_index
#         if nel_index + key > 26:
#             encrypted_letter = alphabet_list_upper[nel_index + key - 26]
#             encrypted_line += encrypted_letter
#         else:    
#             encrypted_letter = alphabet_list_upper[nel_index + key]
#             encrypted_line += encrypted_letter
# print(encrypted_line)


##### Задача 5 #####

# # input_str = str()
# # subject = list(input_str.split()[0])
# # # input_str != ''
# # i = 1
# # print(subject, surname, rating)
# report_card = dict()
# while input_str := input():
#     subject = input_str.split()[0]
#     surname = input_str.split()[1]
#     rating = input_str.split()[2]
#     if subject in report_card:
#         if surname in report_card[subject]:
#             report_card[subject][surname].append[rating]
#         else:
#             report_card[subject][surname] = [rating]
#     else:
#         report_card[subject] = {surname: [rating]}
# for subject in report_card.items():
#     print(subject)
#     for surname, rating in student.items():
#         print(surname, rating)
#     # report_card[i] = subject, surname, rating
#     # i += 1
# # print(report_card)


# dict_data = {}
# while data := input().split():
#     subj, name, mark = data
#     if subj in dict_data:
#         if name in dict_data[subj]:
#             dict_data[subj][name].append(mark)
#         else:
#             dict_data[subj][name] = [mark]
#     else:
#         dict_data[subj] = {name: [mark]}
#     print(data)
# for subj, student in dict_data.items():
#     print(subj)
#     for name, marks in student.items():
#         print(name, marks)
#
# print(dict_data)


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

# from math import sqrt

# def prime(num: int) -> bool:
#     if num == 2:
#         return True
#     if num in (0, 1) and not num % 2:
#         return False
#     for dev in range(3, int(sqrt(num)) + 1):
#         if not num % dev:
#             return False
#     return True


# print(prime(23))


users_data = dict()
while data := input().split():
    name, surname, age, identificator = data
    if name.isalpha() == True and surname.isalpha() == True and 18 < int(age) < 60:
        value = name.capitalize(), surname.capitalize(), age
        users_data.setdefault(identificator.zfill(8), value)
    else:
        print("Ошибка, введены некорректные данные")
for key in users_data:
    print(key)
    # for name in users_data[keys]:
    #     print(name, surname, age)

# print(users_data.keys())

