fp = open("test.txt", "w")
fp.write("This file was created using python!")
fp.close()

f = open("test.txt", "a")
f.write(" this is a new line")
f.close()

f = open("test.txt", "r")
f.read()
f.close()
