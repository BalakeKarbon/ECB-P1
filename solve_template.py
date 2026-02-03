def solve(ciphertext):
    """
    Given ECB ciphertext, recover the password
    """
    # TODO:
    blocks = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]
    duplicate = blocks[1]
    print(duplicate)
    
    


with open("challenge.bin", "rb") as f:
    ciphertext = f.read()
    cipher = b'VQ\x08H\xd2<\xb6\x97\xc3\xb9pS\xab\x93\x93\x00\xbbGa]g7L\x15A\x9c\xe4\xc07\x90{0\xbbGa]g7L\x15A\x9c\xe4\xc07\x90{0'
    # convert to hex
    print(cipher.hex())

    solve(ciphertext)
    # 11 22 33 44 55 66 77 88 99 00 aa bb cc dd ee ff
    # 12 34 56 78 90 ab cd ef fe dc ba 09 87 65 43 21