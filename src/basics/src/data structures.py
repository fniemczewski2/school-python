print()
print("Krotka:")

krotka = ('tomek', 'franek', 'kuba', 'tomek', 'marcin') #modyfikacja nie możliwa, uporządkowane
print(krotka)

print()
print("Sety:")

set = {'tomek', 'franek', 'kuba', 'marcin'} #duplikaty nie możliwe, nieuporządkowane
print(set)

set.add('bartek') #add zamiasta append
set.discard('bartek') #usuń, jeżelli istnieje
set.remove('kuba') #usuń
set2 = {'piotr', 'bartek'}
set3 = set.union(set2) #lączenie

print()
print(set.update(set2))
print(set.difference(set2))
print(set.intersection(set2))
print(set.symmetric_difference(set2))

print()
print("Listy:")

lista = ['tomek', 'franek', 'kuba', 'tomek', 'marcin'] #modyfikacja i duplikaty możilwe, nieuporządkowane
print(lista)

lista2 = ['piotr', 'bartek']
print(lista2)

lista3 = lista + lista2
print(lista3)

lista.append('jan') #dodawanie elementu
print(lista)

for imie in lista: #wyswietlenie kazdego elementu osobno
    print(imie)

lista.reverse() #odwrócenie kolejności
for imie in lista:
    print(imie)

lista.sort() #sortowanie
for imie in lista:
    print(imie)

lista.sort(reverse=True) #sortowanie
for imie in lista:
    print(imie)

print(imie[0]) #wyswietlenie konkretnego elementu

print(lista.count('tomek')) #ile razy element wystepuje 

print(len(lista)) #ile razy element wystepuje 

print(lista.pop(0)) #wypisanie i usuwanie elementu

lista.remove('tomek') #usuwanie jednego elementu
print(lista) 

lista.clear #czyszczenie listy
print(lista)

print()
print("Słownik:")

geografia = {"Poland": "Warsaw", "Russia": "Moscow", "USA": "Washington D.C.", "England": "London", "France": "Paris", "China": "Beijing"}
geografia["Japan"] = "Tokyo"

for kraje in geografia.keys():
    print(kraje)

for stolice in geografia.values():
    print(stolice)

for kraje, stolice in geografia.items():
    print(kraje + " - " + stolice)

print(geografia['Poland']) #jeżeli nie znajdzie, będzie błąd
print(geografia.get('Poland')) #jeżeli nie znajdzie, będzie None

if "Poland" in geografia:
    print("Znaleziono")
else:
    print("Nie znaleziono")



