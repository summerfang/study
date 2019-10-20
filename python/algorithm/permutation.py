letters = ['D','E','E','T','L'] # Doing, Experiencing, Enjoying, Thinking, Learning

all_words = {}

def permutation_with_loop_without_duplication(letters):
    for i in range(len(letters)):
        for j in range(len(letters)):
            for k in range(len(letters)):
                for m in range(len(letters)):
                    for n in range(len(letters)):
                        if i != j and i != k and i != m and i != n and j != k and j != m and j != n and k != m and k != n and m != n and n != i:
                            all_words[letters[i] + letters[j] + letters[k] + letters[m] + letters[n]] = ''

permutation_with_loop_without_duplication(letters)
print(list(all_words.keys()))


all_words = []

def permutation_with_loop_and_duplication(letters):
    length = len(letters)
    for i in range(length):
        for j in range(length):
            if j != i:
                for k in range(length):
                    if k != i and k != j:
                        for m in range(length):
                            if m != i and m != j and m != k:
                                for n in range(length):
                                    if n != i and n != j and n !=k and n != m:
                                        all_words.append(letters[i] + letters[j] + letters[k] + letters[m] + letters[n])

permutation_with_loop_and_duplication(letters)    
print(all_words)

