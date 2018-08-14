#----------------------------------------#
# Question 1
# Level 1

# Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# Hints: 
# Consider use range(#begin, #end) method
# Solution:

list_of_numbers=[]
for number in range(2000,3200):
    if number%7==0 and number%5!=0:
        list_of_numbers.append(str(number))
print(','.join(list_of_numbers))


#----------------------------------------#
# Question 2
# Level 1

# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Solution:
def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)
print(factorial(int(input("Enter number to calculate factorial: "))))


#----------------------------------------#
# Question 3
# Level 1

# Question:
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# Consider use dict()

# Solution:

squares = {}
num = int(input("Enter number for squares: "))
for n in range(1,num):
    squares[n] = n*n
print(squares)

#----------------------------------------#
# Question 4
# Level 1

# Question:
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# tuple() method can convert list to tuple

# Solution:

string = input("Enter comma separated numbers: ")
lst = string.split(",")
tupl = tuple(lst)
print(lst)
print(tupl)

#----------------------------------------#
# Question 5
# Level 1

# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# Hints:
# Use __init__ method to construct some parameters

# Solution:

class processString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("")
    def printString(self):
        print(self.s)

newObj = processString()
newObj.getString()
newObj.printString()

#----------------------------------------#
# Question 6
# Level 2

# Question:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24

# Hints:
# If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26)
# In case of input data being supplied to the question, it should be assumed to be a console input. 

# Solution:
import math

inlist = input("Enter comma separated string of numbers: ")
c = 50
h = 30
ans = []
for d in inlist.split(","):
    ans.append(str(int(math.sqrt((2*c*int(d)/h)))))
print( ",".join(ans))


# Question 7
# Level 2

# Question:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

# Hints:
# Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.

# Solution:

multiples = input("Enter two comma separated numbers: ")
nums = multiples.split(",")
anslist = []
for i in range(int(nums[0])):
    tmplist = []
    for j in range(int(nums[1])):
        tmplist.append(i*j)
    anslist.append(tmplist)
print(anslist)


#----------------------------------------#
# Question 8
# Level 2

# Question:
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Solution:
string = input("Enter some words separated by comma: ")
word_list = string.split(",")
word_list.sort()
print(word_list)

#----------------------------------------#
# Question 9
# Level 2

# Question£º
# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Solution:
while True:
    s = input("Enter some text: ")
    if s:
        print(s.upper())
    else:
        break

#----------------------------------------#
# Question 10
# Level 2

# Question:
# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# We use set container to remove duplicated data automatically and then use sorted() to sort the data.

# Solution:
string = input("Enter a sentence: ")
word_list = string.split()
print(" ".join(sorted(set(word_list))))

