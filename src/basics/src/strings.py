name = "franek"

print(len(name)) #dlugosc

print(name.capitalize()) #pierwsza wielka
print(name.upper()) #wszytskie wielkie
print(name.lower()) #wszytskie małe

print(name[0]) #pierwsza litera
print(name[0:2]) #od 1 do 3
print(name[3:]) #od 4 do końca
print(name[-3]) #trzecia od konca

school = "Zespol Szkol Komunikacji"
print(school.split( )) #dzielenie

glue = " "
print(glue.join(['Zespol', 'Szkol', 'Komunikacji'])) #łączenie

print(school.startswith('Z')) #czy zaczyna się od
print(school.startswith('z')) 
print(school.endswith('I')) #czy kończy się na
print(school.endswith('i'))

#usuwanie liter
print(school.rstrip('Z')) #z prawej
print(school.lstrip('i')) #z lewej
print(school.strip('i')) #z obu stron
print(school.strip()) #usuwanie spacji
