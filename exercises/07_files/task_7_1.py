# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
f = open("ospf.txt", "r")
lines = f.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].split()
for i in lines:
    output = f"Prefix                {i[1]}\nAD/Metric             {i[2][1:-1]}\nNext-Hop              {i[4]}\nLast update           {i[5]}\nOutbound Interface    {i[6]}"
    print(output)
    print("\n\n")
