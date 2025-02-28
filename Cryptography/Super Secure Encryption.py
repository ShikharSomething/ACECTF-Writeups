from binascii import unhexlify

def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

# Given values (extract from msg.txt)
encrypted_msg = "d71f4a2fd1f9362c21ad33c7735251d0a671185a1b90ecba27713d350611eb8179ec67ca7052aa8bad60466b83041e6c02dbfee738c2a3"  # First ciphertext (hex) from msg.txt
encrypted_flag = "c234661fa5d63e627bef28823d052e95f65d59491580edfa1927364a5017be9445fa39986859a3"  # Second ciphertext (hex) from msg.txt
known_plaintext = b'This is just a test message and can totally be ignored.'

# Convert hex to bytes
C_msg = unhexlify(encrypted_msg)
C_flag = unhexlify(encrypted_flag)

# Recover keystream
keystream = xor_bytes(C_msg, known_plaintext)

# Decrypt flag
flag = xor_bytes(C_flag, keystream)

print("Flag:", flag.decode())
