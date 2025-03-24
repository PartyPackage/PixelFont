import json
import time

import PIL.Image
import math


def rgb_to_hex(rgb: tuple):
    r = hex(math.floor(rgb[0] / 16))[2:]
    g = hex(math.floor(rgb[1] / 16))[2:]
    b = hex(math.floor(rgb[2] / 16))[2:]
    return chr(int(f"0x{b}{g}{r}", 16) + 0x100)


img = PIL.Image.open("test.png")
if img.mode != "RGB":
    img = img.convert("RGB")
    print("converted image to RGB mode")

pixels = img.load()

start = time.process_time()
chars = []
for x in range(img.width):
    for y in range(img.height):
        chars.append(rgb_to_hex(pixels[x,y]))

rows = []
while len(chars) >= img.width:
    row = []
    for c in range(img.width):
        row.append(chars.pop(0))

    rows.append(" ".join(row) + "\n")

x = int((img.height/2))
jsn = {
    "font": "lfx:pxl",
    "text": "".join(rows[:x])
}

command = f"/summon minecraft:text_display ~ ~2 ~ {{background:-16777216, line_width: 2056, text: '{json.dumps(jsn).replace("\\", "\\\\")}'}}"
print(command)
end = time.process_time()

ms = (end - start) * 10**3
print(f"{ms}ms")
