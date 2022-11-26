# Реализуйте алгоритм перемешивания списка.
import random

n = int(input('Ввудите длину списка: '))
lisrFirst = []
listRandom = []

for i in range(n):
  i = input(f'Введите {i} позицию списка: ')
  lisrFirst.append(i)

b = True         
x = 0 
while x != n-1:                 # Цикл рандомного заполнения
  j = random.choice(lisrFirst) 
  
  if b == True:                # Условие 1го присваивание рандомного значаение
    listRandom.append(j)
    b = False
  
  if (j in listRandom) == False:   # условия проверки на повтор
    listRandom.append(j)
    x+=1 

print(lisrFirst)
print(listRandom)