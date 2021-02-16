lines = ["this is yours", "Red pen", "Can you give me?"]

with open("a.text", "w") as fp:

    for line in lines:

        fp.write(line+"\n")
fp.close()

with open("a.text", "r") as f:
    print(f.read())
