import re

file = open("actual_data.txt")
text = file.read()

lst = re.findall('[0-9]+', text)
lst = list(map(int, lst))

total = sum(lst)
print(total)
