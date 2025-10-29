def func(nums):
    nums = list(map(int, nums.split()))
    return round(sum(nums) / len(nums), 2)


while (s := input()) != "":
    print(func(s))
