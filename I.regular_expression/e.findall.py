import re

s = "multiple phone number, 01711111111, 01811111111, 01910101010, 00000000000"

result = re.findall(r"\d{3}\s*\d{8}", s)
print(result)

s = "multiple phone number, 01711111111, 01811111111, 01910101010, 00000000000 123-123"
result = re.findall(r"01[356789]\s*\d{8}", s)
print(result)
