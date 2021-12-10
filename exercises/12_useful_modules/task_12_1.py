# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess
def ping_ip_adresses(iplist):
    ip_ok = []
    ip_dead = []
    for ip in iplist:
        result = subprocess.run(['ping', '-c', '3', '-n', ip], stdout=subprocess.PIPE)
        status = result.returncode
        if not status:
            ip_ok.append(ip)
        else:
            ip_dead.append(ip)
    result = (ip_ok, ip_dead)
    return result
listips = ["192.168.1.1", "localhost", "192.168.177.162", "google.com", "127.0.0.1", "vk.com"]

if __name__ == "__main__":
    print(ping_ip_adresses(listips))
