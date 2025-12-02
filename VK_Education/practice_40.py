from collections import deque
from typing import List


def rotate_list(nums: List[int], n: int):
    if not nums:
        return nums
    n = n % len(nums)  # обработка случая, когда n больше длины списка
    dq = deque(nums)
    for _ in range(n):
        dq.appendleft(dq.pop())  # забираем с конца и добавляем в начало
    return list(dq)
