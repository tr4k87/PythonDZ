from functools import reduce
import random
import numpy as np
# 1 Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# print('Введите значение X,Y,Z')
# x = input()
# y = input()
# z = input()
# one = not (x,y,z)
# two = not x and not y and not y
# # if one == two:
# #     print('True')
# # else:
# #     print('False')

# Упрощенный
# x = 1
# y = 2
# z = 3
# one = not (x,y,z)
# two = not x and not y and not z
# result = bool(lambda one, two: True if one == two else False)
# print(result)

# 2 # Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# n = list(map(int,input('Введите значения  через запятую ').split(',')))
# my_summ = 0
# i = n[1]
# for i, elem in enumerate(n):
#     if i % 2:
#         my_summ = my_summ + elem
# print(f"Сумма чисел на четном порядке из списка {n} -> {my_summ}")

# Упрощенный
# n = [1,2,3,4,5,6]
# result = list(map(lambda x: x if x%2 == 0 else None, n))
# result = [i for i in result if i!= None]
# result = reduce(lambda x,y: x + y, result)
# print(result)

# 3 Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# my_list = [1.1, 1.2, 3.1, 5, 10.01]
# max = my_list[0] % 1 * 100
# min = my_list[0] % 1 * 100
# j = int
# for i in my_list:
#     j = i % 1 *100
#     if j > 0:
#         if j > max: max = j
#         if j < min: min = j
# result = (max - min) / 100
# print(round(result, 2))

# Упрощенный
# my_list = [i for i in np.random.uniform((10, 10, 6, 7,10, 10))]
# print(my_list)
# result_list = list(map(lambda i: round(i % 1, 2) if i %1 != 0 else None, my_list))
# result_list = [i for i in result_list if i != None]
# print(max(result_list) - min(result_list))


# 4 Задача
# my_text = 'Напишите программу, удаляющабвую из текста все слова, содержащие "абв"'
# my_text = my_text.split()
# d = 'абв'
# my = list()
# for i in my_text:
#     if d not in i:
#         my.append(i)
# my = " ".join(my)
# print(my)

# Упрощенный
# my_text = 'Напишите программу, удаляющабвую из текста все слова, содержащие "абв"'
# my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
# my = " ".join(my_text)
# print(my)


#  5 Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов последовательности в том же порядке.

# list1 = list() # создаем списки
# list2 = list()
# n = input('Введите число ') # определяем длину списка
# def rand(n): # функция создания рандомного списка
#     for i in range(n):
#         list1.append(randrange(10)) # ограничил 10, чтобы чаще были совпадения
#     print(list1)

# def sort(n): # функция сортировки
#     for i in n:
#         if n.count(i) == 1: # проверяем вхождение числа == 1 в наш список,
#             list2.append(i)
#     print(list2)
# rand(n)
# sort(list1)

# упрощенный

list1 = (1,2,4,7,3,4,5,6,3,3,3) # создаем списки
print(list1)
list2 = list(i for i in list1 if list1.count(i) ==1)
print(list2)



