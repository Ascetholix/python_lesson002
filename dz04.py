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
b = True
result =0
for i in range(-n , n+1):  
  list.append(i)

print(list)
  
index = input("Укажите индексы: ")
compos = index.split(' ')        # методом split делим индекс 

print(compos)

for j in compos[1:]:             # начинаем от 2 позиции
  if b == True:                    # буливая перемная для первичного присвоения
    result = int(list[int(compos[0])])         # перевдоим на int первую позицию
    b = False
  j=int(j)                           # перевдоим на int индексы
  result = result * list[j]

print(result , end= ' ')

