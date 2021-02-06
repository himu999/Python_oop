import fib_package
print("Hello, Now i am inside fibo_package.py")
print(fib_package.list_fib(15))
n = fib_package.find_fib(15)
print("15th fibonacci number is : ", n)

for i in range(1, 11):
    print(fib_package.find_fib(i), end=" ")


