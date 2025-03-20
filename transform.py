import json


''' EARLY EXPERIMENTS FOR POTENTIAL FUTURE REFERENCE '''

def transform(s: str):
    s = s[2:] # remove U+
    s = s.lower() # lowercase it
    padding = "0" * (4 - len(s)) # pad the beginning if it's too short
    return f"\\u{padding}{s}"

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield "".join(lst[i:i + n])

with open("./glyphs.json", "r",  encoding="utf-8") as f:
    jsn = json.load(f)

glyphs = jsn["glyphs"]
i = "unicodeCode"

# get the unicodeCodes of the accented glyphs, but only non UTF-32 ones
accented = [transform(x[i]) for x in glyphs if x["fileName"] == "accented.png" and len(x) < 7]
accented = accented[:1024] # only need the first 1024 chars

advances = {}
for x in accented:
    advances[x] = 1

font = {
    "providers" : [
        {
            "type": "bitmap",
            "file": "mclivefx:font/pxl.png",
            "ascent": 0,
            "height": 1,
            "chars": list(chunks(accented, 32))
        },
        {
            "type": "space",
            "advances": advances
        }
    ]
}

with open('pxl.json', 'w', encoding='utf-8') as f:
    json.dump(font, f, ensure_ascii=False, indent=4)
