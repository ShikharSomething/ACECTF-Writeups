extract '. 87.jpg' file
steghide extract -sf '. 87.jpg'
u'll find whitespace.txt

def whitespace_decrypt_from_file(file_path):
    # Open the file and read its contents
    with open(file_path, 'r') as file:
        encoded_message = file.read()
    
    # Initialize an empty list to store the binary string
    binary_string = ""

    # Loop through each character in the encoded message
    for char in encoded_message:
        if char == ' ':
            binary_string += '0'  # Space is 0
        elif char == '\t':
            binary_string += '1'  # Tab is 1
        elif char == '\n':
            # When encountering newline, it indicates the end of one byte
            binary_string += ' '  # Just to separate chunks of bytes

    # Split the binary string into 8-bit chunks (bytes)
    binary_values = binary_string.split()

    # Convert each 8-bit binary chunk into its corresponding ASCII character
    decoded_message = ''.join(chr(int(bv, 2)) for bv in binary_values)

    return decoded_message

# Example usage:
file_path = 'whitespace_flag.txt'  # The path to your file
decoded_message = whitespace_decrypt_from_file(file_path)
print("Decoded message:", decoded_message)

ACECTF{n0_3xp1017_n0_g41n}