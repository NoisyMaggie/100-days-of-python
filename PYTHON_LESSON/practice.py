print("Hello World!")
if 5 > 2:
     print("five is greater than two!")
#This is a comment.
print("Hello World")
#print("Hello, World")
print("Cheers, Mate")
#This is a comment
#written in
#more than just one line
print("Hello, World")
x = 5
x = "John"
print(x)
x = 4       #x is of type int
x = "Sally" #x is now of type str
print(x)
x = str(3)     #x will be '3'
y = int(3)     #y will be 3
z = float(3)   #z will be 3.0
a = 4
A = "Sally"
print(a)
print(A)
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
x = y = z = "Orange"
print(x)
print(y)
print(z)
fruit = ["apple", "banana", "cherry"]
x, y, z = fruit
print(x)
print(y)
print(z)
x = "python"
y = "is"
z = "awesome"
print(x + y + z)
x = 5
y = 10
print(x + y)
x = 5
y = "John"
print(x, y)
print('Hello', 'World')

x = "awesome"

def myfunc():
     x = "fantastic"
     print("python is " + x)

myfunc()

print("python is " + x)

def myfunc():
     global x              #global variables
     x = "fantastic"

myfunc()
print("python is " + x)

x = tuple(("apple", "banana", "cherry"))
print(type(x))
x = 5
print(type(x))
x = 35e3   
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))

x= frozenset({"apple", "banana", "cherry"})
print(type(x))
x = 1      #int
y = 2.8    #float
z = 1j     #complex

#convert int to float:
a = float(x) 

#convert float to int:
b = int(y) 

#convert int to complex:
c = complex(z)

print(a)                          #casting
print(b)
print(c) 

print(type(a))
print(type(b))
print(type(c)) 

import random

print(random.randrange(1,10))
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

print(x)
print(y)
print(z) 

print(int(35.88))
print(str(35.80))
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a) 
print("It's alright")
print("He is called 'Johnny'")
a = "Hello World"
print(a[1]) 
for x in "banana":          #looping through a string
     print(x) 

a = "Hello World"
print(len(a))

txt = "The best things in life are free!"
if "free" in txt:                #to check string
     print("expensive" not in txt)
txt = "The best things in life are free"
if "expensive" not in txt:       #check if not
     print("No, 'expensive' NOT present.")

b = "Hello, World"
print(b[2:5])
print(b[:5])               #slicing strings
print(b[2:]) 
print(b[-5:-2])

a = "Hello, World"
print(a.lower())    #modify strings
print(a.upper())
print(a.strip())    # returns "Hello, World!"
print(a.replace("H", "J")) 
print(a.split(","))

a = "Hello"
b = "World"         #to add space to concatenation
c = a + " " + b
print(c) 

age = 36               #format strings
txt = f"My name is John, I am {age}" 
print(txt) 
price = 59
txt = f"The price is {price} dollars"
print(txt) 
txt = f"The price is {price:.2f} dollars" 
print(txt) 
txt = f"The price is {20 * 59} dollars"
print(txt)

#escape character
txt = "We are the so-called \"Vikings\" from the north"
print(txt) 

#booleans
print(10 > 9)
print(10 == 9)
print(10 < 9) 
a = 200
b = 33

if b > a :
     print("b is greater than a")
else:
     print("b is not greater than a")
x = "Hello"
y = 15 
print(bool(x))
print(bool(y))
bool("abc")
bool(123)
bool(["apple", "banana", "cherry"])
bool(())
bool([]) 
bool("")
print(bool("")) 

class myclass():
     def _len_(self):
      return 0

myobj = myclass()
print(bool(myobj))

def myFunction():
     return True

print(myFunction())

def myFunction():
     return True

if myFunction():
     print("YES!")
else: print("NO!")

X = 200
print(isinstance(x,int)) 
print(5 > 3)
print(10 == 9)
print(bool("abc"))
print(bool(0))
print(6 & 3)
print(6 | 3)                #PEMAS rule
print((6 + 3) - (6 + 3))
x = 5
x += 3
print(x)
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)
list1 = ["abc", 34, True, 40, "male"]
print(list1)
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

integer_number = 123
float_number = 1.23

new_number = integer_number + float_number 

#display new value and resulting data type
print("value:" , new_number)
print("data Type:" , type (new_number)) 

num_string = '12'
num_integer = 23

print("Data Type of num_string before Type Casting:" , type(num_string))

#explicit data conversion 
num_string = int(num_string)
print("Data Type of num_string after conversion:" , type(num_string))

num_sum = num_integer + num_string  

print("Sum:", num_sum)
print("Data type of the num_sum:" , type(num_sum))

#print with end whitespace
print('Good Morning!' , end= ' ')
print('It is raining today')
print('New Year', '2023', 'see you soon!', sep= '. ')

x = 5
y = 10
print('The value of x is {} and y is {}' .format(x,y))

#using input() to take user input
num = input('Enter a number: ')

print('You Entered:', num)

print('Data type of num:', type(num))

a = 7
b = 2

#addition
print('Sum: ', a + b)

#subtraction
print('Subtraction: ', a - b)

#multiplication
print('Multiplication: ', a * b)

#division
print('Division: ', a / b)

#floor division
print('Floor Division: ', a // b)

#modulo
print('Modulo: ', a % b)

#a to the power of b
print('Power: ', a ** b)

#assign 10 to a
a = 10

#assign 5 to b
b = 5

#assign sum of a and b to a
a += b        #a = a + b
print(a)

#comparison operators
a = 5
b = 2

#equal to operator
print('a == b =', a == b)

#not equal to operator
print('a != b =', a != b)

#greater than operator
print('a > b =', a > b)

#less than operator
print('a < b =', a < b)

# greater than or equal to operator
print('a >= b =', a >= b)

# less than or equal to operator
print('a <= b =', a <= b)

# logical AND
print(True and True)     # True
print(True and False)    # False

# logical OR
print(True or False)     # True

# logical NOT
print(not True)          # False


def bill_split(amount, friends):
    tax = 20 / 100 * 100
    result = 20 + 100/ friends
    return result

# total bill= 20% + 100 /5
subtotal = 100
tax = 0.2   #iyen ni 20% tax
num_friends = 5

#calculate tax 
tax = 0.2 * 100
print(tax)

#calculate total with tax
total_with_tax = tax + subtotal

#calculate total for friends
total_for_friends = tax + subtotal / num_friends

print(f"subtotal is {subtotal:.2f} dollars")
print(f"tax is (20%) {tax:.2f} dollars")
print(f"total with tax is {total_with_tax:.2f} dollars")
print(f"total for friends is {total_for_friends:.2f} dollars")

