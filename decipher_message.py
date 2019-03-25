#Decoder

def get_cipher():
    cipher_list = list(input("cipher:"))
    return cipher_list

def get_message():
    message = input("message:")
    return message

def decipher(message):
    new_message = ""
    for character in message:
        n = ord(character)
        n += shift
        result += chr(n)

    print(new_message)

def shift(c,n):
    ascii_value = ord(c)
    ascii_value -= n
    'wrap around here'
    return chr(ascii_value)

    


cipher_list = get_cipher()
message = get_message()
decipher(message)
shift (message)
