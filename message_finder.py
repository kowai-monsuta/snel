def chi_square(nums):
    exp = sum(nums) / len(nums)
    x_sq = 0

    for obs in nums:
         x_sq += (obs - exp) ** 2 / exp

    return x_sq

def get_char_counts(text):
    counts = [0] * 127

    for c in text:
        ascii_value = ord(c)
        counts[ascii_value] += 1
    
    return counts[32:]

def get_file_name (num):
    '''returns a file name like file_00001.text'''
    hex_str = hex(num)
    hex_str = hex_str[2:]

    if len(hex_str) == 1:
        zeros = "000"
    elif len(hex_str) == 2:
        zeros = "00"
    elif len(hex_str) == 3:
        zeros = "0"
    else:
        zeros = ""

    return "file_" + zeros + hex_str + ".txt"

def get_file_content (file_name):
    with open (file_name, 'r') as f:
        content = f.read()
    return content


# just testing...
values = [4, 2, 7, 3, 8, 5, 2]
print(chi_square(values))

counts = get_char_counts('!qMax+/a')
print(counts)

name = get_file_name(15)
print(name)

name = get_file_name(243)
print(name)

# let's do this...
num_files = 18000
threshold = 145


for n in range(num_files):
    file_name = get_file_name(n)
    text = get_file_content ("text_files/" + file_name)
    counts = get_char_counts(text)
    x_sq = chi_square(counts)

    if x_sq > threshold:
        print(n, file_name, x_sq)
