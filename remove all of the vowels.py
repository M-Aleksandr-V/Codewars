def disemvowel(string_):
    n = 0
    while n < len(string_):
        string_ = string_.replace('a', '')
        string_ = string_.replace('e', '')
        string_ = string_.replace('i', '')
        string_ = string_.replace('o', '')
        string_ = string_.replace('u', '')
        string_ = string_.replace('y', '')
        n += 1
        return string_