import rsa


def get_d(phi, e):
    """
    Находим d, которое будет удволетворять условию i * phi + 1 делится  нацело на e
    """
    for i in range(1, e):
        x = (i * phi + 1)
        if x % e == 0:
            return x / e


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


def main():
    p = 18496081
    q = 41752783
    e = 65537

    n = p * q
    phi = (p - 1) * (q - 1)
    d = get_d(phi, e)

    encrypted_word = encrypt_word(b"Valera", n, e)
    print(encrypted_word)
    print(decrypt_word(encrypted_word, int(d), n))

if __name__ == '__main__':
    main()
