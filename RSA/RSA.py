from Cryptodome.PublicKey import RSA

code = 'nooneknows'
key = RSA.generate(2048)  # генерируем ключ на 2048 бит

# Задаем настройки для приватного ключа
encrypted_key = key.exportKey(
    passphrase=code,
    pkcs=8,
    protection="scryptAndAES128-CBC"
)

# Записываем результаты в файлы
with open('my_private_rsa_key.bin', 'wb') as f:
    f.write(encrypted_key)

with open('my_rsa_public.pem', 'wb') as f:
    f.write(key.publickey().exportKey())

