# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

import random

n=int(input("Введите количество элементов массива -> "),)
a=[]
for i in range(n):
    a.append(random.randint(-5,10))
print(a)

x=int(input("Введите ваше число -> ",))

kol=0
for i in range(len(a)):
    if a[i]==x: kol+=1

print(f"ваше число {x} встречается -> {kol} раз")
