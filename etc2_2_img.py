from PIL import Image
import os
import struct

def convert_etc2_2_png(etc2_file_path, width, height):
    with open(etc2_file_path, 'rb') as f:
        f.seek(0x20)
        etc2_data = f.read()

    image = Image.new('RGBA', (width, height))
    block_size = 8
    offset = 0
    for y in range(0, height, block_size):
        for x in range(0, width, block_size):
            for block_y in range(block_size):
                for block_x in range(block_size):
                    if offset + 4 <= len(etc2_data):
                        a, b, g, r = struct.unpack_from('BBBB', etc2_data, offset)
                        image.putpixel((x + block_x, y + block_y), (r, g, b, a))
                        offset += 4

    return image

etc2_file_path = input("Paste Path to *.3DST Image: ")

if '"' in etc2_file_path:
    etc2_file_path = etc2_file_path.replace('"','')

with open(etc2_file_path,'rb+') as of:
    of.seek(0x0C)
    width_b = of.read(0x04)
    of.seek(0x10)
    height_b = of.read(0x04)
    
    width = int.from_bytes(width_b, byteorder='little')
    height = int.from_bytes(height_b, byteorder='little')
    print(f"\nImage Demesions: {width}x{height}\n")
    of.close()

image = convert_etc2_2_png(etc2_file_path, width, height)

image.save('yourImage_reconstructed.png')
print(f"Output Image to: 'youImage_reconstructe.png'.")

if os.name == 'nt':
    os.system('pause')