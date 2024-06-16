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

# report_card = {}
# while data := input().split():
#     subject, surname, mark = data
#     if subject not in report_card:
#         report_card[subject] = {}
#     if surname not in report_card[subject]:
#         report_card[subject][surname] = []
#
#     report_card[subject][surname].append(mark)
#
# for subject, surnames in report_card.items():
#     print(subject)
#     print(f'{"Фамилия":<15} {"Оценки"}')
#     for surname, marks in surnames.items():
#         print(f'{surname:<16}{' '.join(marks)}')
