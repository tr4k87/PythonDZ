
import random
from unittest.mock import patch
# ЗАДАЧА №1: Вычислить число с заданной точностью d

# n = float(input('Введите значение ')) # вводим значение
# d = float(input('Введите значение d в формате 0.0001: '))  #Вводим погрешность
# count = 0 # создаем счетчик
# while d < 1: # пока d < 1 умножаем на 10, после каждого прохода увеличиваем счетчик, чтобы посчитать кол-во знаков после ","
#     d = d*10
#     count += 1
# print(round(n, count)) # через round форматируем число под нужную точность

# ЗАДАЧА №2: Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N

# N = int(input('Введите число '))
# result = list() # создаем список
# d = 2 # обозначаем делитель
# while N > 1: #
#     while N % d == 0: # проверяем остаток на деление
#         result.append(d)
#         N = N / d
#     d += 1
# print(result)

# ЗАДАЧА №3: Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов последовательности в том же порядке.

# from random import randrange

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

# ЗАДАЧА №4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлена в степени k.

# k = int(input('Введите степень '))
# n = list(random.randint(0,101) for i in range(k))
# z = list()
# print(n)
# def mnogo(k, n):
#     while k >= 1:
#         for i in range(k):
#             if k > 1:
#                 j = n[i] 
#                 f = k
#                 # l = j
#                 z.append(j)
#                 l = "*x^"
#                 z.append(l)
#                 z.append(f)
#                 z.append('+')
#             elif k > 0:
#                 j = n[i]
#                 l = "*x = 0"
#                 z.append(j)
#                 z.append(l)
#             k -= 1      
# mnogo(k, n)
# z = str(z)
# z = "".join(z)
# print(z)
# mnocl = open('mnogo.txt', 'a')
# mnocl.writelines(z)
# mnocl.write('\n')
# mnocl.writelines(z)
# mnocl.write('\n')
# mnocl.writelines(z)
# mnocl.close()

# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

a = open('file.txt', 'r')
res1 = a.read()
a.close()
b = open('mnogo.txt', 'r')
res2 = b.read()
b.close()
print(res1+res2)