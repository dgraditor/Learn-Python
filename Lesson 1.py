print("Hello World")
#This is a comment. Comments will not be read by the program
#Variable
#Variables can hold four different types of data
#Integers can hold any whole number, even negatives
num = 5
print(num)
#Floats can hold decimals
float_num = 10.00
print(float_num)
#Strings are any kind of text that isn't a number. You surround these strings in quotations
var = "Hello, Class!"
print(var)
#Booleans can only hold one of two values: True or False
#Variable Rules
#1. You cannot add strings and integers together
#Concatenation = string addition
print("Yellow" + '7')
#2. Variables can have numbers in them BUT they must start with a letter
num2 = 10 #This is good
#2num = 15 #This is NOT good
#3. Variables are case sensitive (an uppercase letter is different from a lowercase letter)
A = "Uppercase"
a = "Lowercase"
print(A)
print(a)
#4. You can change a variable's value mid-code
var = "hello online class people!"
print(var)
#' and " will do the same thing
#DOING MATH 
#Addition, subtraction, multiplication, and division
#Modulus
print(5 + 10)
print(10 - 5)
print(100 - 100)
print(6 * 100)
print(100 * 100)
#Concatenation
name = "Dawson"
print("hello, stranger " + name)
#Functions
#All functions will and must have a pair of parenthesis at the end
#Notable Functions include:
#Print(): This will print any text inside the parenthesis on your screen
#Input(): This will take any user input and place it inside a variable
name = input("What is your name?")
print(name)
#User inputs will always be recognized as STRINGS
#Conversion functions will convert a value from one datatype to another
num1 = input("Enter a number!")
num2 = input("Enter a second number!")
print(num1 + num2) #Print the concatenation of two strings
print(int(num1) + int(num2)) #Print the sum of two strings
print(int(num1 + num2)) #Print the concatenation of two strings
#Length function: Counts how many characters are in a string
long = "saoidasidjaiodj"
len_long = len(long)
print(len_long)
