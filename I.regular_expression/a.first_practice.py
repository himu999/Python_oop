s = "Afganistan, America, Bangladesh, Canada, Denmark, England, Greenland, Iceland, Netherlands, New Zealand, Sweden, " \
    "Swizerland"


countries = s.split(',')


print(countries, end="\n\n")

li = [item for item in countries if item.endswith("land") or item.endswith("lands")]

print(li)
