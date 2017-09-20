
prompt = 'Enter file:'
fileName = input(prompt)
file = open(fileName)
#print(file)
#type(file)
words = []

for line in file:
	line = line.rstrip()
	words += line.split()

counts = dict()

for word in words:
	counts[word] = counts.get(word, 0) + 1 
#print(counts)



#if word in counts:
#		x = counts[word]