a = int(input('First number: '))
b = int(input('Second number: '))
while b > 0:
        a, b = b, (a % b)
print(a)
