# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# n = list(map(int,input('Введите значения  через запятую ').split(','))) 
# my_summ = 0
# i = n[1]
# for i, elem in enumerate(n):
#     if i % 2:
#         my_summ = my_summ + elem 
# print(f"Сумма чисел на четном порядке из списка {n} -> {my_summ}")

# my_list = [2, 3, 5, 6, 8]
# my_sum = 0
# for i in range(1, len(my_list), 2):
#     if i % 2 :
#         my_sum += my_list[i]
# print(my_sum)

# import random
# num=int(input('Введите число '))
# num_list=[]
# for i in range(num):
# 	num_list.append(random.randint(1,10))	
# print(num_list)
# print(sum(num_list[::2]))

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# my_list = input('Введите значения в список ')
# while not my_list.isdigit():
#     my_list = input('Ошибка ввода! Введите значения в список ')
# my_list = list(map(int, my_list))
# result = list()
# j = 0
# size1 = len(my_list)
# size2 = len(my_list)
# k = my_list[-1]
# for i in my_list:
#     if size2 > size1/2:
#         j = i * k
#         result.append(j)
#         size2 = size2 - 1
#         k = k - 1
# print(result)

# my_list = [2, 1, 4, 5, 6]
# print_list = []
# for i in range(len((my_list)+1)//2):
#     print_list.append((my_list) + my_list[-1 - i])
# print(print_list)


# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

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

# my_list = [1.1, 1.2, 3.1, 5, 10.01]
# result_list = []
# for i in my_list:
#     if i % 1 !=0:
#         result_list.append(round(i % 1, 2))
# print(max(result_list) - min(result_list))


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# n = int(input('Введите число '))
# j = (n, 'b')
# print(f"Цифра {n} -> {j}")

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# f1 = 1
# f2 = 0
# n = int(input('Введите число '))
# k = -n
# result = list()
# while n > 0:
#     f1, f2 = f2, f1 + f2
#     result.append(f2)
#     n -= 1
# result = result
# f1 = 1
# f2 = 0 
# while k < 0:
#     f1, f2 = f2, f1 - f2
#     result.insert(0 , f2)
#     k += 1
# result = result
# print(result)
