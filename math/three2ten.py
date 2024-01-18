all = []
ten_and_above = 0
for i in range(1,7):
    for j in range(1,7):
        for k in range(1,7):
            all.append([i,j,k])
            if i + j + k >= 10:
                ten_and_above += 1

print(f'The total possible is {len(all)}, ten and above is {ten_and_above}, the probability is {ten_and_above/len(all)}')