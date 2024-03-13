def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if(shift % 26 == 0):
                if(shift > 0):
                    shift_amount = (shift + 1) % 26
                else:
                    shift_amount = (shift - 1) % 26

            char_code = ord(char) + shift_amount

            if char.isupper():
                if char_code > ord('Z'):
                    char_code -= 26
                elif char_code < ord('A'):
                    char_code += 26
            elif char.islower():
                if char_code > ord('z'):
                    char_code -= 26
                elif char_code < ord('a'):
                    char_code += 26

            encrypted_text += chr(char_code)
        elif char.isdigit():
            shift_amount = shift % 10
            if(shift % 10 == 0):
                if(shift > 0):
                    shift_amount = (shift + 1) % 10
                else:
                    shift_amount = (shift - 1) % 10

            new_digit = (int(char) + shift_amount) % 10
            encrypted_text += str(new_digit)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def verify_crypt(pre_encrpted_text, post_decrypted_text):
    if(pre_encrpted_text == post_decrypted_text):
        return True
    else:
        return False
