from typing import List, Dict

import random
import string


def create_random_square() -> List:
    letters = list(string.ascii_lowercase)
    digits = list(string.digits)

    random.shuffle(letters)
    random.shuffle(digits)
    
    square = [['A', 'D', 'F', 'G', 'V', 'X']]
    i = 0
    j = 0
    while i < len(letters):
        square.append([square[0][j]])
        while i < len(letters) and len(square[-1]) < 7:
            square[-1].append(letters[i])
            i += 1
        j += 1

    i = 0
    j -= 1
    while i < len(digits):
        while i < len(digits) and len(square[-1]) < 7:
            square[-1].append(digits[i])
            i += 1
        j += 1
        square.append([square[0][j if j < len(square[0]) else 0]])

    square.pop()
    return square

    
def create_adfgvx_square(square_2d: List) -> Dict:
    keys_code = {}
    headers = square_2d[0]
    for i in range(1, len(square_2d)):
        row = square_2d[i]
        row_label = row[0]
        for j in range(1, len(row)):
            char = row[j]
            col_label = headers[j - 1]
            
            keys_code[char] = f"{row_label}{col_label}"
            
    return keys_code

def create_decod_adfgvx_square(square: Dict) -> Dict:
    new_square = {}
    for key, val in square.items():
        new_square[val] = key

    return new_square
    

def adfgvx_encrypt(plaintext: str, key: str, square: dict) -> str:
    if not all((isinstance(plaintext, str), isinstance(key, str), isinstance(square, Dict))):
        raise TypeError()
    
    if not key.isalpha():
        raise ValueError()
    
    if not plaintext.strip():
        return ''
    
    square = {k.lower(): v for k, v in square.items()}
    
    new_str = []
    for ch in plaintext:
        ch = ch.lower()
        if ('a' <= ch <= 'z') or ch.isdigit():
            new_str.append(ch)
    
    encrypt_str = []
    for ch in new_str:
        encrypt_str.append(square[ch])
    

    encrypt_str = ''.join(encrypt_str)
    key_to_encrypt = {}
    for k in range(len(key)):
        for i in range(k, len(encrypt_str), len(key)):
            key_to_encrypt[key[k]] = key_to_encrypt.get(key[k], '') + encrypt_str[i]
    
    sort_key_to_encrypt = sorted(key_to_encrypt.items(), key=lambda x: x[0])
    res = [c for _, v in sort_key_to_encrypt for c in v]

    return ''.join(res)



def adfgvx_decrypt(ciphertext: str, key: str, square: dict) -> str:
    if not all((isinstance(ciphertext, str), isinstance(key, str), isinstance(square, Dict))):
        raise TypeError()
    
    if not key.isalpha():
        raise ValueError()
    
    if not ciphertext.strip():
        return ''
    
    square = {v.upper(): k.upper() for k, v in square.items()}

    col_high = len(ciphertext) // len(key)
    rem = len(ciphertext) % len(key)
    cnt_items_for_key = {}
    for i in range(len(key)):
        if i < rem:
            cnt_items_for_key[i] = col_high + 1
        else:
            cnt_items_for_key[i] = col_high

    sort_cnt_key = sorted(cnt_items_for_key.keys(), key=lambda x: (key[x], x))

    col_data = {}
    i = 0
    for k in sort_cnt_key:
        count = cnt_items_for_key[k]
        col_data[k] = ciphertext[i : i + count]
        i += count

    max_high_col = col_high + (1 if rem > 0 else 0)       
    restored_stream = []
    for j in range(max_high_col):
        for i in range(len(key)):
            if j >= len(col_data[i]):
                continue
            restored_stream.append(col_data[i][j])
    
    res = [square[restored_stream[i] + restored_stream[i + 1]] for i in range(0, len(restored_stream) - 1, 2)]

    return ''.join(res)
    

square = create_adfgvx_square(create_random_square())
test_cases = [
            "Hello, World! 123",
            "ADFGVX cipher",
            "Python programming",
            "Cryptography is fun",
            "1234567890",
            "attackatdawn",
        ]
k = 'SECRNT'
for t in test_cases:
    print()
    print(t)
    e = adfgvx_encrypt(t, k, square)
    print(e)
    d = adfgvx_decrypt(e, k, square)
    print(d)
    print()

# plaintext = "attackatdawn"
# key1 = "DIFFERENT"
# key2 = "KEYWORD"
# print(plaintext)
# encrypted1 = adfgvx_encrypt(plaintext, key1, square)
# encrypted2 = adfgvx_encrypt(plaintext, key2, square)
# print(encrypted1)
# print(encrypted2)
# dec1 = adfgvx_decrypt(encrypted1, key1, square)
# dec2 = adfgvx_decrypt(encrypted2, key2, square)
# print(dec1)
# print(dec2)
