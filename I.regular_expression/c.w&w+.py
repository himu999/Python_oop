import re

s = "Bangladesh is our homeland"
match = re.search("o\w\w", s)
print(match.group())

match = re.search("i\w\w", s)
print(match)

match = re.search("B\w+h", s)
print(match.group())

match = re.search("B.+h", s)
print(match.group())

match = re.search("B.+?h", s)
print(match.group())






