alphabet = string.ascii_lowercase

def vigenere_cipher(text_file, encrypted_text, key_word):
	"""
	Encrypt text using vigener cipher
	"""
    with open(encrypted_text, 'w') as encr_file:
        with open(text_file, 'r') as t_file:
            symbol = t_file.read(1)
            count = 0
            while symbol:
                # check if symbol is uppercase, because we want to save Uppercase symbols in text
                if symbol.lower() in alphabet:
                    if symbol.islower():
                        index_word = alphabet.index(symbol)
                        index_key = alphabet.index(key_word[count])
                        # % 26 - the number of characters in the alphabet
                        encr_file.write(alphabet[(index_word + index_key) % 26])
                    else:
                        lower_s = symbol.lower()
                        index_word = alphabet.index(lower_s)
                        index_key = alphabet.index(key_word[count])
                        encr_file.write(alphabet[(index_word + index_key) % 26].upper())
                    count = (count + 1) % len(key_word)
                else:
                    encr_file.write(symbol)
                symbol = t_file.read(1)

key_word = "game"
vigenere_cipher("text.txt", "text_encrypt.txt", key_word)
