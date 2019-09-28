def isPrime(num):
    if num <= 1: #Negative, 0 and 1 is not a prime number
        return False

    b = True # Assume num is a prime number
    
    for i in range(2, num):
        if num % i == 0:
            b = False
            break
    
    return b
