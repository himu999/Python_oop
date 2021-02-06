import fibo as f

print("Hello, i am inside program.py")
print(f.list_fib(15))

print("15th fibonacci number is : ", f.find_fib(15))

print("First 15th fibonacci number is : ")

for i in range(16):
    print(f.find_fib(i))
