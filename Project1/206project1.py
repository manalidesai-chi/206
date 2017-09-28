import os
import filecmp

import csv
import statistics
import re
import datetime

def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.

	#Your code here:

	facebook = []
	with open(file) as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			if row[0] == "First":
				continue
			tempdic = {"First" : row[0], "Last" : row[1], "Email" : row[2], "Class" : row[3], "DOB" : row[4] }
			facebook.append(tempdic)

	return facebook			


#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	newlist = sorted(data, key=lambda k: k[col])

	name = newlist[0].get("First") + " " + newlist[0].get("Last")
	return name



#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

#count num of senior, juniors etc
#put in a list of tuples

# iterate thru dictionaries
# look at the clas 
# make counter fr each clas


	#Your code here:
	#data = sorted(data, key=lambda k: k[])
	senior = 0
	junior = 0
	fresh = 0
	soph = 0

	for d in data:
		clss = d.get("Class")
		
		if clss == "Senior": 
			senior += 1
		elif clss == "Junior": 
			junior += 1
		elif clss == "Sophomore": 
			soph += 1
		elif clss == "Freshman": 
			fresh += 1

	tuplist = [ ("Senior", senior), ("Junior", junior), ("Sophomore", soph), ("Freshman", fresh) ]
	tuplist = sorted(tuplist, key = lambda x: x[1], reverse = True)
	return tuplist

# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB
	lst = []
	for d in a:
		date = d.get("DOB")
		word = re.findall( '/.*/' , date )
		lst.append(word[0][1: len(word[0])-1 ])

	return int( statistics.mode(lst) )




# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB
	ages = []
	today = datetime.datetime.now()

	for d in a:
		strdate = d.get("DOB") #get b day
		temp = strdate.split("/")
		bday = datetime.datetime(int(temp[2]), int(temp[0]), int(temp[1]))
		ages.append(((today-bday).days)/365)
	return round(statistics.mean(ages))



#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None
	
	lst = sorted(a, key = lambda k: k[col])

	with open(fileName, 'w') as csvfile:
		c = csv.writer(csvfile)

		for row in lst:
			c.writerow([row["First"]] + [row["Last"]] + [row["Email"]])






################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()

