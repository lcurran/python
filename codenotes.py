# Declaring variables is like ruby

str() #converts to string
input() #asks for command line input
print() #to print
import math #imports math module

# while loop
x = 0
while x != 5:
   x = int(input("Guess a number:"))

   if x != 5:
      print("Incorrect choice")

print("Correct")

# for in loop
squares = [1, 4, 9, 16]
  sum = 0
  for num in squares:
    sum += num
  print sum  ## 30

 # for loops can have an else that executes upon exhaustion of the list (with for)
 # or if condition becomes false (with while), but NOT if the loop is terminated
 # by a break

 # When used with a loop, the else clause has more in common with the else clause of a try statement than it does that of if statements: a try statement’s else clause runs when no exception occurs, and a loop’s else clause runs when no break occurs. For more on the try statement and exceptions, see Handling Exceptions.

 # Conditionals
if condition:
    pass
elif
else

in # tests whether or not a sequence contains a certain value.

# lists
c = [5,2,10,48,32,16,49,10,11,32,64,55,34,45,41,23,26,27,72,18]
# elements accessed via index. negative index starts from the back
len(c) #returns length

# executes command line arguments like node if import sys module
# python actually ignores the word 'python' when you use sys.argv, so
# sys.argv[1] is the name of the script and sys.argv[2] is the arguments entered
# after
import sys
sys.argv

#Tuple: collection that cannot be modified
x = (1,)
y = (1,2,3,4)

#Dictionary in python is a ONE TO ONE MAPPING. every key points to a value
#dictionaries are not ordered
k = { 'EN':'English', 'FR':'French' }
print(k['EN'])

#to remove a value
del k['FR']

# strings can be accessed just like arrays, and sliced
slice = s[0:5]

#reading files
#!/usr/bin/env python
filename = "readme.txt"

with open(filename) as fn:
    content = fn.readlines()

print(content)

# writing files
!/usr/bin/env python

f = open("output.txt","w")
f.write("Pythonprogramminglanugage.com, \n")
f.write("Example program.")
f.close()

# modules
import modulename

# math
import math
# division in python always returns a float

# builtin modules
import time

.time() #ticks

.localtime(time.time())
#returns
Current time : time.struct_time(tm_year=2015, tm_mon=12, tm_mday=19, tm_hour=15, tm_min=42, tm_sec=0, tm_wday=5, tm_yday=353, tm_isdst=0)
# format it by printing elements of the array

import random
# generates real number between 0 and 1
x = random.random()
print(x)

# generates number between 1 and 50
x = random.randint(0,50)
print(x)

# choose 3 random items from a listslist = [1,2,3,4,5,6,7,8,9,10]
x = random.sample(list,3)
print(x)

# logging
import logging
logging.warning('Something went wrong.')

#levels of severity
logging.basicConfig(level=logging.WARNING)
logging.debug('Debug message')
logging.error('This is an error')

logging.basicConfig(level=logging.ERROR)
logging.debug('Debug message')
logging.info('Program started..')
logging.info('Loading files')
logging.error('This is an error')

# Regular expressions, testing if a string contains another string
>>> s = "Are you afraid of ghosts?"
>>> "ghosts" in s
True
>>> "coffee" not in s
True
>>>

import re
s = "123"
matcher = re.match('\d{3}\Z',s)

if matcher:
    print("True")
else:
    print("False")

    # \d     Matches a decimal digit; equivalent to the set [0-9].
    # \D     The complement of \d. It matches any non-digit character; equivalent to the set [^0-9].
    # \s     Matches any whitespace character; equivalent to [ \t\n\r\f\v].
    # \S     The complement of \s. It matches any non-whitespace character; equiv. to [^ \t\n\r\f\v].
    # \w     Matches any alphanumeric character; equivalent to [a-zA-Z0-9_].
    # \W     Matches the complement of \w.
    # \b     Matches the empty string, but only at the start or end of a word.
    # \B     Matches the empty string, but not at the start or end of a word.
    # \\     Matches a literal backslash.

# Classes
class ShoppingList:
    products = []

    def __init__(self):
        print('Shopping list created')

    def add(self, name):
        self.products.append(name)

    def show(self):
        print(self.products)

groceries = ShoppingList()
groceries.add('Peanutbutter')
groceries.add('Milk')
groceries.show()
