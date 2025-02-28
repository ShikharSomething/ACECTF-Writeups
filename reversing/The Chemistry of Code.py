from binascii import unhexlify, hexlify
from base64 import b64decode
from Crypto.Util.number import long_to_bytes

# Given values
username = "AdminFeroxide"
password_b64 = "NjQzMzcyNzUzNTM3MzE2Njc5MzE2ZTM2"
alkaline_secret_hex = "4143454354467B34707072336E373163335F3634322C28010D3461302C392E"

# Decode password from Base64
password_hex = b64decode(password_b64).decode()

# Convert username to hex
username_hex = hexlify(username.encode()).decode()

# Convert values to integers
username_int = int(username_hex, 16)
password_int = int(password_hex, 16)
alkaline_secret_int = int(alkaline_secret_hex, 16)

# XOR operations
covalent_link = username_int ^ password_int
metallic_alloy = covalent_link ^ alkaline_secret_int

# Convert result back to ASCII (flag)
flag = long_to_bytes(metallic_alloy).decode(errors="ignore")
print("Flag:", flag)
