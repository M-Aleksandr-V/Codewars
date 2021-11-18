from collections import Counter

def find_it(seq):
    __dict__ = dict(Counter(seq))
    for k, v in __dict__.items():
        if v % 2 == 1:
            return  k

seq = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
print(find_it(seq))