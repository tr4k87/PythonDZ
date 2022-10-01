# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# n = [2, 3, 5, 9, 3, 4, 8]
# my_summ = 0
# i = n[1]
# for i, elem in enumerate(n):
#     if i % 2:
#         my_summ = my_summ + elem 
# print(my_summ)

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

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# my_list = [1.1, 1.2, 3.1, 5, 10.01]
# max = my_list[1] % 1 * 100
# min = my_list[1] % 1 * 100
# j = int
# for i in my_list:
#     j = i % 1 *100
#     if j > max: max = j
#     if j < min: min = j
# result = (max - min) / 100
# #  не стал применять округление, т.к. при любом кол-ве после "," 
# # в данном случае округляет до одной цифры после нее
# print(result)

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# n = int(input('Введите число '))
# j = format(n, 'b')
# print(f"Цифра {n} -> {j}")

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

f1 = 1
f2 = 0
n = int(input('Введите число '))
k = -n
result = list()
while n > 0:
    f1, f2 = f2, f1 + f2
    result.append(f2)
    n -= 1
result = result
f1 = 1
f2 = 0 
while k < 0:
    f1, f2 = f2, f1 - f2
    result.insert(0 , f2)
    k += 1
result = result
print(result)
