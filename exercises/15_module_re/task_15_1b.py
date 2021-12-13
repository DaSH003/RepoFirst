# -*- coding: utf-8 -*-
"""
Задание 15.1b

Проверить работу функции get_ip_from_cfg из задания 15.1a
на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция get_ip_from_cfg, интерфейсу Ethernet0/1
соответствует только один из них.

Скопировать функцию get_ip_from_cfg из задания 15.1a и переделать ее таким
образом, чтобы в значении словаря она возвращала список кортежей
для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет
несколько кортежей. Ключом остается имя интерфейса.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.

Обратите внимание, что в данном случае, можно не проверять корректность
IP-адреса, диапазоны адресов и так далее, так как обрабатывается вывод команды,
а не ввод пользователя.

"""
import re
def get_ip_from_cfg(filename):
	result = {}
	f = open(filename, 'r')
	lines = f.readlines()
	port = ""
	for i in range(len(lines)):
		match = re.search(r'interface (\S+)', lines[i])
		if match:
			port = match.groups()
			print(port)
			port = f"{port[0]}"
			offset = 0
			for j in range(i, len(lines)):
				if lines[j] == "!\n":
					offset = j
					break
			ip_mask_list = []
			for k in range(i, offset):
				ip_mask = re.search(r'ip address (\S+) (\S+)', lines[k])
				if ip_mask:
					ip_mask = ip_mask.groups()
					ip_mask_list.append(ip_mask)
			if len(ip_mask_list):
				result.update([(port, ip_mask_list)])
	return result

if __name__ == "__main__":
	print(get_ip_from_cfg("config_r2.txt"))