numer = 1

while numer < 6:
    print(numer)
    numer +=1

for numer in range (1, 6):  #zakres <1;6) 
    print(numer) 

for numer in range (0, 11, 2): #zakres <0;11) krok 2
    print(numer)

for numer in range (0, 10): 
    if numer == 5: #przerwanie wykonywania dla 5, kontynuacja dla innych
        continue
    if numer == 9: #przerwanie przy 9
        break
    print(numer)

