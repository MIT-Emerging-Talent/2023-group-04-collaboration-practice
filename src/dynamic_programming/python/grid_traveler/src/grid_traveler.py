def grid(a,b):
    if a == 1:
        return 1
    if b == 1:
        return 1
    return grid(a-1, b) + grid(a, b-1)
