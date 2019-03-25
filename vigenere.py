def encrypt(message, keyword):

    result = ""
    index = 0
    for c in message:
        old_ascii = ord(c)
        shift = ord(keyword[index])
        new_ascii = 158 - old_ascii
        if new_ascii < 32:
            new_ascii += 95

        result += chr(new_ascii)
        index += 1

        if new_ascii > 5:
            index = 0


        
    return result

num = "30d3"

with open("text_files/file_" + num + ".txt") as f:
    text = f.read()

print("after encryption: ", encrypt(text, "enigma"))
input("press enter to exit ;)")
