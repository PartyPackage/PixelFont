import json


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield "".join(lst[i:i + n])


'''
    Each pixel is represented as 0xBGR, giving us 4096 possible colors.
    Starting at 0xFFF to avoid weird formatting codes.
'''
codes = [chr(x) for x in range(0xFFF, 0xFFF + 0xFFF + 1)]

advances = {
    " ": -1
}
for x in codes:
    advances[x] = 10

font = {
    "providers" : [
        {
            "type": "bitmap",
            "file": "lfx:font/pxl.png",
            "ascent": 3,
            "height": 10,
            "chars": list(chunks(codes, 64)) # 64x64 palette image
        },
        {
            "type": "space",
            "advances": advances
        }
    ]
}

with open('pxl.json', 'w', encoding='utf8') as f:
    json.dump(font, f, ensure_ascii=True, indent=4)
    print("generated font: pxl.json")
