network = input("Введите адрес сети с маской: ")
i = 0
maskbits = int(network.split("/")[1])
ip = network.split("/")[0]
ip = ip.split(".")
bits = "1"*maskbits + "0"*(32-maskbits)
netbits = [bits[0:8], bits[8:16], bits[16:24], bits[24:32]]
hostbin = []
for i in ip:
    a = int(i)
    _bin = f"{a:b}"
    _bin = '0'*(8-len(_bin)) + _bin
    hostbin.append(_bin)
for i in range(len(hostbin)):
    net = ""
    for j in range(len(hostbin[i])):
        if hostbin[i][j] == "1" and netbits[i][j] == "1":
            net += "1"
        else:
            net += "0"
    ip[i] = int(net, 2)
ipbin = []
print("Network: ")
for i in ip:
    ipdec = int(i)
    ipb = f"{ipdec:b}"
    ipb = ("0" * (8 - len(ipb))) + ipb
    ipbin.append(ipb)
for i in ip:
    print(i, end="")
    print(" "*16, end="")
print()
for i in ipbin:
    print(i, end="")
    print(" "*8, end="")
print()
print("Mask: ")
bitslist = []
bitslist.append(bits[0:8])
bitslist.append(bits[8:16])
bitslist.append(bits[16:24])
bitslist.append(bits[24:32])
for ibits in bitslist:
    decimal = 0
    for digit in ibits:
        decimal = decimal*2 + int(digit)
    print(decimal, end="")
    print(" "*16, end="")
print()
for ibits in bitslist:
    print(ibits, end="")
    print(" "*8, end="")
