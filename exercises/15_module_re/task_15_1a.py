# -*- coding: utf-8 -*-
"""
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом,
чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1': ('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2': ('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды,
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
			port = f"{port[0]}"
			offset = 0
			for j in range(i, len(lines)):
				if lines[j] == "!\n":
					offset = j
					break
			for k in range(i, offset):
				ip_mask = re.search(r'ip address (\S+) (\S+)', lines[k])
				if ip_mask:
					ip_mask = ip_mask.groups()
					result.update([(port, ip_mask)])
					break
	return result

if __name__ == "__main__":
	print(get_ip_from_cfg("config_r1.txt"))