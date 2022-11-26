# Реализуйте алгоритм перемешивания списка.
import random

n = int(input('Ввудите длину списка: '))
lisrFirst = []
listRandom = []
listCopy = []

for i in range(n):
  i = input(f'Введите {i} позицию списка: ')
  lisrFirst.append(i)
  
listCopy = lisrFirst.copy()

x = 0 
while x != n:                 # Цикл рандомного заполнения
  j = random.choice(lisrFirst) 
  
  if (j in listCopy ):   # условия проверки на повтор
    listRandom.append(j)
    listCopy.remove(j)
    x+=1 

print('Вводимый список = ', lisrFirst)
print('Рамдомный список = ', listRandom)