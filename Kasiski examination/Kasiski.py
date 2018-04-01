import string

alphabet = string.ascii_lowercase


def find_index_of_max(count):
    """
    find index of max concurrences
    """
    max_count = max(count)
    index_max_count = count.index(max_count)
    return index_max_count + 1


def find_key_length(text_encrypt):
    """
    find key length (we check length from 1 to 7)
    """
    list_of_counts = []

    for i in range(1, 7):
        count = 0
        with open(text_encrypt, 'r') as first_ecr_text:
            with open(text_encrypt, 'r') as second_ecr_text:
                for j in range(i):
                    poriv = second_ecr_text.read(1)
                    while poriv.lower() not in alphabet or len(poriv) == 0:
                        if len(poriv) == 0:
                            second_ecr_text.seek(0)
                        poriv = second_ecr_text.read(1)

                symbol = first_ecr_text.read(1)
                while symbol.lower() not in alphabet:
                    symbol = first_ecr_text.read(1)

                while symbol:
                    poriv = second_ecr_text.read(1)
                    while poriv.lower() not in alphabet or len(poriv) == 0:
                        if len(poriv) == 0:
                            second_ecr_text.seek(0)
                        poriv = second_ecr_text.read(1)

                    if symbol == poriv:
                        count += 1

                    symbol = first_ecr_text.read(1)
                    if symbol:
                        while symbol.lower() not in alphabet:
                            symbol = first_ecr_text.read(1)
                            if not symbol:
                                break

            # print("count for", i, "coincidedо=", count, "\n")
            list_of_counts.append(count)

    return list_of_counts


def init_groups_lists(list_groups, key_length):
    """
    We have count of groups = len(key_word)
    and init groups with list (like alphabet, 26 elements)
    """
    for i in range(key_length):
        list_groups.append([])
        for j in range(len(alphabet)):
            list_groups[i].append(0)

    return list_groups


def add_symbols_to_groups(text_encrypt, lists_of_groups, key_length):
    """
    Add symbols to groups from text
    """
    with open(text_encrypt, 'r') as f:
        iterator = 0
        s = f.read(1)
        while s.lower() not in alphabet:
            s = f.read(1)

        while s:
            index = alphabet.find(s.lower())
            lists_of_groups[iterator % key_length][index] += 1
            iterator += 1

            s = f.read(1)
            if s:
                while s.lower() not in alphabet:
                    s = f.read(1)
                    if not s:
                        break

    return lists_of_groups


def find_letter(list_of):
    """
     find letter of key_word using information
     that e is the most used character
     and e has index 4.
    """
    max_l = max(list_of)
    max_id = list_of.index(max_l)

    if max_id - 4 >= 0:
        delta = max_id - 4
    else:
        delta = 26 + max_id - 4

    return alphabet[delta]


def find_encrypt_key(text_encrypt="text_encrypt.txt"):
    """
    Find key_word using Kasiski examination
    """
    key_length = find_index_of_max(find_key_length(text_encrypt))
    lists_of_groups = init_groups_lists([], key_length)
    lists_of_groups = add_symbols_to_groups(text_encrypt, lists_of_groups, key_length)

    print(lists_of_groups)
    print(max(lists_of_groups[0]))

    found_key_word = ""
    for i in range(len(lists_of_groups)):
        found_key_word += find_letter(lists_of_groups[i])
    print("Key word:", found_key_word)
    return found_key_word


def decrypt_text(text_file, encrypted_text, key_word):
    """
    Decrypt text with found key_word
    """
    with open(encrypted_text, 'w') as encr_file:
        with open(text_file, 'r') as t_file:
            symbol = t_file.read(1)
            count = 0
            while symbol:
                if symbol.lower() in alphabet:
                    if symbol.islower():
                        index_word = alphabet.index(symbol)
                        index_key = alphabet.index(key_word[count])
                        if index_word - index_key >= 0:
                            encr_file.write(alphabet
                                            [(index_word - index_key) % 26])
                        else:
                            encr_file.write(alphabet
                                            [(26 + index_word - index_key) % 26])
                    else:
                        lower_s = symbol.lower()
                        index_word= alphabet.index(lower_s)
                        index_key = alphabet.index(key_word[count])
                        if index_word - index_key >= 0:
                            encr_file.write(alphabet
                                            [(index_word - index_key) % 26].upper())
                        else:
                            encr_file.write(alphabet
                                            [(26 + index_word - index_key) % 26].upper())

                    count = (count + 1) % len(key_word)
                else:
                    encr_file.write(symbol)
                symbol = t_file.read(1)


key_word = "game"
vigenere_cipher("text.txt", "text_encrypt.txt", key_word)
find_key = find_encrypt_key()
print(find_key)
decrypt_text("text_encrypt.txt", "decrypt.txt", find_key)



