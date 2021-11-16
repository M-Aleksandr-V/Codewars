def xo(s):
    s = s.lower()
    a = s.count('o')
    b = s.count('x')
    if a == b:
        return True
    elif a and b == 0:
        return True
    else:
        return False
