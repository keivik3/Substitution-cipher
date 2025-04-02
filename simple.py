def encrypt(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for char in text.lower():
        idx = alphabet.index(char)
        result += key[idx]

    return result
def decrypt(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for char in text.lower():
        idx = key.index(char)
        result += alphabet[idx]

    return result

key = "cdefghijklmnopqrstuvwxyzab"

open_text = input("Введите открытый текст: ")
print("Ключ: ", key)
print("Зашифрованный текст: ", encrypt(open_text, key))
encrypted_input = input("Введите зашифрованный текст: ")
print("Расшифрованный текст: ", decrypt(encrypted_input, key))
