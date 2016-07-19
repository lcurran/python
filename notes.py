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

# lists
c = [5,2,10,48,32,16,49,10,11,32,64,55,34,45,41,23,26,27,72,18]
# elements accessed via index. negative index starts from the back
len(c) #returns length

# executes command line arguments like node if import sys module
import sys
sys.argv

#Tuple: collection that cannot be modified
x = (1,)
y = (1,2,3,4)
