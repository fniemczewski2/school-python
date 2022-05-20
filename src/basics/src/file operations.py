file = open("..\files\geo.txt",  "w+")
geo = {}
geo["Poland"] = ("Warsaw", 37.9)
geo["Russia"] =  ("Moscow", 144.1)
geo["England"] = ("London", 55.9)
geo["France"] = ("Paris", 67.4)
geo["Germany"] = ("Berlin", 83.2)

for country, info in geo.items():
    file.write(country + " - Stolica: " + info[0] + ", Ludnosc: " + str(info[1]) + "\n")

file.close()


file = open("geo.txt")

for line in file.readlines():
    print(line.strip())
    
file.close()