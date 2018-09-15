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
# a slicing operation allows one to subset string or list
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
- Interactive programming is a lot of fun but documenting your codes can save a lot of time!
- Create a file yourname_plots.py with a text editor (Vi, TextEdit, Nano, Notepad)
- Recreate swarm, boxen, and box plots. Save them.
- add plt.close() after each plt.save()
```
# run you code
python yourname_plots.py
```
---
##### Collaboration and sharing

---
So far the code and its output are at different places. Jupyter notebook integrates them so you don't have to!

```
start a jupyter notebook
bring your code (recreate yourname_plots.py) to the notebook
run the code with shift + enter (or by clicking the *run* button)

add on top of your notebook if plot doesnt show
%matplotlib inline

download the notebook
send it to the person sitting next to you
```

---
##### Exercise 3 (10 minutes)
This time no code examples. Use your previous experience to solve this exercise.
- Your mission: Using the titanic dataset, figure out if money increase the chance of survival
- Dataset: [titanic.csv](https://github.com/fibonaccirabbits/visual_python/tree/master/src)

```
##Hint:

#load a local dataset
titanic = pd.read_csv('titanic.csv')

#list all kinds of plots in seaborn
print([item for item in dir(sns) if 'plot' in item])
```

---
##### Summary
We explored: 
* Turning data into a visual object (plot)
* Making that visual object engaging and infromative via shapes and colors
* Documenting codes and outputs for seamless collaboration and sharing

---?image=src/bg-05.png&size=contain
Share your thoughts: [**feedback**](https://docs.google.com/forms/d/e/1FAIpQLSf3Q05NBO8jELU_6uLeobsRcvbNUBpwPRU3OPivHoukbDZmlQ/viewform)

---?image=src/thanks-06.png&size=contain



