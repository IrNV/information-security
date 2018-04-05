from Cryptodome.Cipher import DES

key = b'aaaaaaaa' # Ключевое слово


# Считываемтекст с файла
def get_text():
    with open("text_lab2.txt", 'br') as text_file:
        return text_file.read()


# Добавляем дополнительные байты, если их число не кратно 8
def pad(text):
    while len(text) % 8 != 0:
        text += b'\x00'
    return text

des = DES.new(key, DES.MODE_ECB)
text = get_text()
padded_text = pad(text)


encrypted_text = des.encrypt(padded_text)

with open("text_encrypt!.txt", 'wb') as f1:
    f1.write(encrypted_text)

s = bytes
with open("text_encrypt!.txt", 'rb') as f1:
    s = f1.read()

dec_text = des.decrypt(s)
print("Dec text:", dec_text)
