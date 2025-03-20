import math

from PIL import Image


def rgb_from_hex(h):
    h = str(h)
    h = h[2:] # remove 0x
    padding = "0" * (3 - len(h)) # pad the beginning if it's too short
    h = padding + h

    # multiply values by 16 to scale to 24 bit color values
    # subtract 1 so values are within range of 0-255
    r = int(f"0x{h[2]}", 16) * 16
    g = int(f"0x{h[1]}", 16) * 16
    b = int(f"0x{h[0]}", 16) * 16

    return tuple([int(max(r - 1, 0)), int(max(g - 1, 0)), int(max(b - 1, 0))])


if __name__ == '__main__':
    d = 64 # d x d resolution
    with Image.new('RGB', (d, d)) as im:
        pixels = [rgb_from_hex(hex(x)) for x in range(0, 0xFFF + 1)]

        for p in range(len(pixels)):
            x = (p % d)
            y = int((math.floor(p / d) / (d - 1)) * (d - 1))
            im.putpixel((x, y), pixels[p])

        print(len(set(im.getdata()))) # ensure no duplicate colors
        im.save("pxl.png")
