# -*- coding: utf-8 -*-
"""
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT
из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
"""
import re
def convert_ios_nat_to_asa(config_input, config_output):
	config = open(config_input, 'r')
	lines = config.readlines()
	output = ""
	for line in lines:
		ip = re.search(r'\d+\.\d+\.\d+\.\d+', line)
		if ip:
			ip = ip.group()
		port = re.search(r'\d+\.\d+\.\d+\.\d+\s(\d+)\s', line)
		if port:
			port = port.groups()[0]
		mode = re.search(r'\w+\s\w+\s(\w+)', line)
		if mode:
			mode = mode.groups()[0]
		prot = re.search(r'(\w+)\s\d+\.\d+\.\d+\.\d+', line)
		if prot:
			prot = prot.groups()[0]
		status = re.search(r'(\w+)\s\w+\s\d+\.\d+\.\d+\.\d+', line) 
		if status:
			status = status.groups()[0]
		smth = re.search(r'^\w+\s(\w+)', line)
		if smth:
			smth = smth.groups()[0]
		nums = re.search(r'(\d+)\s$', line)
		if nums:
			nums = nums.groups()[0]
		if ip and port and mode and prot and status and smth and nums:
			output += f"object LOCAL_{ip}\n host {ip}\n {smth} ({mode}, outside) {status} interface service {prot} {port} {nums}\n"
	config.close()
	config = open(config_output, 'w')
	config.write(output)

if __name__ == '__main__':
	convert_ios_nat_to_asa('cisco_nat_config.txt','cisco_nat_config_converted.txt')