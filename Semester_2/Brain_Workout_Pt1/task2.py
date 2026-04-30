from typing import Tuple
import random
import string
import re
import math
from collections import Counter


PASSWORD_CRITERIA = {

    'TOO_SHORT': {
        'score': -30,
        'message': 'Password is too short (minimum 8 characters required)',
        'example': 'pass'
    },
    'RECOMMENDED_LONGER': {
        'score': -5,
        'message': 'Password could be stronger with at least 12 characters',
        'example': 'Password10!'
    },


    'NO_UPPERCASE': {
        'score': -10,
        'message': 'Missing uppercase letters',
        'example': 'password123!'
    },
    'NO_LOWERCASE': {
        'score': -10,
        'message': 'Missing lowercase letters',
        'example': 'PASSWORD123!'
    },
    'NO_NUMBERS': {
        'score': -10,
        'message': 'Missing numbers',
        'example': 'Password!'
    },
    'NO_SPECIAL': {
        'score': -10,
        'message': 'Missing special characters',
        'example': 'Password123'
    },


    'KEYBOARD_PATTERN': {
        'score': -20,
        'message': 'Contains keyboard pattern (e.g., qwerty, asdf)',
        'example': 'qwerty123'
    },
    'NUMERICAL_SEQUENCE': {
        'score': -15,
        'message': 'Contains simple number sequence (e.g., 123, 987)',
        'example': 'Password123'
    },
    'ALPHABETICAL_SEQUENCE': {
        'score': -15,
        'message': 'Contains alphabetical sequence (e.g., abc, xyz)',
        'example': 'Passwordabc!'
    },
    'REPEATED_CHARS': {
        'score': -15,
        'message': 'Contains repeated characters (e.g., aaa, 111)',
        'example': 'Password111!'
    },


    'COMMON_PASSWORD': {
        'score': -50,
        'message': 'Matches commonly used password',
        'example': 'admin'
    },
    'COMMON_WORD': {
        'score': -20,
        'message': 'Contains common dictionary word',
        'example': 'monkey123'
    },
    'YEAR_PATTERN': {
        'score': -15,
        'message': 'Contains year-like pattern (4-digit year 1900-2099)',
        'example': 'Password1990!'
    },


    'LOW_ENTROPY': {
        'score': -15,
        'message': 'Low character diversity',
        'example': 'aaaaaa123'
    },


    'GOOD_LENGTH': {
        'score': 20,
        'message': 'Good password length',
        'example': 'ThisIsALongPassword123!'
    },
    'HIGH_ENTROPY': {
        'score': 20,
        'message': 'High character diversity',
        'example': 'P@s$w0rd#123'
    }
}

def calculate_entropy(password: str) -> float:
    if not isinstance(password, str):
        raise TypeError("Input must be a string")
    
    if not password:
        return 0.0
    
    char_counts = Counter(password)
    lenght_password = len(password)
    
    entropy = 0.0
    for count in char_counts.values():
        probability = count / lenght_password
        entropy -= probability * math.log2(probability)
    
    return entropy


def detect_patterns(password: str) -> list[str]:
    if not isinstance(password, str):
        raise TypeError("Input must be a string")
    
    result = []
    
    if len(password) < 8:
        result.append('TOO_SHORT')
    elif len(password) < 12:
        result.append('RECOMMENDED_LONGER')
    else:
        result.append('GOOD_LENGTH')
    
    if not re.search(r'[A-Z]', password):
        result.append('NO_UPPERCASE')
    if not re.search(r'[a-z]', password):
        result.append('NO_LOWERCASE')
    if not re.search(r'[0-9]', password):
        result.append('NO_NUMBERS')
    if not re.search(rf'[{re.escape(string.punctuation)}]', password):
        result.append('NO_SPECIAL')

    inv_pass = password.lower()
    if any(p in inv_pass for p in ['qwerty', 'asdf', 'zxcv', '123456', 'qazwsx']):
        result.append('KEYBOARD_PATTERN')
    if re.search(r'(012|123|234|345|456|567|678|789|890|987|876|765|654|543|432|321|210)', inv_pass):
        result.append('NUMERICAL_SEQUENCE')
    if re.search(r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)', inv_pass):
        result.append('ALPHABETICAL_SEQUENCE')
    if re.search(r'(.)\1{2,}', inv_pass):
        result.append('REPEATED_CHARS')

    if inv_pass in frozenset(['password', 'admin', '123456', 'qwerty', 'letmein', 'welcome', 'login']):
        result.append('COMMON_PASSWORD')
    if any(w in inv_pass for w in frozenset(['password', 'monkey', 'dragon', 'master', 'football', 'shadow', 'sunshine', 'princess', 'abc'])):
        result.append('COMMON_WORD')
    
    if re.search(r'(19|20)\d{2}', password):
        result.append('YEAR_PATTERN')

    entropy = calculate_entropy(password)
    if entropy < 2.5:
        result.append('LOW_ENTROPY')
    else:
        result.append('HIGH_ENTROPY')

    return result


