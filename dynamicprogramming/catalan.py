def catalan(n):
    # Cn = (2n)!/(n+1)!n!

    if n == 0: return 1
    
    two_n = 2*n
    n_1 = n + 1
    n_this = n

    Cn = 1

    factorial_two_n = 1
    for j in range(two_n, 1, -1):
        factorial_two_n *= j

    factorial_n_1 = 1
    for j in range(n_1, 1, -1):
        factorial_n_1 *= j

    factorial_n = 1
    for j in range(n_this, 1, -1):
        factorial_n *= j

    
    Cn  = factorial_two_n / (factorial_n_1 * factorial_n)

    return Cn

def catalan_v2(n) -> int: 
    #C0=C1=1, Cn=\sum_{i=0}^{n-1}C_iC_{n-i-1}\, for \, n>=2

    if n == 0 or n == 1: return 1

    C_0 = 1
    C_1 = 1

    catalan_items = [0 for x in range(n+1)]
    catalan_items[0] = C_0
    catalan_items[1] = C_1

    sum_catalan = 0

    for i in range(2, n + 1):
        for j in range(i):
            catalan_items[i] += catalan_items[j] * catalan_items[i-j-1]

    return catalan_items[n]