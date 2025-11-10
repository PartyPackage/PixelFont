import json
import time

import PIL.Image


def rgb_to_char(rgb: tuple):
    r = round(rgb[0] / 16)
    g = round(rgb[1] / 16)
    b = round(rgb[2] / 16)
    pxl = ((b * (16 * 16)) + (g * 16) + r) + 0xFFF
    return chr(pxl)


filename = "test.png"
img = PIL.Image.open(filename)
if img.mode != "RGB":
    img = img.convert("RGB")
    print("converted image to RGB mode")

chars = [rgb_to_char(x) for x in img.getdata()]

"""
    Remove whitespace in between pixels and add a newline to the end of the row
    (in this case, " " is negative space)
"""
rows = []
while len(chars) >= img.width:
    row = []
    for c in range(img.width):
        row.append(chars.pop(0))

    rows.append(" ".join(row) + "\n")

text = json.dumps("".join(rows))
command = f"/summon minecraft:text_display ~ ~2 ~ {{line_width: 2056, text: {{font: \"lfx:pxl\", text: {text}}}}}"

with open("test_command.txt", "w") as f:
    f.write(command)

print("generated command in test_command.txt")
