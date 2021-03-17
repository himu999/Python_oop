def fun(n):
    if n == 0:
        return 1
    else:
        return 7 + fun(n-2)


if __name__ == "__main__":

    print(fun(4))
