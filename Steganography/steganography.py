from PIL import Image


def create_symbol_bin_code(symbol):
    """
    Создаем бинарный код символа, при необходимости дополняем старшие биты нулями
    """
    len_bits = bin(ord(symbol))[2::]
    extra_zero = "0b"
    for i in range(len(len_bits), 8):
        extra_zero += "0"

    return extra_zero + len_bits


def create_number_bin_code(number):
    """
    Создаем бинарный код числа, при необходимости дополняем старшие биты нулями
    """
    len_bits = bin(number)[2::]

    extra_zero = "0b"
    for i in range(len(len_bits), 8):
        extra_zero += "0"

    return extra_zero + len_bits


def set_data_to_picture(file_name, message):
    """
    Записываем данные в картинку (за алгоритмом LSB) и
    возвращаем новую картинку с записанными результатами
    """
    img = Image.open(file_name)
    length, width = img.size
    im = Image.new("RGB", (length, width))
    pixels_new = im.load()
    iterator = 0
    rgb_im = img.convert('RGB')

    for symbol in message:
        bin_code = create_symbol_bin_code(symbol)
        # print("Symbol:", symbol, " -->", bin_code)
        for i in range(0, 8, 2):
            red, green, blue = rgb_im.getpixel((iterator % length, iterator // length))
            # print("x, y:", (iterator % length, iterator // length), "Value:", (red, green, blue))
            bits = bin_code[2 + i: i + 4]
            int_number = int(bits, 2)
            result = int_number | ((255 << 2) & red), int_number | ((255 << 2) & green), int_number | ((255 << 2) & blue)
            # print("New pixel. x, y:", (iterator % length, iterator // length), "Value:", result)
            pixels_new[iterator % length, iterator // length] = result
            iterator += 1

    while iterator < length * width:
        pixels_new[iterator % length, iterator // length] = rgb_im.getpixel((iterator % length, iterator // length))
        iterator += 1

    result_file = open("encrypted.bmp", "wb")
    im.save(result_file, "BMP")
    return "encrypted.bmp"


def get_data_from_picture(file_name):
    """
    Считываем данные из картинки за алгоритмом LSB
    """
    img = Image.open(file_name)
    length, width = img.size
    rgb_im = img.convert('RGB')
    symbol = "0b"
    text = ""
    for i in range(length * width):
        red, green, blue = rgb_im.getpixel((i % length, i // length))
        symbol += create_number_bin_code(red)[-2::]
        if len(symbol) == 10:
            text += chr(int(symbol, 2))
            symbol = "0b"

    return text


def main():
    with open("message.txt", "r") as f:
        message = f.read()
    result = set_data_to_picture("testik.bmp", message)
    print(get_data_from_picture(result))

if __name__ == '__main__':
    main()
