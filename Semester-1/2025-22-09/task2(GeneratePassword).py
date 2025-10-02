import random
import string


def generate_password():
    password = []
    password += [random.choice(string.ascii_uppercase) for _ in range(3)]
    password += [random.choice(string.digits) for _ in range(3)]
    password += [random.choice("?#$%&*") for _ in range(2)]

    return ''.join([random.choice(password) for _ in range(8)])


if __name__ == '__main__':
    print(generate_password())
