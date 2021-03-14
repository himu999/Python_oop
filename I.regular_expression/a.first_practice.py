import re

match = re.search('Bangla', 'Bangladesh')

print(match)
print(match.group())

match1 = re.search("desh", "Bangladesh")
print(match1)
print(match1.group())

match = re.search("dets", "Bangladesh")
# print(match.group())

print(match)

print(type(match))

print(match is None)
