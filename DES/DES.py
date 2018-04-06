from Cryptodome.Cipher import DES


# Считываемтекст с файла
def get_text():
    with open("text_lab2.txt", 'br') as text_file:
        return text_file.read()


# Добавляем дополнительные байты, если их число не кратно 8
def pad(byte_array):
    while len(byte_array) % 8 != 0:
        byte_array += b'\x00'
    return byte_array


def des_encrypt(des_obj, text, file):
    padded_text = pad(text)

    encrypted_text = des_obj.encrypt(padded_text)
    with open(file, 'wb') as f1:
        f1.write(encrypted_text)


def des_decrypt(des_obj, file_encrypt, file_decrypt):
    with open(file_encrypt, 'rb') as f1:
        s = f1.read()

    dec_text = des_obj.decrypt(s)

    with open(file_decrypt, 'wb') as f1:
        f1.write(dec_text)


if __name__ == '__main__':
    # Задаем мод шифрования
    key = b'asterisk'  # Ключевое слово
    des = DES.new(key, DES.MODE_ECB)

    text = get_text()
    file_name_encrypt = "text_encrypt_DES.txt"
    file_name_decrypt = "text_decrypt_DES.txt"

    des_encrypt(des, text, file_name_encrypt)
    des_decrypt(des, file_name_encrypt, file_name_decrypt)

