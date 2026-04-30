from typing import Union

import math

Number = Union[int, float]

def _validate_input(a1: Number, a2: Number, b1: Number, b2: Number) -> None:
    if any((a1 is None, a2 is None, b1 is None, b2 is None)):
        raise ValueError()
    if not all((isinstance(a1, Number), isinstance(a2, Number), isinstance(b1, Number), isinstance(b2, Number))):
        raise TypeError()
    
    for v in (a1, a2, b1, b2):
        if math.isinf(v) or math.isnan(v):
            raise ValueError()


def check_intersection(a1: Number, a2: Number, b1: Number, b2: Number) -> bool:
    _validate_input(a1, a2, b1, b2)

    sub1 = (min(a1, a2), max(a1, a2))
    sub2 = (min(b1, b2), max(b1, b2))

    left_sub = min(sub1, sub2, key=lambda x: x[0])
    right_sub = max(sub1, sub2, key=lambda x: x[0])

    if left_sub[1] < right_sub[0]:
        return False
    
    return True
    

if __name__ == "__main__":
    assert check_intersection(1, 2, 3, 4) == False
    assert check_intersection(1, 2, 2, 3) == True
    assert check_intersection(1, 2, 1, 2) == True
    assert check_intersection(1.5, 5, 6, 10) == False
    assert check_intersection(1, 5, 3, 7) == True
    assert check_intersection(1, 5, 5, 10) == True
    assert check_intersection(5, 1, 3, 7) == True
    assert check_intersection(10, 13, 5, 9) == False
    try:
        check_intersection(10, 13, None, 9)
    except ValueError:
        print('None')

    try:
        check_intersection(float('nan'), 13, 10, 9)
    except ValueError:
        print('nan')
    
    try:
        check_intersection('float(nan)', 13, 10, 9)
    except TypeError:
        print('str')

