from PIL import Image
import struct
import os

def convert_png_2_etc2(png_file_path):
    with Image.open(png_file_path) as image:
        if image.mode != 'RGBA':
            image = image.convert('RGBA')
        
        width, height = image.size
        etc2_data = bytearray()
        for y in range(0, height, 8):
            for x in range(0, width, 8):
                block_data = b''
                for block_y in range(8):
                    for block_x in range(8):
                        pixel = image.getpixel((x + block_x, y + block_y))
                        r, g, b, a = pixel
                        block_data += struct.pack('BBBB', a, b, g, r)

                etc2_data += block_data

        return bytes(etc2_data)


png_file_path = input("Paste Path to *.PNG/*.JPG/*.JFIF/*.GIF Image: ")

if '"' in png_file_path:
    png_file_path = png_file_path.replace('"','')

etc2_data = convert_png_2_etc2(png_file_path)

with open('yourImage.3dst','wb+') as f:
    f.write(etc2_data)


if os.name == 'nt':
    os.system('pause')
