# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах.
# Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

n = int(input("Введите число: "))

list = []

for i in range(-n , n+1):  
  list.append(i)

print(list)
  
index = input("Укажите индексы: ")
compos = index.split(' ')           # методом split делим индекс 

for j in compos[1:]:             # начинаем от 2 позиции
  compos[0] = int(compos[0])         # перевдоим на int первую позицию
  j=int(j)                           # перевдоим на int индексы
  result = list[compos[0]] * list[j]

print(result , end= ' ')

