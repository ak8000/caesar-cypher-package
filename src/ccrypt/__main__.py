import caesar_crypt as caesar

if __name__ == "__main__":
    original_text = "My name is Adam Schwartz and I was born in 2001!"
    shift_amount = 26

    encrypted = caesar.caesar_encrypt(original_text, shift_amount)
    print(f"Encrypted: {encrypted}")

    decrypted = caesar.caesar_decrypt(encrypted, shift_amount)
    print(f"Decrypted: {decrypted}")

    print(caesar.verify_crypt(original_text, decrypted))