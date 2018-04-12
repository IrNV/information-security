import rsa
from hashlib import sha1
import random


def create_symmetric_key():
    """
    Создаем случайный ключ из случайно последовательности чисел
    """
    random_numbers = [str(i) for i in range(40)]
    random.shuffle(random_numbers)

    return ",".join(random_numbers)


def symmetric_encryption(key_symmetric, message):
    """
    Шифруем простой перестановкой
    """
    encrypted_message = list(message)
    key = key_symmetric.split(",")

    for i, v in enumerate(message):
        new_position = key[i]
        encrypted_message[int(new_position)] = chr(v)

    return "".join(encrypted_message)


def symmetric_decryption(key_symmetric, message):
    """
    Дешифруем простую перестановку
    """
    decrypted_message = list(message)
    key = key_symmetric.split(",")

    for i, v in enumerate(key):
        decrypted_message[i] = chr(message[int(v)])

    return "".join(decrypted_message)


def get_bob_message(alice_pub):
    """
    Формируем сообщение от Боба, зашифрованный простой перестановкой хеш этого сообщения и
    зашифрованный ключ простой перестановки шифром rsa.
    """
    message = 'hello Alice!'.encode('utf8')
    hash_message = sha1(message)

    key_symmetric = create_symmetric_key()  # Создаем ключ для простой перестановки

    # Шифруем хеш
    encrypted_hash = symmetric_encryption(key_symmetric, hash_message.hexdigest().encode("utf8"))

    # Шифруем ключ симметрического шифрования (шифр простой перестановки)
    encrypted_symmetric_key = rsa.encrypt(key_symmetric.encode('utf8'), alice_pub)

    return message, encrypted_hash, encrypted_symmetric_key


def alice_function():
    (alice_pub, alice_priv) = rsa.newkeys(1024)
    message, encrypted_hash, encrypted_symmetric_key = get_bob_message(alice_pub)

    print("Alice receive from Bob message:", message)
    print("Alice receive from Bob encrypted hash:", encrypted_hash)
    print("Alice receive from Bob encrypted symmetric key:", encrypted_symmetric_key)

    symmetric_key = rsa.decrypt(encrypted_symmetric_key, alice_priv)
    print("Alice has decrypted Bob's key by her private key:", symmetric_key)
    decrypted_hash = symmetric_decryption(symmetric_key.decode('utf8'), encrypted_hash.encode("utf8"))
    print("Alice has decrypted hash by symmetric key:", decrypted_hash)

    if decrypted_hash == sha1(message).hexdigest():
        print("\n")
        print("decrypted hash:", decrypted_hash)
        print("sh1(message from Bob):", sha1(message).hexdigest())
        print("Alice receive right message!")


def main():
    alice_function()

if __name__ == '__main__':
    main()
