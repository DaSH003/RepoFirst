london_co = {
	"r1":{
		"location":"21 New Globe Walk",
		"vendor":"Cisco",
		"model":"4451",
		"ios":"15.4",
		"ip":"10.255.0.1"
	},
	"r2":{
		"location":"21 New Globe Walk",
		"vendor":"Cisco",
		"model":"4451",
		"ios":"15.4",
		"ip":"10.255.0.2"
	},
	"sw1":{
		"location":"21 New Globe Walk",
		"vendor":"Cisco",
		"model":"3850",
		"ios":"3.6.XE",
		"ip":"10.255.0.101",
		"vlans":"10, 20, 30",
		"routing":True
	}
}
mode = input("Введите имя устройства: ")
configs = london_co[mode].keys()
configs_print = ""
i = 0
for i in configs:
	configs_print += f"{i}, "
config = input(f"Введите имя параметра({configs_print[0:-2]}): ").lower()
try:
	print(london_co[mode][config])
except:
	print("Такого параметра нет")
