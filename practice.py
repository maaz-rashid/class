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
