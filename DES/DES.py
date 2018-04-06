from Cryptodome.Cipher import DES
from Cryptodome.Cipher import DES3


def get_text():
    """
    Считываемтекст с файла
    """
    with open("text_lab2.txt", 'br') as text_file:
        return text_file.read()


def pad(byte_array):
    """
    Добавляем дополнительные байты, если их число не кратно 8
    """
    while len(byte_array) % 8 != 0:
        byte_array += b'\x00'
    return byte_array


def des_encrypt(des_obj, text, file):
    """
    Шифрование данных
    """
    padded_text = pad(text)

    encrypted_text = des_obj.encrypt(padded_text)
    with open(file, 'wb') as file_encrypt:
        file_encrypt.write(encrypted_text)


def des_decrypt(des_obj, file_encrypt, file_decrypt):
    """
    Разшифрование данных
    """
    with open(file_encrypt, 'rb') as f_encrypt:
        s = f_encrypt.read()

    dec_text = des_obj.decrypt(s)

    with open(file_decrypt, 'wb') as f_decrypt:
        f_decrypt.write(dec_text)


if __name__ == '__main__':
    # Задаем мод шифрования
    key = b'asterisk'  # Ключевое слово 8 байт
    des = DES.new(key, DES.MODE_ECB)

    text = get_text()
    file_name_encrypt = "text_encrypt_DES.txt"
    file_name_decrypt = "text_decrypt_DES.txt"

    des_encrypt(des, text, file_name_encrypt)
    des_decrypt(des, file_name_encrypt, file_name_decrypt)

    # 3DES #
    key = b'GRRichard Martin'  # Ключевое слово 16 байт
    des = DES3.new(key, DES3.MODE_ECB)

    text = get_text()
    file_name_encrypt = "text_encrypt_3DES.txt"
    file_name_decrypt = "text_decrypt_3DES.txt"
    des_encrypt(des, text, file_name_encrypt)
    des_decrypt(des, file_name_encrypt, file_name_decrypt)



