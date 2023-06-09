# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: 
# an  = a1  + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

def create_list(pr_a1: int, pr_d: int, pr_count: int) -> list:
    res_list=list()
    for i in range(1,pr_count+1):
        res_list.append(pr_a1+(i-1)*pr_d)
    return res_list

def main():
    a1=int(input("Введите первый элемент арифметической прогрессии -> "))
    d=int(input("Введите разность арифметической прогресии -> "))
    n=int(input("Введите количество элементов арифметической прогресии -> "))

    print(create_list(a1, d, n))

main()