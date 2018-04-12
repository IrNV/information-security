import rsa
from hashlib import sha1
import random


def symetric():
    random_numbers = [str(i) for i in range(40)]
    random.shuffle(random_numbers)

    return ",".join(random_numbers)


def symsetric_encryption(key_symetric, message):
    encrypted_message = list(message)
    key = key_symetric.split(",")

    print("me", message)
    print("key", key)
    for i, v in enumerate(message):
        new_positon = key[i]
        encrypted_message[int(new_positon)] = chr(v)

    print(encrypted_message)

    return "".join(encrypted_message)


def get_bob_message(alice_pub):
    message = 'hello Alice!'.encode('utf8')
    hash_message = sha1(message)
    print(hash_message.hexdigest())

    key_symetric = symetric()
    print(key_symetric)

    encrypted_hash = symsetric_encryption(key_symetric, hash_message.hexdigest().encode("utf8"))
    print("Encrypted_hash:", encrypted_hash)

    encrypted_key_symetric = rsa.encrypt(key_symetric.encode('utf8'), alice_pub)

    return message, encrypted_hash, encrypted_key_symetric


def alice_function():
    (alice_pub, alice_priv) = rsa.newkeys(1024)
    message, encrypted_hash, encrypted_key_symetric = get_bob_message(alice_pub)
    key_symetric = rsa.decrypt(encrypted_key_symetric, alice_priv)

    print(key_symetric)
    #print("asdasd".encode("utf8"))
    print(symsetric_encryption(key_symetric.decode('utf8'), encrypted_hash.encode("utf8")))


def main():
    alice_function()

if __name__ == '__main__':
    main()