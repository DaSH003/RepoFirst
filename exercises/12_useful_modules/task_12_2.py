# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона,
например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список,
где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список, в котором содержатся IP-адреса
и/или диапазоны IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10


if iprange[-2] == "-":
                from_digits = 
                lastdigits = iprange[-1]
            else:
                lastdig

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные
адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только
последний октет адреса.

Функция возвращает список IP-адресов.

Например, если передать функции convert_ranges_to_ip_list такой список:
"""
ips = ['8.8.4.4-8', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
"""
Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""
def convert_ranges_to_ip_list(iplist):
    result = []
    ranges_for_ips = []
    for i in range(len(iplist)):
            iprange = iplist[i].split(".")
            rest_of_ip = f"{iprange[0]}.{iprange[1]}.{iprange[2]}."
            if "-" in iprange[-1]:
                from_digit = 0
                to_digit = 0
                for sym in range(len(iprange[-1])):
                    if iprange[-1][sym] == "-":
                        from_digit = iprange[-1][:sym]
                        to_digit = iprange[-1][sym+1:]
                ranges_for_ips.append([from_digit, to_digit, rest_of_ip])
            elif "-" in iprange[3]:
                from_digit = 0
                to_digit = 0
                for sym in range(len(iprange[3])):
                    if iprange[3][sym] == "-":
                        from_digit = iprange[3][:sym]
                        to_digit = iprange[-1]
                ranges_for_ips.append([from_digit, to_digit, rest_of_ip])
            else:
                ranges_for_ips.append([-1, -1])
                result.append(iplist[i])
    for ip in range(len(iplist)):
        if ranges_for_ips[ip][0] == -1:
            continue
        from_digit = int(ranges_for_ips[ip][0])
        to_digit = int(ranges_for_ips[ip][1]) + 1
        for num in range(from_digit, to_digit):
            result.append(f"{ranges_for_ips[ip][2]}{num}")
    return result

print(convert_ranges_to_ip_list(ips))
