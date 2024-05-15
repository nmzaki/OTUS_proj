
# сделать через int делением нацело

# figure = str(input('Введите пятизначное число \n'))
# if len(str(figure)) > 5:
#     print('Введено больше 5-ти цифр')
# elif  len(str(figure)) < 5:
#     print('Введено меньше 5-ти цифр')
# new_figure = figure[0] + figure[3] + figure[2] + figure[1] + figure[4]
# print(new_figure)

work_days = int(input('Введите количество дней до ближайшего отпуска \n'))
weeks = work_days // 7
if work_days < 5:
    print('0')
elif 5 < work_days < 7:
    print(7 - work_days)
elif work_days > 7 and (work_days - weeks * 7) < 5:
    print(weeks * 2)
else:
    print((weeks * 2) + (work_days - (weeks * 7) - 5))
