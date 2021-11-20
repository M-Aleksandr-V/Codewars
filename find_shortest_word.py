def find_short(s):

    b = s.split()
    return min(b, key=len)


s = "bitcoin take over the world maybe who knows perhaps"

print(find_short(s))
