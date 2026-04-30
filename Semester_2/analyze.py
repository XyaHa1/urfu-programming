# 1
# O(1)
def some_func(input: int) -> bool:
   return True if input % 2 == 0 else False


some_func(1512312541256)



# 2
# O(1)
def some_func2(arr: list[int]) -> int:
   return arr[len(arr) - 5]


# 3
# O(n)
def some_func3(arr: list[int]) -> None:
   for i in range(len(arr)):
       print(1)


some_func3([1,5,67,73,45,1,2])


# 4
# O(x)
x: int = 5
res: int = 0
for i in range(x):
   res += 1



# 5
# O(n)
x: int = 5643232
res: int = 0
for i in range(1035456):
   res += x



# 6
# O(x^2)
x: int = 5
res: int = 0
for i in range(x):
   for j in range(x):
       res += 1



# 7
# O(n)
def interesting_func(power: int) -> None:
   num = 2
   nextPower = 1

   while nextPower <= power:
       print(num)
       num *= 2
       nextPower+=1



# 8
# O(logn)
def interesting_func2(val: int) -> None:
   num = 2
 
   while num <= val:
       num *= 3




# 9
# O(n^2 * logn)
def some_func4(arr: list[int]) -> None:
   for i in range(len(arr)):
       print(arr)


some_func4([1,5,67,73,45,1,2])

# 9
# O(n^2)
def find_pairs(numbers: list[int]) -> int:
    n: int = len(numbers)
    count: int = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == 0:
                count += 1
    
    return count

# 10
# O(n)
def find_pairs_optimized(numbers: list[int]) -> None:
    number_set = set()
    count = 0
    
    for num in numbers:
        if -num in number_set:
            count += 1
            
        number_set.add(num)
    
    return count
