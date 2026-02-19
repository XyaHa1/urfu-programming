def is_almost_lucky(ticket_number: str) -> bool:
    if not isinstance(ticket_number, str):
        raise ValueError()
    
    if len(ticket_number) != 6:
        raise ValueError()
    
    n = len(ticket_number)
    i = int(ticket_number)

    if i == 0 or i == 999999:
        return False
    
    prev = str(i - 1).zfill(n)
    nxt = str(i + 1).zfill(n)

    prev_l = sum(map(int, prev[:n//2]))
    prev_r = sum(map(int, prev[n//2:]))

    nxt_l = sum(map(int, nxt[:n//2]))
    nxt_r = sum(map(int, nxt[n//2:]))

    return prev_l == prev_r or nxt_l == nxt_r
    