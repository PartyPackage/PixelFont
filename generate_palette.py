import math

from PIL import Image


def int_to_rgb(i):
    # multiply values by 16 to scale to 24 bit color values
    # subtract 1 so values are within range of 0-255
    r = (i & 0x0F) * 16
    g = ((i >> 4) & 0x0F) * 16
    b = ((i >> 8) & 0x0F) * 16

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
