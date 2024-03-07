# 3DST-Converter:
- Previously known as: **PNG-2-3DST**.
- This is a script that takes advantage of `ETC2_ABGR` and `ETC2_RGBA` to Convert Multiple Formats to 3DST.

## Script Usage:
```
Convert 3DST to Image:   --convert2image,   -c2i
Convert Image to 3DST:   --image2raw,       -i2r
Show Image:              --show-true,       -st
Don't Show Image:        --show-false,      -sf (Alternatively, Leave it blank).

*** Show Images ONLY work for '--convert2image' or '-c2i'.
```

<br>
<br>
<br>

### Example Usage:
- **Convert ^.3DST to ^.PNG:**
```
python.exe etc_converter.py "sunset.3dst" --convert2image --show-true
```
- **Convert ^.PNG to ^.3DST:**
```
python.exe etc_converter.py "isz_screen.png" --image2raw -sf
```
- **Convert Other Formats to ^.3DST:**
```
python.exe etc_converter.py "sunset.jpg" --image2raw -sf
python.exe etc_converter.py "isz_screenshot.bmp" --image2raw -sf
python.exe etc_converter.py "texture_ui.tiff" --image2raw -sf
```

<br>
<br>
<br>

## Feature(s):
- Converts multiple image formats into a raw `ETC_ABGR/ETC_RGBA` *.3dst image for Minecraft3DS Modding.
- Supports the following Image Formats:
```
*.png
*.jpg, *.jpeg, *.jfif
*.gif
*.bmp
*.tiff, *.tif
*.ico, *.icon
*.webp
*.jp2, *.j2k
```
