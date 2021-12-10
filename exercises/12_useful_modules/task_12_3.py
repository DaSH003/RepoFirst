# -*- coding: utf-8 -*-
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7   
10.1.1.2     10.1.1.8
             10.1.1.9

"""
def print_ip_table(reachable, unreachable):
    print("Reachable    Unreachable")
    print("-----------  -------------")
    sum_lengths = len(reachable) + len(unreachable)
    for i in range(sum_lengths):
        string = ""
        if i < len(reachable):
            string += reachable[i] 
            string = string + " " * (14 - len(reachable[i]))
        if i >= len(reachable):
            string = string + " " * 14
        if i < len(unreachable):
            string += unreachable[i]
        print(string)


print_ip_table(["localhost", "127.0.0.1", "192.168.1.1","192.168.1.43"],["google.com", "vk.com", "ya.ru", "youtube.com", "bing.com"])
    
