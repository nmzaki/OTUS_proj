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
#     hundreds = ar_num // 100 % 10
#     tens = ar_num // 10 % 10
#     units = ar_num % 10
#     if ar_num < 4000:
#         if thousands < 4:
#             rome_thousands = 'M' * thousands
#         elif thousands == 0:
#             rome_thousands = ''
#         else:
#             print('В римской нумерации нет чисел больше 3999!')
#         if hundreds != 0:
#             if hundreds < 4:
#                 rome_hundreds = 'C' * hundreds
#             elif hundreds == 4:
#                 rome_hundreds = 'CD'
#             elif hundreds == 5:
#                 rome_hundreds = 'D'
#             elif hundreds > 5 and hundreds < 9:
#                 rome_hundreds = 'D' + ('C' * (hundreds - 5))
#             elif hundreds == 9:
#                 rome_hundreds = 'CM'
#         else:
#             rome_hundreds = ''
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
#     rome_number = rome_thousands + rome_hundreds + rome_tens + rome_units
#     print(rome_number)
# else:
#     print('В римской нумерации нет чисел больше 3999!')


# Задача 5
# data = input('Введите данные: \n')
# if data.count('.') <= 1 and data.isdigit == True and '.' not in data[-1]:
#     print(f'{float(data)} -> {True}')
# else:
#     print(f'{data} -> {False}')
