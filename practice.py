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

#----------------------------------------#
# Question 11
# Level 2

# Question:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Solution:

items = [x for x in input("Enter comma separated binary digits: ").split(",")]
ans = []
for x in items:
    if (int(x,2))%5 == 0:
        ans.append(x)

print(",".join(ans))

#----------------------------------------#
# Question 12
# Level 2

# Question:
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Solution:
ans = []
for x in range(1000,3001):
    strngx = str(x)
    if (int(strngx[0])%2 == 0) and (int(strngx[1])%2 == 0) and (int(strngx[2])%2 == 0) and (int(strngx[3])%2 == 0):
        ans.append(strngx)

print(",".join(ans))

#----------------------------------------#
# Question 13
# Level 2

# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Solution:
strInput = input("Enter a sentense: ")
letterCount = 0
numCount = 0
for char in strInput:
    if char.isdigit():
        numCount += 1
    elif char.isalpha():
        letterCount +=1
    else:
        pass

print(f"No. Letters: {letterCount}")
print(f"No. Digits: {numCount}")

#----------------------------------------#
# Question 14
# Level 2

# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

strInput = input("Enter a sentense: ")
upperCount = 0
lowerCount = 0
for char in strInput:
    if char.isupper():
        upperCount += 1
    elif char.islower():
        lowerCount +=1
    else:
        pass

print(f"UPPER CASE: {upperCount}")
print(f"LOWER CASE: {lowerCount}")

#----------------------------------------#
# Question 15
# Level 2

# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Solution:
a = int(input("Enter a number: "))
b = int(input("Enter range: "))
def Power(num,pow):
    return num**pow
c=0
for item in range(1,b+1):
   c+=Power(a,item)

print(c)



a = input("Enter a number: ")
b = int(input("Enter range: "))
def Multiples(num,multipl):
    return num*multipl
c=0
for item in range(1,b+1):
       c+= int(Multiples(a,item))
print(c)

#----------------------------------------#
# Question 16
# Level 2

# Question:
# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Solution:
strInput = input("Enter comma separated numbers: ")
list_of_odd_squares = [int(x)**2 for x in strInput.split(",") if int(x)%2 != 0 ]
print( ",".join(list_of_odd_squares))

#----------------------------------------#
# Question 17
# Level 2

# Question:
# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200
# ¡­
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Solution:
balance = 0
while True:
    strInput = input("Enter transaction: ")
    if not strInput:
        break
    vals = strInput.split()
    if vals[0] == "D":
        balance += int(vals[1])
    elif vals[0] == "W":
        balance -= int(vals[1])
    else:
        pass

print(balance)

#----------------------------------------#
# Question 18
# Level 3

# Question:
# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
import re
strInput = input("Enter passwords: ")
passwords = strInput.split(",")
goodPass = []
for pas in passwords:
    if len(pas) > 6 and len(pas) < 13:
        if re.match(r'[A-Za-z0-9]',pas):
            if re.search("[$#@]",pas):
                goodPass.append(pas)

print(",".join(goodPass))

#----------------------------------------#
# Question 19
# Level 3

# Question:
# You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# We use itemgetter to enable multiple sort keys.

# Solutions:
from operator import itemgetter
initList = []
while True:
    s = input("Enter info: ")
    if not s:
        break
    initList.append(tuple(s.split("",)))

print(sorted(initList, key=itemgetter(0,1,2)))


#----------------------------------------#
# Question 20
# Level 3

# Question:
# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

# Hints:
# Consider use yield

# Solution:
def divisble_by_seven(num):
    for x in range(num+1):
        if x%7==0:
            yield x

nums = divisble_by_seven(100)

for n in nums:
    print(n)

#----------------------------------------#
# Question 21
# Level 3

# Question
# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# ¡­
# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Solution:
import math
position = [0,0]
while True:
    s = input("Enter direction and steps: ")
    if not s:
        break
    to_move = s.split()
    direction = to_move[0]
    steps = int(to_move[1])
    if direction == "UP":
        position[0] += steps
    elif direction == "DOWN":
        position[0] -= steps
    elif direction == "LEFT":
        position[1] -= steps
    elif direction == "RIGHT":
        position[1] += steps
    else:
        pass

print(int(round(math.sqrt(position[0]**2 + position[1]**2))))

#----------------------------------------#
# Question 22
# Level 3

# Question:
# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1

