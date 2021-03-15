import re

s = "Phone number : 0171110100"
match = re.search("\d+", s)
print(match.group())

s = "house number : 5, phone number : 01711101001"
match = re.search("\d+", s)
print(match.group())

match = re.search('\d{11}', s)
print(match.group())

s = "house number : 5, phone number : 017 11101001"
match = re.search("\d{3}\s*\d{8}", s)
print(match.group())

s = "house number : 5, phone number : 017  11101001"
match = re.search("\d{3}\s+\s+\d{8}", s)
print(match.group())


s = "house number : 5, phone number : 017  11101001"
match =re.search("\d{3}\s+\d{8}", s)
print(match.group())

s = "house number : 5, phone number : 017 11101001"
result = re.search("\d{3}\s?\d{8}", s)
print(result.group())


