# sink("log.txt")
# sink("log.txt", split=TRUE)
# sink()

sink("log.txt", split=TRUE)

for (i in 1:5)
    print(i)

sink()

sink("log.txt", append=TRUE)
print("RUNOOB")