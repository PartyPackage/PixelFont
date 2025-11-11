'''
    This program generates a test command to be used in a command block which spawns a text display of the provided test image.
    Copyright 2025 Thomas Davidson

    This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
    This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
'''


import json
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
    row = [""]
    for c in range(img.width):
        row.append(chars.pop(0))

    rows.append(" ".join(row) + " \n")

text = json.dumps("".join(rows))
command = f"/summon minecraft:text_display ~ ~2 ~ {{line_width: 2056, text: {{font: \"lfx:pxl\", text: {text[:-3] + "\""}}}}}" # it's hacky, i know

with open("test_command.txt", "w") as f:
    f.write(command)

print("generated command in test_command.txt")
