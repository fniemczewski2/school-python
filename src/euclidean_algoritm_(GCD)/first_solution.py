while True:
    nbr1 = int(input('First number: '))
    nbr2 = int(input('Second number: '))

    if nbr1 == 0:
        print("GCD: ", nbr2)

    elif nbr2 == 0:
        print("GCD: ", nbr1)

    else:
        while nbr1 != nbr2:
            if nbr1 > nbr2:
                nbr1 -= nbr2
            else:
                nbr2 -= nbr1

        print("GCD: ", nbr1)
