# 3n + 1 problem is also called Collatz Conjecture. Please refer to https://en.wikipedia.org/wiki/Collatz_conjecture
# Giving any positive integer, return a list contains all sequence number according to Collatz Conjecture.

def collatz(i):
    if not isinstance(i, int) or i <= 0:
        raise ValueError("Parameter i must to be a postive integer")

    collatz_list = list()
    while i != 1:
        collatz_list.append(i)
        if i % 2 == 0:
            i = int(i//2)
        else:
            i = int(i*3 + 1)

    collatz_list.append(1)
    return collatz_list


for i in range(1,100):
    print(collatz(i))