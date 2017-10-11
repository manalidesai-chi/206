from bs4 import BeautifulSoup

#YOUR CODE 1

#stuff = file.read()
# open the "samplehtml.html" file and read it into a string
# No ouptput
file = open("samplehtml.html", "r").read()

print("\n")

#YOUR CODE 2
# create a BeautifulSoup object from the string
# No output
bs = BeautifulSoup(file, "lxml")

#***????
imgs = bs.findall("img")
xkcd_img = img[0]
#****???

print("\n")

#YOUR CODE 3
# Write/plan code to print the URL to the XKCD comic, using BSoup and this file.

print(xkcd_img("src"))
print("\n")

#YOUR CODE 4
# Write code to grab all the links (URLs) in that html page, but nothing else.
for link in bs.find_all('a'):
	print(link['href'])

print(b)

#YOUR CODE 5
# Write/plan code to grab the TEXT of all the links in that html page, but nothing else.
list_obj = bs.find_all('li')
for li in list_obj:
	print(li.text)

print("\n")
#YOUR CODE 6
# Write/plan code to grab the text of each of the items in the ordered list. (Not the 1/2/2, just the text. 


print("\n")
#YOUR CODE 7
# - Write/plan code to grab the alt text associated with the image of the XKCD comic.
# see way above for accessing xkcd_img...
# OUTPUT - 

print("\n")
#YOUR CODE 7
# Write  code to assign the BeautifulSoup object holding the div that contains the image to a variable `image_div_obj` 
#Ouput: print image_div_obj



print("\n")
#YOUR CODE 7
# - Write/plan code to add these three strings to a list, using just BSoup and the html doc available…
#   > An image from the comic XKCD below.
#   > Find more similar stuff at the comic web site.
#   > Or just check out your homework after you sign into Canvas.

# first, get the thing that contains them all, the span! store in variable names span_container
# print span_conainer

#second, get ll of the paragraphs in the span_container and store in a variable called paragraph_tags
# print paragraph_tags

#third: print all of the text in the paragraphs.  Consider using strip(), rstrip(), etc.
