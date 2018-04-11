import rsa


def get_bob_message(alice_pub):
    message = 'hello Alice!'.encode('utf8')
    crypto = rsa.encrypt(message, alice_pub)

    return crypto


def alice_function():
    (alice_pub, alice_priv) = rsa.newkeys(512)
    message = rsa.decrypt(get_bob_message(alice_pub), alice_priv)

    print(message)


def main():
    alice_function()

if __name__ == '__main__':
    main()