import re
s = "Bangladesh is our homeland"
match = re.search("o\w\w", s)
print(match.group())

