# repeat
sum = 0
start = 0

repeat {
    start = start + 1
    sum = sum + start
    if (start == 10)
        break;
}

print(sum)

# while
sum = 0
start = 0
while (start != 10) {
    start = start + 1
    sum = sum + start
}

print(sum)


# for

sum = 0
nums = c(1:10)

for (num in nums) {
    sum = sum + num
}

print(sum)