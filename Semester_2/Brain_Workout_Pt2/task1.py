def find_wire(n: int) -> int:
    if not isinstance(n, int) or isinstance(n, bool):
        raise ValueError()
    
    if n < 0:
        raise ValueError()
    
    s = 1
    lenght = 0
    curr_lenght = 0
    while n < lenght + curr_lenght:
        count_nums = 9 * (10 ** (s - 1))
        curr_lenght = count_nums * s

        if n < lenght + curr_lenght:
            break
        
        lenght += curr_lenght
        s += 1
    
    offset = n - lenght
    num = 10 ** (s - 1) + offset // s
    digit_pos = offset % s
    return int(str(num)[digit_pos])
        
"""
[1; 10) = 9 -> 9 * (10 ** 0) * 1 = 9
[10:100) = 90 -> 9 * (10 ** 1) * 2 = 180
[100:1000) = 900 -> 9 * (10 ** 2) * 3 = 2700
"""

if __name__ == '__main__':
    print(find_wire(0))