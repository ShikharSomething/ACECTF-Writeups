expected = "GRX14YcKLzXOlW5iaSlBIrN7"
key = [0x06, 0x11, 0x1d, 0x72, 0x60, 0x1f, 0x18, 0x7c, 0x3e, 0x0f] + [ord(c) for c in "mx35@^>%_0x"] + [0x14, 0x37, 0x4a]

# Recover the original input
original = "".join(chr(ord(e) ^ k) for e, k in zip(expected, key))

print("Recovered Input:", original)
