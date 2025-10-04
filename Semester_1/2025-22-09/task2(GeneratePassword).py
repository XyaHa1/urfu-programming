import random
import string


def generate_password():
    password = []
    password += [random.choice(string.ascii_uppercase) for _ in range(3)]
    password += [random.choice(string.digits) for _ in range(3)]
    password += [random.choice("?#$%&*") for _ in range(2)]

    res = []
    for _ in range(len(password)):
        s = random.choice(password)
        password.remove(s)
        res.append(s)

    return ''.join(res)


if __name__ == '__main__':
    print(generate_password())
