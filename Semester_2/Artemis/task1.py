def is_almost_lucky(s: str) -> bool:
    if len(s) != 6:
        return False
    
    n = len(s)
    i = int(s)

    if i == 0 or i == 999999:
        return False
    
    prev = str(i - 1).zfill(n)
    nxt = str(i + 1).zfill(n)

    prev_l = sum(map(int, prev[:n//2]))
    prev_r = sum(map(int, prev[n//2:]))

    nxt_l = sum(map(int, nxt[:n//2]))
    nxt_r = sum(map(int, nxt[n//2:]))

    return prev_l == prev_r or nxt_l == nxt_r
    