a = []
b = True
while b != "False":
    b = input()
    if b == "False":
        break
    a.append(b)



print(a[2])

# with open("b.txt", "w") as f:
#     for i in range(len(a)):
#         f.write(a[i]+"\n")
#
# f.close()
#
# b = []
# with open("b.txt", "r") as f:
#     t = f.read()
#
#     for A in t:
#         print(A)
#






# a = ["Himu", "Rimu"]
#
# for i in range(len(a)):
#     if "H" in a[i]:
#         print(a[i])
#         print(a.index(a[i]))