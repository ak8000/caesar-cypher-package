def caesar_encrypt(text, shift):
    """
    Encrypts a given text using the Caesar cipher, extended to include numbers.

    :param text: The input string to encrypt.
    :param shift: The number of positions to shift each character.
    :return: The encrypted string.
    """
    encrypted_text = ""
    
    for char in text:
        if char.isupper():
            encrypted_char = chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            encrypted_char = chr((ord(char) + shift - 97) % 26 + 97)
        elif char.isdigit():
            encrypted_char = chr((ord(char) + shift - 48) % 10 + 48)
        else:
            encrypted_char = char
        encrypted_text += encrypted_char

    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


def verify_crypt(pre_encrpted_text, post_decrypted_text):
    if(pre_encrpted_text == post_decrypted_text):
        return True
    else:
        return False
