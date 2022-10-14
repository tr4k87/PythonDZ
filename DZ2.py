# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

result = 0
n = input('Введите число ')
while not n.isdigit():
    n = input('Неверно ввел, введите число ')
n = (list(map(int, n)))
for i in n:
    result = result + n[i-1]
print(result)

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# n = input('Введите число ')
# while not n.isdigit():
#     n = input('Неверно ввел, введите число ')
# n = int(n)
# result = list()
# j = 1
# for i in range(n):
#     j = (i + 1) * j
#     result.append(j)
# print(result)


# Задайте список из n чисел, заполненных по формуле (1+1/n)**n и выведети их сумму

# n = input('Введите число ')
# while not n.isdigit():
#     n = input('Введите число ')
# n = int(n)
# result = dict()
# sum = 0
# for i in range(1, n + 1):
#     result[i] = (1+1/i)**i
#     result[i] = round(result[i], 0)
#     sum = sum + result[i]
# print(result)
# print(sum)

# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 

# a = input('Введите первое значение ')
# while not a.isdigit():
#     a = input('Введите первое значение ')
# b = input('Введите второе значение ')
# while not b.isdigit():
#     b = input('Введите второе значение ')
# a = int(a)
# b = int(b)
# N = input('Введите количество элементов в списке ')
# while not N.isdigit():
#     N = input('Введите количество элементов в списке ')
# N = int(N)
# result = list()
# for i in range(-N, N+1):
#     result.append(i)
# print(result)
# print(result[a-1]*result[b-1])


# Реализуйте алгоритм перемешивания списка.
# import random
# n = input('Введите количество элементов в списке ')
# while not n.isdigit():
#     n = input('Введите количество элементов в списке ')
# n = int(n)
# result = list()
# def add(n):
#     for i in range(1,n+1):
#         result.append(i)
#     return(result)
# def rand(n):
#     for i in range(1, n):
#         j = random.randint(1,n)
#         result[i] = j
#     return(result)
# print(add(n))
# print(rand(n))
