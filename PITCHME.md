---
# Structured data

Hands on session

---
####  Geek speak for today
- **Data structure:**  a format that enables efficient access and modification.
- **Object:** a combination of variables, functions, and data structures.
- **Package manager:** a tool that manages packages (programs).


---
#### Input: opening a file in python

```
# Open a jupyter notebook from Anaconda
# or on your terminal do
jupyter notebook

# define a file path
infile = 'fasta1/cor6_6.fasta'

# read the file
content = open(infile).read()

# visualize the file
print(content)


```

- Easy! You can now read files on python.

---
##### Exercise 1 (10 minutes)

```
# get to know your data
# there are 6 more files in the fasta6 directory
# open the files and look into their content

```

---
##### Python data structures

* String
* List

---
```
# a string is enclosed by quotes: '' or ""
mystring = 'Hello world'
print(mystring)

#a list is enclosed by squearebrackets: [ ]
mylist = ['Hello', 'world']
print(mylist)

```

---
* Slicing and indexing

```
# a slicing/indexing operation allows one to subset string or list
# python indexing starts from 0

mystring = 'Hello world'
print(mystring)
mystring1 = mystring[1]
print(mystring1)
print(mystring)
```
---
```
mylist = ['Hello', 'world']
print(mylist)
mylist1 = mylist[1]
print(mylist1)
```
---
```
# a slicing operation is enclosed by squere brackets: []
# the start and end index is separated by a colon
# the terminal index is exluded

mystring1_to_2 = mystring[1:3]
print(mystring1_to_2)
```
---
##### Exercise 2 (10 minutes)
- With your newly acquired slicing skill, get the name of the organisms on each fasta file in fasta6
- the names are: A.thaliana, Rapeseed, Armoracia rusticana, Brassica rapa, and Brassica napus


---
##### Output: Writing a file to local directory

```
# open an output file
outfile = open('myoutput.txt', 'w')

# get some content to write
mycontent = 'Hello world, I am Groot'

# write the content file 
outfile.write(mycontent)

# close the output file
outfile.close()
```


---
##### Exercise 3 (10 minutes)
- Read the files in fasta6
- With slicing get the name of the organisms
- Write an output file containg the name for each organism


---
##### Loop + slice = magic 


---
- A loop allows one to perform operations on a set of items (e.g., items on a list) 

```
# create a list
mystring = 'Hello world, I am Groot'
print(mystring)
mylist = mystring.split()
print(mylist)

# With loop, print only the first letter of each item in the list
for item in mylist:
	print(item[0])
```

---
```
#collecting values with loops
first_letters = [] # an empty list
for item in mylist:
	first_letter = item[0]
	firs_letters.append(first_letter)
print(first_letters)

```


---
##### Exercise 4 (10 minutes)
- With a loop
	- Read the files in fasta6
	- With slicing get the name of the organisms
	- Write an output file containg the name for all organisms



---
Share your thoughts: [**feedback**](https://docs.google.com/forms/d/e/1FAIpQLSf3Q05NBO8jELU_6uLeobsRcvbNUBpwPRU3OPivHoukbDZmlQ/viewform)

---?image=src/thanks-06.png&size=contain



