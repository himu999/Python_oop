s = "Afganistan, America, Bangladesh, Canada, Denmark, England, Greenland, Iceland, Netherlands, New Zealand, Sweden, " \
    "Swizerland"


countries = s.split(',')

print(type(countries))

print(countries)

li = [item for item in countries if item.endswith("land")]

print(li)
