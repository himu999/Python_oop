def fact(n):

    if n == 1:
        return 1
    else:

        return fact(n-1) * n


if __name__ == "__main__":

    print(fact(int(input("Enter a number : "))))
