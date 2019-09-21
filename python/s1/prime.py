def isPrime(num):
    hasNoRemainder = False
    
    for i in range(1,num):
        if num % i == 0:
            hasNoRemainder = True
            break
    
    return hasNoRemainder
