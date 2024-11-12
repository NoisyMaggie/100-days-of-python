# Write a Python function called calculate_area that takes the shape of a geometric figure as input (either "rectangle", "triangle", or "circle") and calculates the area based on user-provided dimensions.

# For a rectangle, prompt the user to input the length and width.
# For a triangle, prompt the user to input the base and height.
# For a circle, prompt the user to input the radius.
# Make sure your function handles invalid shapes and provides appropriate error messages. Use appropriate formulas for each shape:

# Area of a rectangle = length × width
# Area of a triangle = 0.5 × base × height
# Area of a circle = π × radius² (you can use 3.14159 for π)
# The function should print the calculated area of the shape.

# Sample Output:

# mathematica
# Copy code
# Enter the shape (rectangle, triangle, circle): rectangle
# Enter the length: 5
# Enter the width: 3
# The area of the rectangle is 15.0
# mathematica
# Copy code
# Enter the shape (rectangle, triangle, circle): circle
# Enter the radius: 4
# The area of the circle is 50.26544

def calculate_area():
    print("press 1 for rectangle")
    print("press 2 for circle")
    print("press 3 for triangle")
    user_input = input() 
    if user_input == "1":
        length = input("Enter the length of the rectangle ")
        width = input("Enter the width of the rectangle ")
        area = int(length) * int(width)
        print(f"the area of the rectangle for {length} and {width} is {area}")

    elif user_input == "2":
        pie = 3.142
        radius = float(input("Enter the radius of the circle "))
        area = pie * radius**2 
        print(f"the area of circle for {radius} is {area}")
    
    elif user_input == "3":
        base = float("Enter the base of the triangle ")
        height = float("Enter the height of the triangle ") 
        area = 0.5 * base * height
        print(f"the area of triangle is {area}")

    else:
        print("invalid option")

calculate_area() 