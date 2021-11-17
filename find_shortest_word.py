def find_short(s):
    l = s.split()
    return min(l, key = len)

s = "bitcoin take over the world maybe who knows perhaps" 

print(find_short(s))