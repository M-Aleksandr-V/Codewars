def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:  # count repetitions are multiples of three
            return i


a = [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]
print(find_it(a))
