def find_fib(x):
    if x <= 2:
        if x == 0:
            return 0
        else:
            return 1

    fib_x, fib_next = 1, 1

    i = 3

    while i <= x:
        fib_x, fib_next = fib_next, fib_x + fib_next
        i = i + 1
    return fib_next


def list_fib(n):
    list_fibo = [0, 1, 1]
    if n <= 2:
        return list_fibo[:n]

    fib_x, fib_next = 1, 1

    i = 3

    while i <= n:
        fib_x, fib_next = fib_next, fib_x + fib_next
        list_fibo.append(fib_next)
        i = i + 1
    return list_fibo[:n]


if __name__ == "__main__":
    print("First 10 fibonacci number is : ", list_fib(10))
    print("15th fibonacci number is : ", find_fib(15))