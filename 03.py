# 3. Напишите программу, в которой пользователь будет задавать 
# две строки, а программа - определять количество вхождений одной строки в другой.
# 'Я люблю Python'
# 'лю'
# --> 2

# text = 'Я люблю Python'
# searchtext = 'лю'
# ----------------------------------------
# Методом split

# list = text.split(searchtext)
# print(len(list)-1)
# ----------------------------------------
# Методом cout

# cout = text.count(searchtext)
# print(cout)
# ----------------------------------------
# Алгоритм разделения строки на куски через цикл ащк

# my_string = 'Я люблю Python'
# s2 = input("Введите строку для проверки вхождения: ")
# number = 0
# for i in range(len(my_string) - len(s2)+1):
#     if my_string[i:i+len(s2)] == s2:
#         number += 1
# print(number)
# ----------------------------------------
# Алгоритм резделения строки на куски через цикл while

# text = 'Я люблю Python'
# char = input('Введите значение поиска: ')
# len_char = len(char)
# i = 0
# count = 0

# while i < len(text)-len_char:
#     if char.lower() == text[i:len_char+i].lower():
#         count +=1
#     i += 1
# print(count)
# ----------------------------------------
# for i in text:
#   if i == text1:
#     cout+=1
# print(cout)


