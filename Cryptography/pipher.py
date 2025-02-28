charset = "4bcd3f6h1jklmn0pqr57uvwxyz"

mapping = {
    "DC#": "A",
    "DD#": "C",
    "DF": "E",
    "EC": "T",
    "G#B": "{",

    "FC#": "_",
    "C#C#": "7",
    "CE": "0",
    "F#C": "h",
    "CF": "1",
    "C#C": "6",
    "C#B": "5",
    "C#A": "3",
    "F#A#": "f",
    "AF#": "n",
    "C#A#": "4",
    "GA#": "p",
    "GC": "r"
}

custom = {}

with open("./cipher.txt", "r") as f:
    keys = f.read().split()

for key in keys:
    if key in mapping:
        keys[keys.index(key)] = mapping[key]
    elif key.startswith("'"):
        keys[keys.index(key)] = chr(int(key[1:-1]))
    else:
        keys[keys.index(key)] = ' '
        if key not in custom:
            custom[key] = 1
        else:
            custom[key] += 1
print(''.join(keys))
print(custom)
