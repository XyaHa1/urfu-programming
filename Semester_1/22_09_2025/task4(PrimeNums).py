from typing import List


def prime_nums(n: int) -> List[int]:
    prime_list = [x for x in range(2, n + 1)]
    flag_list = [True] * len(prime_list)

    i = 0
    for i in range(2, int(n ** 0.5) + 1):
        if flag_list[i]:
            for j in range(i + 1, len(prime_list)):
                if prime_list[j] % prime_list[i] == 0:
                    flag_list[j] = False
        i += 1

    res = []
    for i in range(len(flag_list)):
        if flag_list[i]:
            res.append(prime_list[i])

    return res


if __name__ == "__main__":
    print(prime_nums(10000))