# -*- coding: utf-8 -*-
"""
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.

Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример итогового списка:
["Loopback0", "Tunnel0", "Ethernet0/1", "Ethernet0/3.100", "Ethernet1/0"]

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
"""
import re

def get_ints_without_description(config_file):
	config = open(config_file, 'r')
	lines = config.readlines()
	response = []
	interface = ""
	for i in range(len(lines)):
		line = lines[i]
		interface = re.search(r'^interface (\S+)\n', line)
		if interface:
			interface = interface.groups()[0]
			offset = 0
			for j in range(i+1, len(lines)):
				line_local = lines[j]
				interface_local = re.search(r'^interface (\S+)', line_local)
				if interface_local:
					offset = j
					break
			description = ""
			for k in range(i, offset):
				line_local = lines[k]
				description = re.search(r' description', line_local)
				if description:
					break
			if not description:
				response.append(interface)	

	return response







if __name__ == '__main__':
	print(get_ints_without_description('config_r1.txt'))	