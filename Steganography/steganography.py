from PIL import Image


def create_bin_code(symbol):
    len_bits = bin(ord(symbol))[2::]
    extra_zero = "0b"
    for i in range(len(len_bits), 8):
        extra_zero += "0"

    return extra_zero + len_bits

message = "Hello!"
im = Image.new("RGB", (100, 100))
pixelsNew = im.load()

img = Image.open("testik.bmp")

iterator = 0
rgb_im = img.convert('RGB')
for symbol in message:
    bin_code = create_bin_code(symbol)
    print("Symbol:", symbol, " -->", bin_code)
    for i in range(0, 8, 2):
        pixel_r, p2, p3 = rgb_im.getpixel((iterator % 100, iterator // 100))
        print("x, y:", (iterator % 100, iterator // 100), "Value:", pixel_r, p2, p3)
        bits = bin_code[2 + i: i + 4]
        int_number = int(bits, 2)
        result = int_number | pixel_r, int_number | p2, int_number | p3

        pixelsNew[iterator % 100, iterator // 100] = result
        iterator += 1


f = open("encrypted.bmp", "wb")
im.save(f, "BMP")
rgb_im = im.convert('RGB')

for i in range(12):
    pixel_r, p2, p3 = rgb_im.getpixel((i, 0))
    print("x, y:", (i, 0), "Value:", pixel_r, p2, p3)