# Hints
# In case of input data being supplied to the question, it should be assumed to be a console input.

s = input("Enter a senctence: ")
initList = s.split()
freq = { x:initList.count(x) for x in initList }
freq = { x:freq.get(x) for x in sorted(freq.keys())}
for x in freq.keys():
    print(f"{x} : {freq.get(x)}")


from collections import Counter
newdict = dict(Counter(initList))
newdict = { x:newdict.get(x) for x in sorted(newdict.keys())}
for x in newdict.keys():
    print(f"{x} : {newdict.get(x)}")



#----------------------------------------#
# Question 23
# level 1

# Question:
#     Write a method which can calculate square value of number

# Hints:
#     Using the ** operator

def square(num):
    print(f"square of {num} is: {num**2}")
    return num**2

while True:
    s = input("Enter a number: ")
    if not s:
        break
    square(int(s))


print(abs().__doc__)
print(int().__doc__)


#----------------------------------------#
# Question 25
# Level 1

# Question:
#     Define a class, which have a class parameter and have a same instance parameter.

# Hints:
#     Define a instance parameter, need add it in __init__ method
#     You can init a object with construct parameter or set the value later

# Solution:

class Person:
    name = "Person Name"
    def __init__(self, name = None):
            self.name = name
    
jeff = Person("Jeffery")
print(f"{Person.name}'s name is {jeff.name}")

#----------------------------------------#
# Question 26:
# Define a function which can compute the sum of two numbers.

# Hints:
# Define a function with two numbers as arguments. You can compute the sum in the function and return the value.

# Solution
def sum(a,b):
    return a+b

print(f"{sum(4,4)}")

#----------------------------------------#
# Question 27:
# Define a function that can convert a integer into a string and print it in console.

# Hints:

# Use str() to convert a number to string.

# Solution

def toStr(num):
    print(str(num))

toStr(8)

#----------------------------------------#
# Question 28:
# Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.

# Hints:

# Use int() to convert a string to integer.

# Solution
def sumOfStr(num1,num2):
    print(int(num1) + int(num2))

sumOfStr("4","5")

#----------------------------------------#
# Question 29:
# Define a function that can accept two strings as input and concatenate them and then print it in console.

# Hints:

# Use + to concatenate the strings

# Solution
def concat(s1,s2):
    print(s1+s2)

concat("3","2")

#----------------------------------------#
# Question 30:
# Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.

# Hints:

# Use len() function to get the length of a string

# Solution
def printLongest(s1,s2):
    if len(s1)>len(s2):
        print(s1)
    elif len(s2)>len(s1):
        print(s2)
    else:
        print(s1)
        print(s2)

printLongest("Hello","World")

#----------------------------------------#
# Question 31:
# Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".
# Hints:
# Use % operator to check if a number is even or odd.

# Solution
def checkNum(num):
    if num%2==0:
        print("It's an even number.")
    else:
        print("It's an odd number.")

checkNum(5)

#----------------------------------------#
# Question 32:
# Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.

# Hints:

# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.

# Solution
def dict1to3():
    newdict = { x:x**2 for x in range(1,4) }
    print(newdict)

dict1to3()

#----------------------------------------#
# Question 33:
# Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

# Hints:

# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.
# Use range() for loops.

# Solution
def dict1to20():
    newdict = { x:x**2 for x in range(1,21) }
    print(newdict)

dict1to20()

#----------------------------------------#
# Question 34:
# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the values only.

# Hints:

# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.
# Use range() for loops.
# Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.

# Solution
def dict1to20vals():
    newdict = { x:x**2 for x in range(1,21) }
    [print(v) for (k,v) in newdict.items()]

dict1to20vals()

#----------------------------------------#
# Question 35:
# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.

# Hints:

# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.
# Use range() for loops.
# Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.

# Solution

def dict1to20keys():
    newdict = { x:x**2 for x in range(1,21) }
    [print(k) for (k,v) in newdict.items()]

dict1to20keys()

#----------------------------------------#
# Question 36:
# Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

# Hints:

# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.

# Solution
def lst1to20keys():
    newlst = [x**2 for x in range(1,21)]
    print(newlst)

lst1to20keys()

#----------------------------------------#
# Question 37:
# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.

# Hints:

# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.
# Use [n1:n2] to slice a list

# Solution
def lst20top():
    newlst = [x**2 for x in range(1,21)]
    print(newlst[:5])

