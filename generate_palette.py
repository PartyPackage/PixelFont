'''
    This program generates a 12 bit color palette which is used by the custom font.
    Copyright 2025 Thomas Davidson

    This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
    This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
'''


import math
from PIL import Image


def int_to_rgb(i):
    # multiply values by 16 to scale to 24 bit color values
    # subtract 1 so values are within range of 0-255
    r = (i & 0xF) * 16
    g = ((i >> 4) & 0xF) * 16
    b = ((i >> 8) & 0xF) * 16

    return (r,g,b)


if __name__ == '__main__':
    d = 64 # d x d resolution
    with Image.new('RGB', (d, d)) as im:
        pixels = [int_to_rgb(x) for x in range(0, 0xFFF + 1)]

        for p in range(len(pixels)):
            x = (p % d)
            y = int((math.floor(p / d) / (d - 1)) * (d - 1))
            im.putpixel((x, y), pixels[p])

        im.save("pxl.png")
        print("generated palette: pxl.png")
