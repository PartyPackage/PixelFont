'''
    This program generates a custom font for a minecraft resource pack that provides
    unicode characters of individual colors of a 12 bit color space.
    Copyright 2025 Thomas Davidson

    This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
    This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
'''


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
    "attribution": "Copyright 2025 Thomas Davidson",
    "providers" : [
        {
            "type": "bitmap",
            "file": "lfx:font/pxl.png",
            "ascent": 8,
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
