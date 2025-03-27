import json
import time

import PIL.Image


def rgb_to_hex(rgb: tuple):
    r = round(rgb[0] / 16)
    g = round(rgb[1] / 16)
    b = round(rgb[2] / 16)
    pxl = ((b * (16 * 16)) + (g * 16) + r) + 0xFFF
    return chr(pxl)


img = PIL.Image.open("pxl.png")
if img.mode != "RGB":
    img = img.convert("RGB")
    print("converted image to RGB mode")

pixels = img.load()

start = time.process_time()

chars = [rgb_to_hex(x) for x in img.getdata()]
for i in range(len(chars)):
    if i+1 == len(chars):
        break
    if ord(chars[i+1]) - ord(chars[i]) != 1:
        print(f"{chars[i]}, {chars[i+1]}")

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
