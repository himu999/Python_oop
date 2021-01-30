def find_fibo(x):
    if x <= 2:
        return 1
    fib_x, fib_next = 1, 1

    i = 3
    while i <= x:
        i = i + 1

        fib_x, fib_next = fib_next, fib_x + fib_next
    return fib_next


for n in range(1, 10 + 1, 1):
    if n < 10:
        print(find_fibo(n), end=", ")
    else:
        print(find_fibo(n), end="")
