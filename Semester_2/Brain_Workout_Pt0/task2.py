LENGHT_ENG_ALP = 26


def get_lower_alphabet() -> dict:
    return {u % ord('a') : chr(u) for u in range(ord('a'), ord('z') + 1)}

def get_upper_alphabet() -> dict:
    return {u % ord('A'): chr(u) for u in range(ord('A'), ord('Z') + 1)}

def select_ord_from_keyword(ch: str) -> int:
    if ch.islower():
        return ord(ch) % ord('a')
    if ch.isupper():
        return ord(ch) % ord('A')
    return 0


def caesar_encrypt(plaintext: str, keyword: str) -> str:
    lower_alphabet = get_lower_alphabet()
    upper_alphabet = get_upper_alphabet()

    new_text = []
    ik = 0
    for ch in plaintext:
        if ik == len(keyword):
            ik = 0
        if ch.isalpha():
            if ch.islower():
                new_ch = lower_alphabet[(ord(ch) % ord('a') + select_ord_from_keyword(keyword[ik])) % LENGHT_ENG_ALP]
            elif ch.isupper():
                new_ch = upper_alphabet[(ord(ch) % ord('A') + select_ord_from_keyword(keyword[ik])) % LENGHT_ENG_ALP]
            ik += 1
        else:
            new_ch = ch
        new_text.append(new_ch)
    
    return ''.join(new_text)


def caesar_decrypt(ciphertext: str, keyword: str) -> str:
    lower_alphabet = get_lower_alphabet()
    upper_alphabet = get_upper_alphabet()

    new_text = []
    ik = 0
    for ch in ciphertext:
        if ik == len(keyword):
            ik = 0
        if ch.isalpha():
            if ch.islower():
                new_ch = lower_alphabet[(LENGHT_ENG_ALP + ord(ch) % ord('a') - select_ord_from_keyword(keyword[ik])) % LENGHT_ENG_ALP]
            elif ch.isupper():
                new_ch = upper_alphabet[(LENGHT_ENG_ALP + ord(ch) % ord('A') - select_ord_from_keyword(keyword[ik])) % LENGHT_ENG_ALP]
            ik += 1
        else:
            new_ch = ch
        new_text.append(new_ch)
    
    return ''.join(new_text)



s, k = "Hello World", "Nfd"
print(caesar_encrypt(s, k))
print(caesar_decrypt(caesar_encrypt(s, k), k))

assert s == caesar_decrypt(caesar_encrypt(s, k), k)