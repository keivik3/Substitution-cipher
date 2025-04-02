import math
def encrypt(text, key_1, key_2):
    if math.gcd(key_1[0], 26) != 1:
        return "Некорректный ключ"
    if math.gcd(key_2[0], 26) != 1:
        return "Некорректный ключ"
    a = key_1[0] % 26
    b = key_1[1] % 26
    a1 = key_2[0] % 26
    b1 = key_2[1] % 26
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    text = list(text)
    text_num = []
    for i in range(len(text)):
        text_num.append(alphabet.index(text[i]))
        i += 1
    key_3 = [0, 0]
    for i in range(len(text_num)):
        text_num[i] = (text_num[i] * a + b) % 26
        key_3[0] = (a * a1) % 26
        key_3[1] = (b + b1) % 26
        key_1 = key_2
        key_2 = key_3
        key_3 = [0, 0]
    encrypted_text = []
    for i in range(len(text_num)):
        encrypted_text.append(alphabet[text_num[i]])
        i += 1
    return "".join(encrypted_text)


def decrypt(text, key_1, key_2):
    if math.gcd(key_1[0], 26) != 1:
        return "Некорректный ключ"
    if math.gcd(key_2[0], 26) != 1:
        return "Некорректный ключ"
    a = key_1[0] % 26
    b = key_1[1] % 26
    a1 = key_2[0] % 26
    b1 = key_2[1] % 26
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    text = list(text)
    text_num = []
    for i in range(len(text)):
        text_num.append(alphabet.index(text[i]))
        i += 1
    key_3 = [0, 0]
    for i in range(len(text_num)):
        n = 1
        while (True):
            if int(n/a) == n/a:
                n = n/a
                break
            n += 26
        text_num[i] = int(((text_num[i] - b) * n) % 26)


        key_3[0] = (a * a1) % 26
        key_3[1] = (b + b1) % 26
        key_1 = key_2
        key_2 = key_3
        key_3 = [0, 0]
    decrypted_text = []
    for i in range(len(text_num)):
        decrypted_text.append(alphabet[text_num[i]])
        i += 1
    return "".join(decrypted_text)




key_1 = [3, 5]
key_2 = [7, 4]
text = input("Введите текст: ")
print("Ключи: ", key_1, key_2)
print('Текст после зашифровки: ', encrypt(text, key_1, key_2))
print('Текст после расшифровки: ', decrypt(input("Введите текст для расшифрования:"), key_1, key_2))
