def fib(n):
    # fib(n) = fib(n-1) + fib(n-2)

    if n == 0 or n == 1:
        return n
    
    fn_1 = 1
    fn_2 = 0
    fn = 0

    for i in range(1, n):
        fn = fn_1 + fn_2
        fn_2 = fn_1
        fn_1 = fn

    return fn


if __name__ == '__main__':
    for i in range(20):
        print(f'n={i}:{fib(i)} ')

    # print(fib(14521))

    i = 0
    while fib(i) < 9785989:
        i += 1

    print(f'i={i}: fib({i})={fib(i)}')
    print(f'i={i-1}: fib({i-1})={fib(i-1)}')