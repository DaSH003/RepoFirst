# -*- coding: utf-8 -*-
"""
Задание 15.5

Создать функцию generate_description_from_cdp, которая ожидает как аргумент
имя файла, в котором находится вывод команды show cdp neighbors.

Функция должна обрабатывать вывод команды show cdp neighbors и генерировать
на основании вывода команды описание для интерфейсов.

Например, если у R1 такой вывод команды:
R1>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Eth 0/0           140          S I      WS-C3750-  Eth 0/1

Для интерфейса Eth 0/0 надо сгенерировать такое описание
description Connected to SW1 port Eth 0/1

Функция должна возвращать словарь, в котором ключи - имена интерфейсов,
а значения - команда задающая описание интерфейса:
'Eth 0/0': 'description Connected to SW1 port Eth 0/1'


Проверить работу функции на файле sh_cdp_n_sw1.txt.
"""
import re
def generate_description_from_cdp(filename):
    response = {}
    config = open(filename, 'r')
    lines = config.readlines()
    for line in lines:
        print(line)
    for i in range(len(lines)):
        line = lines[i]
        device = re.search(r'^(\w+\d+)', line)
        interface = re.search(r'^\S+\s+(\w+\s+\d+/\d+)', line)
        port_id = re.search(r'(\w+\s+\d+/\d+)$', line)
        if device and interface and port_id:
            device = device.groups()[0]
            interface = interface.groups()[0]
            port_id = port_id.groups()[0]
            response.update([(interface, f"description Connected to {device} port {port_id}")])
    return response

if __name__ == "__main__":
    response = generate_description_from_cdp("sh_cdp_n_sw1.txt")
    for i in response:
        print(f"{i}:{response[i]}")