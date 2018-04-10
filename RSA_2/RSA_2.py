def encrypt_word(word, n, e):
    """
    Шифруем слово открытым ключем
    """
    word_in_number = int.from_bytes(word, "big")
    return pow(word_in_number, e, n)


def decrypt_word(encrypted_word, d, n):
    """
    Расшифровываем слово закрытым ключем
    """
    return pow(encrypted_word, d, n)


def gcdex(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = gcdex(b, a % b)
        return d, y, x - y * (a // b)


def get_d(phi, e):
    """
    Находим d, которое будет удволетворять условию e*d + y*phi = 1
    т.е. используем алгоритм расширеный алгоритм Евклида
    """
    return gcdex(e, phi)[1] + phi


def convert_decrypted_word(decrypted):
    """
    Разбиваем число на байты и переводим байты в символы
    """
    word = ""
    hex_decrypted = hex(decrypted)
    for i in range(2, len(hex_decrypted), 2):
        word += chr(int((hex_decrypted[i: i + 2]).encode("utf8"), 16))

    return word


def main():
    p = 18496081
    q = 41752783
    e = 65537

    n = p * q
    phi = (p - 1) * (q - 1)

    d = get_d(phi, e)
    print("R:", d)

    encrypted_word = encrypt_word(b"Valera", n, e)
    print(encrypted_word)
    print(decrypt_word(encrypted_word, int(d), n))
    d_w = decrypt_word(encrypted_word, int(d), n)
    print(convert_decrypted_word(d_w))

if __name__ == '__main__':
    main()