lst20top()

#----------------------------------------#
# Question 38:
# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.

# Hints:

# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.
# Use [n1:n2] to slice a list

# Solution
def lst20last():
    newlst = [x**2 for x in range(1,21)]
    print(newlst[-5:])

lst20last()

#----------------------------------------#
# Question 39:
# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.

# Hints:

# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.
# Use [n1:n2] to slice a list

# Solution
def lst20but5():
    newlst = [x**2 for x in range(1,21)]
    print(newlst[5:])

lst20but5()

#----------------------------------------#
# Question 40:
# Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included). 

# Hints:

# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.
# Use tuple() to get a tuple from a list.

# Solution
def lst20tuple():
    newlst = [x**2 for x in range(1,21)]
    print(tuple(newlst))

lst20tuple()

#----------------------------------------#
# Question 41:
# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line. 

# Hints:
# Use [n1:n2] notation to get a slice from a tuple.

# Solution:

tupl = (1,2,3,4,5,6,7,8,9,10)
print(tupl[:5])
print(tupl[5:])

#----------------------------------------#
# Question 42:
# Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10). 

# Hints:
# Use "for" to iterate the tuple
# Use tuple() to generate a tuple from a list.

# Solution
tupl = (1,2,3,4,5,6,7,8,9,10)
print(tuple([x for x in tupl if x%2==0]))

#----------------------------------------#
# Question 43:
# Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No". 

# Hints:
# Use if statement to judge condition.

# Solution:
s = input()
if s.upper()=="YES":
    print("Yes")
else:
    print("No")

#----------------------------------------#
# Question 44:
# Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

# Hints:

# Use filter() to filter some elements in a list.
# Use lambda to define anonymous functions.

# Solution:

li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = filter(lambda x: x%2==0, li)
print(list(evenNumbers))

#----------------------------------------#
# Question 45:
# Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

# Hints:

# Use map() to generate a list.
# Use lambda to define anonymous functions.

# Solution
li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = filter(lambda x: x%2==0, li)
print(list(evenNumbers))

#----------------------------------------#
# Question 46:
# Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

# Hints:
# Use map() to generate a list.
# Use filter() to filter elements of a list.
# Use lambda to define anonymous functions.

# Solution
li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = map(lambda x: x**2, filter(lambda x: x%2==0, li))
print(list(evenNumbers))

#----------------------------------------#
# Question 47:
# Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

# Hints:
# Use filter() to filter elements of a list.
# Use lambda to define anonymous functions.

# Solution:
evenNumbers = list(filter(lambda x: x%2==0, range(1,21)))
print(evenNumbers)

#----------------------------------------#
# Question 48:
# Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

# Hints:
# Use map() to generate a list.
# Use lambda to define anonymous functions.

# Solution
evenNumbers = list(map(lambda x:x**2, range(1,21)))
print(evenNumbers)


#----------------------------------------#
# Question 49:
# Define a class named American which has a static method called printNationality.

# Hints:
# Use @staticmethod decorator to define class static method.

# Solution

class American(object):
    @staticmethod
    def printNationality():
        print("American")
    
    def nationality(self):
        print("American")


anAmerican = American()
anAmerican.printNationality()
anAmerican.nationality()
American.printNationality()
American.nationality(anAmerican)


#----------------------------------------#
# Question 50:
# Define a class named American and its subclass NewYorker. 

# Hints:
# Use class Subclass(ParentClass) to define a subclass.

# Solution:
class NewYorker(American):
    pass


#----------------------------------------#
# Question 51:
# Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area. 

# Hints:

# Use def methodName(self) to define a method.

# Solution:
class Circle(object):
    def __init__(self, r):
        self.radius = r
    
    def area(self):
        print(2*self.radius*3.14)
newCircle = Circle(3)
newCircle.area()

#----------------------------------------#
# Question 52:
# Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area. 

# Hints:
# Use def methodName(self) to define a method.

# Solution:
class Rectangle(object):
    def __init__(self,l,w):
        self.length = l
        self.width = w
    
    def area(self):
        print(self.length*self.width)

rect = Rectangle(3,5)
rect.area()

#----------------------------------------#
# Question 53:
# Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

# Hints:
# To override a method in super class, we can define a method with the same name in the super class.

# Solution:

class Shape(object):
    def __init__(self):
        pass
    
    def area(self):
        print(0)
        