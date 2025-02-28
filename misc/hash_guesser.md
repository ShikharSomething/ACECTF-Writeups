from pwn import *

HOST, PORT = "34.131.133.224", 5000


def interact_with_server(md5_hash):
    conn = remote(HOST, PORT)
    conn.recvuntil(b"Enter MD5 hash:")
    conn.sendline(md5_hash.encode())

    response = conn.recvall().decode()
    conn.close()

    try:
        matched = int(response.split("Characters matched: ")[1].split("/")[0])
        correct_pos = int(
            response.split("Characters in correct positions: ")[1].split("/")[0]
        )
        log.info(f"Matched: {matched}, Correct Position: {correct_pos}")
        log.info(f"Response: {response}")
        log.info(f"MD5 Hash: {md5_hash}")
    except:
        matched, correct_pos = 0, 0

    return matched, correct_pos


def brute_force_md5():
    initial_hash = "0" * 32
    best_hash = list(initial_hash)
    best_match, best_pos = 0, 0

    for i in range(32):
        for char in "0123456789abcdef":
            test_hash = best_hash[:]
            test_hash[i] = char
            test_hash_str = "".join(test_hash)

            matched, correct_pos = interact_with_server(test_hash_str)

            if matched > best_match or correct_pos > best_pos:
                best_match, best_pos = matched, correct_pos
                best_hash[i] = char

            if correct_pos == 32:
                return "".join(best_hash)

    return "".join(best_hash)


if __name__ == "__main__":
    found_md5 = brute_force_md5()
    log.success(f"Found MD5 Hash: {found_md5}")