import random

# Напишите программу, удаляющую из текста все слова, содержащие "абв".

# my_text = 'Напишите программу, удаляющабвую из текста все слова, содержащие "абв"'
# my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
# my = " ".join(my_text)
# print(my)

# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# name1 = input('Введите имя первого игрока: ')
# name2 = input('Введите имя второго игрока: ')
# ran = random.randint(1,2)
# print(f'Перый ходит Игрок № {ran}')

# def game(n1, n2):
#     k = 2021
#     print('У вас 2021 конфета, можно брать максимум 28 конфет, кто сдлелал последний ход, тот и победил')
#     if ran == 1:
#         print(f'Первый ходит {name1} ')
#         count = 1
#     else:
#         print(f'Первый ходит {name2} ')
#         count = 2
#     while k > 0:
#         kon = int(input('Введите количество конфет '))
#         k = k - kon
#         print(f'осталось {k} конфет')
#         count += 1
#     if count % 2 == 0:
#         print(f'Выиграл игрок {name1}')
#     else:
#         print(f'Выиграл игрок {name2}')

# game(name1, name2)

# a) Добавьте игру против бота
# name1 = input('Введите Ваше имя: ')
# ran = random.randint(1,2)
# print(f'Жребий пал на Игрока № {ran}')
# def game(n1):
#     k = 30
#     print('У вас 2021 конфета, можно брать максимум 28 конфет, кто сдлелал последний ход, тот и победил')
#     if ran == 1:
#         print(f'Первый ходит {name1} ')
#         count = int(1)
#     else:
#         print(f'Первый ходит Бот ')
#         count = int(2)
#     while k > 0:
#         if count %2 == 0:
#             k = k - bot(k)
#             count += 1
      
#         else:
#             kon = int(input('Введите количество конфет '))
#             k = k - kon
#             print(f'осталось {k} конфет')
#             count += 1

#     if count % 2 == 0:
#         print(f'Выиграл игрок {name1}')
#     else:
#         print(f'Выиграл игрок Бот')

# def bot(n):
#     if n > 28:
#         print('Бот забрал 28 конфет')
#         return 28
#     else:
#         print(f'Бот забрал {n} конфет')
#         return n


# game(name1)

# b) Подумайте как наделить бота ""интеллектом""
# name1 = input('Введите Ваше имя: ')
# ran = random.randint(1,2)
# print(f'Жребий пал на Игрока № {ran}')
# def game(n1):
#     k = 30
#     print('У вас 2021 конфета, можно брать максимум 28 конфет, кто сдлелал последний ход, тот и победил')
#     if ran == 1:
#         print(f'Первый ходит {name1} ')
#         count = int(1)
#     else:
#         print(f'Первый ходит Бот ')
#         count = int(2)
#     while k > 0:
#         if count %2 == 0:
#             k = k - bot(k)
#             count += 1
      
#         else:
#             kon = int(input('Введите количество конфет '))
#             k = k - kon
#             print(f'осталось {k} конфет')
#             count += 1

#     if count % 2 == 0:
#         print(f'Выиграл игрок {name1}')
#     else:
#         print(f'Выиграл игрок Бот')

# def bot(n):
#     if n > 28:
#         print('Бот забрал 28 конфет')
#         return 28
#     else:
#         print(f'Бот забрал {n} конфет')
#         return n

# # Я не стал копировать всю программу, добавил алгоритм для "умного" бота. 
# def iqbot(n):
#     kon = n % 29
#     print(f'Бот забрал {kon} конфет')
#     return kon
# game(name1)

# Создайте программу для игры в ""Крестики-нолики"".

# print('-----')
# print('{0} {1} {2}'.format(1,2,3))
# print('{3} {4} {5}'.format(4,5,6))
# print('{6} {7} {8}'.format(7,8,9))
# print('-----')

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
with open('dz5in.txt', 'r') as data:
    a = data.read()
count = 1
for i in range(len(a)-1):
    if i <= len(a):
        if a[i] == a[i + 1]:
            count += 1
        else:
            print(f'{count}{a[i]}',end ='')
            count = 1
print(f'{count}{a[i]}')

a = '6a7b6e4w'
b = ''
for i in range(0,len(a),2):
    if i <= len(a):
        c = int(a[i])
        b += a[i+1] * c
print(b)
with open('dz5out.txt', 'a') as data:
    data.write(b)


