geo = {}
geo["Poland"] = ("Warsaw", 37.9)
geo["Russia"] =  ("Moscow", 144.1)
geo["England"] = ("London", 55.9)
geo["France"] = ("Paris", 67.4)
geo["Germany"] = ("Berlin", 83.2)

for country in geo.keys():
    print(country)

def show_info(country):

    info = geo[country]

    print(country)
    print("Stolica: " + info[0])
    print("Ludność: " + str(info[1]))

country = input("Wybierz kraj: ")
show_info(country)
