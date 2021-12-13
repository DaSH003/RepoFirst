#!/usr/bin/env python3
access_template = ['switchport mode access', 'switchport acces vlan{}', 'switchport nonegotiate', 'spannin-tree portfast', 'spanning-tree bpduguard enable']
print('\n'.join(access_template).format(5))
