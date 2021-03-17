def odd(n):
    if n <= 10:

        if n % 2 != 0:
            print(n+1)

        n += 1

        even(n)


def even(n):

    if n <= 10:
        if n % 2 == 0:
            print(n-1)

        n += 1

        odd(n)


a = 1
odd(a)
