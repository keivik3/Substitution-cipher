from math import *

def encrypt(text, key):
    if gcd(key[0], 26) != 1:
        return "Некорректный ключ"
    a = key[0] % 26
    b = key[1] % 26
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    text = list(text)
    text_ind = []
    for i in range(len(text)):
        text_ind.append(alphabet.index(text[i]))
        i += 1
    for i in range(len(text_ind)):
        text_ind[i] = (text_ind[i] * a + b) % 26
    encrypted_text = []
    for i in range(len(text)):
        encrypted_text.append(alphabet[text_ind[i]])
        i += 1
    return "".join(encrypted_text)

def decrypt(text, key):
    if gcd(key[0], 26) != 1:
        return ("Некорректный ключ")
    a = key[0] % 26
    b = key[1] % 26
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    text = list(text)
    text_ind = []
    for i in range(len(text)):
        text_ind.append(alphabet.index(text[i]))
        i += 1
    for i in range(len(text_ind)):
        n = 1
        while True:
            if (a * n) % 26 == 1:
                text_ind[i] = (n *(text_ind[i] - b) % 26)
                break
            n += 1
    decrypted_text = []
    for i in range(len(text)):
        decrypted_text.append(alphabet[text_ind[i]])
        i += 1
    return "".join(decrypted_text)

key = [3, 3]
text = input("Введите текст: ")
print("Основной ключ: ", key)
print("Зашифрованный текст: ", encrypt(text, key))
print("Расшифрованный текст: ", decrypt(input("Введите текст для расшифрования: "), key))
