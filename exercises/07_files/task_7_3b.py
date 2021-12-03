# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
def sorting(val):
    return int(val[0])
vlan = int(input("Enter VLAN number: "))
f = open("CAM_table.txt", 'r')
lines = f.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].split()
filtered = []
for i in range(6, len(lines)):
    filtered.append(lines[i])
out = ""
filtered = sorted(filtered, key=sorting)
for i in range(len(filtered)):
    if int(filtered[i][0]) == vlan:
        out += filtered[i][0] + " "*(9 - len(filtered[i][0])) + filtered[i][1] + " "*6 + filtered[i][3] + "\n"
print(out)
