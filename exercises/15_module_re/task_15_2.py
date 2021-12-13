# -*- coding: utf-8 -*-
"""
Задание 15.2

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show ip int br

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br.txt.

"""
import re
def parse_sh_ip_int_br(filename):
	result = []
	f = open(filename, 'r')
	lines = f.readlines()
	for i in lines:
		port = re.search(r'\w+\d+\D\d+\s', i)
		if not port:
			port = re.search(r'\w+\d+\s', i)
		ip = re.search(r'\d+\.\d+\.\d+\.\d+', i)
		if not ip:
			ip = re.search(r'unassigned', i)
		status = re.search(r'(\w+)\s+\w+\s+$', i)
		protocol = re.search(r'\w+$', i)
		if port and ip and status and protocol:
			result.append((port.group(), ip.group(), status.groups()[0], protocol.group()))
	return result

if __name__ == '__main__':
	print(parse_sh_ip_int_br("sh_ip_int_br.txt"))