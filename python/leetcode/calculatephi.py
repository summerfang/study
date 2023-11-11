def calculate_phi(n):
    def generate_primes(n):
    # Uses list comprehension
        pass

    def is_prime(n,primes):
        # Checks ifin' is prime
        pass

    def calculate(n,primes):# Performs a calculation
        if is_prime(n,primes):
            return n-1
        else:
            phi = n
            for p in primes:
                if n%p==0:
                    phi -= phi/p
            return int(phi)
        
    primes = generate_primes(n)
    return calculate(n, primes)



print(calculate_phi(10))