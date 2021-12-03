# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]
import sys
filename = sys.argv[1]
filename_output = sys.argv[2]
config = open(filename, 'r')
flag = False
output = []
for i in config:
    for ig in ignore:
        if ig in i:
            flag = True
    if flag:
        flag = not flag
        continue
    if "!" != i[0]:
        output.append(i)
out = open(filename_output, 'w')
for i in output:
    out.write(i)
