def isPrime(num):
    if num <= 1:
        return False

    hasNoRemainder = False
    
    for i in range(1, num):
        if num % i == 0:
            hasNoRemainder = True
            break
    
    return hasNoRemainder
