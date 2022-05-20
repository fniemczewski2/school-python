
U1 = {'imie': 'Piotr', 'nazwisko': 'Nowak', ' klasa': '1A', 'wiek': 7, 'numer': 10}
U2 = {'imie': 'Krzysztof', 'nazwisko': 'Kowalski', 'klasa': '2B', ' wiek': 8, 'numer': 12}
U3 = {'imie': 'Andrzej', 'nazwisko': 'Wiśniewski', 'klasa': '3C', ' wiek': 9, 'numer': 14}
U4 = {'imie': 'Anna', 'nazwisko': 'Kowalczyk', 'klasa': '4D', 'wiek': 10, 'numer': 16}
U5 = {'imie': 'Maria', 'nazwisko': 'Kamińska', 'klasa': '5E', 'wiek': 11, 'numer': 18}
U6 = {'imie': 'Katarzyna', 'nazwisko': 'Lewandowska', 'klasa': '6F', 'wiek': 12, 'numer': 20}

uczniowie = {1: U1, 2: U2, 3: U3, 4: U4, 5: U5, 6:U6}

for nbr, id in uczniowie.items():
    print("\n\n Uczeń/Uczennica:" )
    for key, value in id.items():
        if key == 'wiek':
            print("\t", key, "\b:   \t", value, "lat")
        else:
            print("\t", key, "\b:   \t", value)
    
