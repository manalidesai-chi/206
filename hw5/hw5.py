#Manali Desai
#mrow
#https://github.com/schrodingerscat1901/HW5.git
import re

file = open("actual_data.txt")
text = file.read()

lst = re.findall('[0-9]+', text)
lst = list(map(int, lst))

total = sum(lst)
print(total)
