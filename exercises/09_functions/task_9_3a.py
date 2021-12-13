# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def get_int_vlan_map(config_file):
    f = open(config_file, 'r')
    lines = f.readlines()
    clear = []
    response = ()
    access = {}
    allowed = {}
    for i in lines:
        if i[0] == "!":
            continue
        clear.append(i)
    for i in range(len(clear)):
        clear[i] = clear[i].split()
    clear.pop(0)
    for i in range(len(clear)):
        interface = ""
        if clear[i][0] == "interface" and "Fast" in clear[i][1]:
            interface = clear[i][1]
            end = 0
            for j in range(i, len(clear)):
                if clear[j][0] == "duplex":
                    end = j
                    break
            if end - i < 3:
                access.update([(interface, "1")])
                continue
            for j in range(i, end):
                for k in range(len(clear[j])):
                    if clear[j][k] == "access" and clear[j][k-1] == "switchport":
                        access.update([(interface, clear[j][-1])])
                    if clear[j][k] == "allowed":
                        allowed.update([(interface, clear[j][-1])])
    response = (access, allowed)
    return response

print(get_int_vlan_map("config_sw2.txt"))