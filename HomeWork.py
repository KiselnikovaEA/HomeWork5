# Задача 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# with open('Task1_text.txt', 'r', encoding='utf-8') as f:
#     data = f.read()
#     print('Исходный текст: ', data)

# words = data.split()

# new_text = " ".join(list(filter(lambda x: 'абв' not in x, words)))
# print('Преобразованный текст: ', new_text)

# with open ('Task1_new_text.txt', 'w', encoding='utf-8') as new_file:
#     new_file.write(new_text)

#-------------------------------------------------------------------------------------------------------------------------------------------------------

# Задача 2. Программа для игры с конфетами человек против человека. Всего 2021 конфета, брать можно до 28 конфет по очереди. Кто взял последнюю - тот выйграл.
#       Вариант: ЧЕЛОВЕК ПРОТИВ ЧЕЛОВЕКА

# import random

# player1 = input('Игрок 1, введите Ваше имя: ')
# player2 = input('Игрок 2, введите Ваше имя: ')
# sweets = 2021
# turn = 0

# flag = random.choice([-1, 1])
# if flag == 1:
#     print(f'В результате жребьёвки победил игрок {player1}')
# else:
#     print(f'В результате жребьёвки победил игрок {player2}')

# while sweets > 0:
#     if flag == 1:
#         turn = int(input(f'Остаток конфет: {sweets}. Ходит {player1}: '))
#     else:
#         turn = int(input(f'Остаток конфет: {sweets}. Ходит {player2}: '))
           
#     if turn <= 28 and turn <= sweets:
#         sweets -= turn
#     else:
#         print('Нельзя брать больше 28 конфет или остатка!')
#         continue
#     flag *= -1

# if flag == 1:
#     print(f'Ура! победа за игроком {player2}!')
# else:
#     print(f'Ура! победа за игроком {player1}!')



#       Вариант: ЧЕЛОВЕК ПРОТИВ "ГЛУПОГО БОТА" (бот ходит случайным образом) ------------------------------------------------------

# import time
# import random

# player = input('Игрок, введите Ваше имя: ')
# sweets = 2021
# flag = random.choice([-1, 1]) # встроенная функция используется для жребьёвки

# if flag == 1:
#     print(f'В результате жребьёвки победил игрок {player}')
# else:
#     print(f'В результате жребьёвки победил бот')

# turn = 0 # сюда записываем количество взятых конфет

# def my_random (min, max): # позаимствованный рандомайзер используется для хода компьютера
#     time.sleep(0.3)
#     return int((time.time() % 1 * (max - min)) + min)

# while sweets > 0:
#     if flag == 1:
#         turn = int(input(f'Остаток конфет: {sweets}. Ваш ход, {player}: '))
#     else:
#         print(f'Остаток конфет: {sweets}. Ход бота: ', end='')
#         if sweets <= 28:
#             turn = my_random(1, sweets)
#         else:
#             turn = my_random(1, 28)
#         print(turn)
       
#     if turn <= 28 and turn <= sweets:
#         sweets -= turn
#     else:
#         print('Нельзя брать больше 28 конфет или остатка!')
#         continue
#     flag *= -1

# if flag == 1:
#     print('Да уж. Вас выйграл бот. Ну, не расстраивайтесь.')
# else:
#     print('Ура! Вы победили бота!')



#       Вариант: ЧЕЛОВЕК ПРОТИВ "УМНОГО БОТА" ---------------------------------------------------------------------

# import time
# import random

# player = input('Игрок, введите Ваше имя: ')
# sweets = 2021
# flag = random.choice([-1, 1]) # жребьёвка

# if flag == 1:
#     print(f'В результате жребьёвки победил игрок {player}')
# else:
#     print(f'В результате жребьёвки победил бот')

# turn = 0 # сюда записываем количество взятых конфет

# def my_random (min, max): # рандомайзер для хода компьютера
#     time.sleep(0.3)
#     return int((time.time() % 1 * (max - min)) + min)

# while sweets > 0:
#     if flag == 1:
#         turn = int(input(f'Остаток конфет: {sweets}. Ваш ход, {player}: '))
#     else:
#         print(f'Остаток конфет: {sweets}. Ход бота: ', end='') # ход бота
#         if sweets <= 28:
#             turn = sweets
#         else:
#             turn = sweets - (sweets//29 * 29) # бот всегда берёт остаток от целочисленного деления количества конфет на 28+1
#             if turn == 0:
#                 turn = my_random(1, 29)
#         print(turn)
       
#     if turn <= 28 and turn <= sweets:
#         sweets -= turn
#     else:
#         print('Нельзя брать больше 28 конфет или остатка!')
#         continue
#     flag *= -1

# if flag == 1:
#     print('Да уж. Вас выйграл бот. Ну, не расстраивайтесь.')
# else:
#     print('Ура! Вы победили бота!')

#-----------------------------------------------------------------------------------------------------------------------

# Задача 3. Крестики-нолики (вдохновлялась красивой реализацией в интернете, переделала под себя)

# board = list(range(1,10))

# def draw_board(board): # вывод на экран по сути одномерного массива, но в структуре крадрата 3х3 клетки
#     print ("-" * 13)
#     for i in range(3):
#         print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#         print ("-" * 13)

# def take_input(player_sign):
#     valid = False
#     while not valid:
#         player_answer = input("В какую клетку поставим " + player_sign + "? ")
#         try:           # структура как try-catch в C#
#             player_answer = int(player_answer)
#         except:
#             print ("Некорректный ввод. Вводить можно только числа?")
#             continue
#         if player_answer >= 1 and player_answer <= 9:
#             if (str(board[player_answer-1]) not in "XO"):
#                 board[player_answer-1] = player_sign
#                 valid = True
#             else:
#                 print ("Эта клетка уже занята")
#         else:
#             print ("Некорректный ввод. Введите число от 1 до 9 чтобы сделать ход.")

# def check_win(board):
#     win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
#     for each in win_coord:
#         if board[each[0]] == board[each[1]] == board[each[2]]:
#             return board[each[0]]
#     return False

# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#             take_input("X")
#         else:
#             take_input("O")
#         counter += 1
#         if counter > 4:
#             tmp = check_win(board)
#             if tmp:
#                 print (tmp, "выиграл!")
#                 win = True
#                 break
#         if counter == 9:
#             print ("Ничья!")
#             break
#     draw_board(board)

# main(board)

# Задача 4. RLE-алгоритм: ШИФРАТОР -------------------------------------------------------------------------------------------------

# with open('Task4_text.txt', 'r', encoding='utf-8') as f:
#     some_text = f.read()
#     print('Исходный текст: ', some_text)

# with open('Task4_zipped_text.txt', 'w', encoding='utf-8') as z:
#     count = 1
#     for i in range(1, len(some_text)):
#         if some_text[i] == some_text[i - 1]:
#             count +=1
#         else:
#             z.write(str(count) + some_text[i - 1])
#             count = 1
#     z.write(str(count) + some_text[-1])

# ДЕШИФРАТОР -------------------------------------------------------------------------------------------------

# with open('Task4_zipped_text.txt', 'r', encoding='utf-8') as f:
#     some_text = f.read()
#     print('Исходный текст: ', some_text)

# some_list = list()
# element = ''
# for i in range(0, len(some_text)):
#     if some_text[i] in "0123456789":
#         element += some_text[i]
#     else:
#         some_list.append(int(element))
#         element = ''
#         some_list.append(some_text[i])
# print(some_list)

# with open('Task4_unzipped_text.txt', 'w', encoding='utf-8') as z:
#     for i in range(0, len(some_list), 2):
#         z.write(some_list[i + 1] * some_list[i])