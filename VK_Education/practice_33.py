import os

text = input()


def write_and_read(text):
    filename = 'temp_file.txt'
    with open(filename, 'w') as f:
        f.write(text)
    with open(filename, 'r') as f:
        result = f.read()
    os.remove(filename)
    return result


print(write_and_read(text))
