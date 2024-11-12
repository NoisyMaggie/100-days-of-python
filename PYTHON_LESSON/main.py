# Madlibs game
# a word game where you create a story 
# by filling blanks with random words 

# verb1 = input("Enter a verb (action): ") 
# adjective1 = input("Enter an adjective (decription): ")
# verb2 = input("Enter a verb ending with 'ing': ")
#verb3 = input("Enter a verb:")

#print(f"Today, I went to a {verb1} house")
#print(f"It had a {adjective1} theme to it")
#print(f"It had my firends {verb2} out their lungs")
#print(f"I enjoyed watching my friends {verb3} in the {verb1} house")

#To calculate the radius of a Circle

#import math
#radius = float(input("Enter the radius of the circle: "))
#area = math. pi * pow(radius, 2)

#print(f"The area of the circle is: {round(area, 2)}cm^2")

#import math
#a = float(input("Enter side a: "))
#b = float(input("Enter side b: "))
#c = math. sqrt(pow(a, 2) + pow(b, 2))

#print(f"The value for side c is {c}")

#age = int(input("Enter your age:"))
#if age >= 18:
   # print("You are now signed up!")
#elif age < 1:
    #print("You are too young to be signed up")

#else: 
    #print("You have to be 18+ to be signed up")

#python calculator

operator = input("Enter an operator (+ - * /): ")

num1 = float(input("Enter the first number: "))

num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print(result)

elif operator == "-":
    result = num1 - num2
    print(result)

elif operator == "*":
    result = num1 * num2
    print(result)

elif operator == "/":
    result = num1 / num2
    print(result)

else:
    print(f"The {operator} is invalid")
 