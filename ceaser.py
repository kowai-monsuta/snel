def encrypt(string, shift):

    cipher = ''
    for char in string:
        n = ord(char) - shift
        if n < 32:
            n += 95
        cipher += chr(n)
    return cipher

num = "1c67"
shift = 34

with open("text_files/file_" + num + ".txt") as f:
    text = f.read()

print("after encryption: ", encrypt(text, shift))
input("press enter to exit ;)")
