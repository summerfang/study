# 3n + 1 problem is also called Collatz Conjecture. Please refer to https://en.wikipedia.org/wiki/Collatz_conjecture
# Giving any positive integer, return the sequence according to Collatz Conjecture.

collatzconjecture_list = list()

def collatzconjecture(i):
    if i == 1:
        collatzconjecture_list.append(i)
        return
    else:
        collatzconjecture_list.append(i)

        if i % 2 == 0:
            collatzconjecture(int(i/2))
        else:
            collatzconjecture(int(i*3+1))



while True:
    input_string = input("Please input a positive integer:")
    try:
        input_value = int(input_string)
        if input_value > 0:
            collatzconjecture(input_value)
            break
        else:
            print("This is not a positive integer.\n")
            continue
    except ValueError:
        print("This is not a positive integer.\n")

print(collatzconjecture_list)