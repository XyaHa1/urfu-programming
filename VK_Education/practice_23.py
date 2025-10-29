from typing import List


def get_indexes(nums1: List[int], nums2: List[int]) -> List[int]:
    arr = []
    for i, v in enumerate(zip(nums1, nums2)):
        if v[0] < v[1]:
            arr.append(i)
    return arr


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
