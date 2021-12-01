mode = input("Введите режим интерфейса (access/trunk): ")
interface_num = input("Введите тип и номер интерфейса: ")
access_template = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]
trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]
if mode == "trunk":
    vlans = input("Введите разрешенные VLANы: ")
    print()
    print(f"interface {interface_num}")
    print(trunk_template[0])
    print(trunk_template[1])
    print(trunk_template[2], vlans)
else:
    vlans = input("Введите номер VLAN: ")
    print()
    print(f"interface {interface_num}")
    print(access_template[0])
    print(access_template[1], vlans)
    for i in range(2, len(access_template)):
        print(access_template[i])
    
