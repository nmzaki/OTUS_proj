# Задача 1
# Вариант 1

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

# Вариант 2

# figure = str(input('Введите пятизначное число \n'))
# if len(str(figure)) > 5:
#     print('Введено больше 5-ти цифр')
# elif  len(str(figure)) < 5:
#     print('Введено меньше 5-ти цифр')
# new_figure = figure[0] + figure[3] + figure[2] + figure[1] + figure[4]
# print(new_figure)



# Задача 2

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

# Задача 3
# length, width, size = (
#     int(input("Введите длинну: ")),
#     int(input("Введите ширину: ")),
#     int(input("Введите размер куска: ")),
# )
# if size % length == 0 or size % width == 0:
#     print(True)
# else:
#     print(False)
