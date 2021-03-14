import re

s = "Bangladesh"
match = re.search(".", s)
print(match.group())

match = re.search("B.n", s)
print(match.group())

s = "Bangladesh is our motherland"

match = re.search("............", s)
print(match.group())

