text = input("Input text: ")

# klucz = [' ','x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w']

def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)

        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result

s = 3
print("Text  : " + text)
print("Shift : " + str(s))
print("Cryptec: " + encrypt(text, s))