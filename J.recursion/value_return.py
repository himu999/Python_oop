def fun(n):
    if n == 1:
        return 1
    else:
        return 1 + fun(n-1)


if __name__ == "__main__":

    print(fun(3))
