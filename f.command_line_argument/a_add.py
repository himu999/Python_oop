import sys

arg = sys.argv
print(type(arg))

arg.append(input())
arg.append(input())



print(arg)

a = arg[1]
b = arg[2]

print(a+b)