def get_structural_fingerprint(password: str) -> dict:
    if not isinstance(password, str):
        raise TypeError("Input must be a string")

    if not password:
        return {
            'character_types': [],
            'length': 0,
            'uppercase_positions': [],
            'lowercase_positions': [],
            'digit_positions': [],
            'special_positions': [],
            'repetition_patterns': [],
            'pattern_string': '',
        }
    
    char_types = []
    uppercase_positions = []
    lowercase_positions = []
    number_positions = []
    special_positions = []
    
    for i, char in enumerate(password):
        if char.isupper():
            char_types.append('U')
            uppercase_positions.append(i)
        elif char.islower():
            char_types.append('L')
            lowercase_positions.append(i)
        elif char.isdigit():
            char_types.append('D')
            number_positions.append(i)
        elif char in string.punctuation:
            char_types.append('S')
            special_positions.append(i)
        else:
            char_types.append('O')
    
    char_counts = Counter(password.lower())
    repetition_patterns = [
        {'char_type': 'letter' if c.isalpha() else 'digit' if c.isdigit() else 'special', 
         'count': count}
        for c, count in char_counts.items() 
        if count >= 2
    ]
        
    return {
        'character_types': char_types,
        'length': len(password),
        'uppercase_positions': uppercase_positions,
        'lowercase_positions': lowercase_positions,
        'number_positions': number_positions,
        'special_positions': special_positions,
        'repetition_patterns': repetition_patterns,
    }


def assess_password(password: str) -> Tuple[int, list[str]]:
    if not isinstance(password, str):
        raise TypeError("Input must be a string")
    
    detected_patterns = detect_patterns(password)
    
    total_score = 0
    msgs = []
    for pattern in detected_patterns:
        total_score += PASSWORD_CRITERIA[pattern]['score']
        msgs.append(PASSWORD_CRITERIA[pattern]['message'])

    return total_score, msgs


AMBIGUOUS_CHARS = {
    '0': 'OoQ', 'O': '0oQ', 'o': '0OQ',
    '1': 'Il|!L', 'I': '1l|!L', 'l': '1I|!L',
    '|': '1Il!L', '!': '1Il|L', 'L': '1Il|!',
}
CHAR_SETS = {
    'U': [c for c in string.ascii_uppercase if c not in 'OIL'],
    'L': [c for c in string.ascii_lowercase if c not in 'ol'],
    'D': [c for c in string.digits if c not in '01'],
    'S': [c for c in string.punctuation if c not in '|!'],
    'O': [' '],
}
def get_safe_char(char_type: str, exclude: str = None) -> str:
    available = CHAR_SETS.get(char_type, [' '])
    if exclude:
        available = [c for c in available if c != exclude]
    return random.choice(available) if available else ' '

def is_ambiguous(old_char: str, new_char: str) -> bool:
    ambiguous = AMBIGUOUS_CHARS.get(old_char, '')
    return new_char in ambiguous


def generate_twin(password: str) -> str:
    if not isinstance(password, str):
        raise TypeError("Input must be a string")

    if not password:
        return ''
    
    fingerprint = get_structural_fingerprint(password)
    char_types = fingerprint['character_types']
    
    twin = []
    max_attempts = 10
    
    for i, old_char in enumerate(password):
        char_type = char_types[i]
        new_char = None
        
        for _ in range(max_attempts):
            candidate = get_safe_char(char_type, old_char)
            if not is_ambiguous(old_char, candidate):
                new_char = candidate
                break
        
        if new_char is None:
            new_char = ' '
        
        twin.append(new_char)
    
    return ''.join(twin)


if __name__ == "__main__":
    # test_cases = [
    #         ("a", -75,
    #          ['Password is too short (minimum 8 characters required)', 'Missing uppercase letters', 'Missing numbers',
    #           'Missing special characters', 'Low character diversity']),
    #         ("password", -85,
    #          ['Password could be stronger with at least 12 characters', 'Missing uppercase letters', 'Missing numbers', 'Missing special characters', 'High character diversity', 'Matches commonly used password', 'Contains common dictionary word']),
    #         ("Password123!", 5,
    #          ['Contains simple number sequence (e.g., 123, 987)', 'High character diversity', 'Contains common dictionary word', 'Good password length']),
    #         ("SuperSecure2023!", 25, ['Contains year-like pattern', 'High character diversity', 'Good password length']),
    #     ]
    # for pwd, expected_score, expected_msgs in test_cases:
    #     score, msgs = assess_password(pwd)
    #     assert score == expected_score, f"Expected score {expected_score} but got {score} for password '{pwd}'"
    #     assert set(msgs) == set(expected_msgs), f"Expected messages {expected_msgs} but got {msgs} for password '{pwd}'"
    password = 'password'
    score, messages = assess_password(password)
    print(f"Password: {password}\nScore: {score}\nMessages: {messages}\n")
