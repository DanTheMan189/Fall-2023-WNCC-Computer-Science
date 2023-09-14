import math

# TODO: Make title for program
print (47 * ("-"))
print ("----------     Circle Calculator     ----------")
print (47 * ("-"))

# TODO: Get user input for radius
radius = (float(input("Enter number for radius: ")))
# TODO: Put in formula for diameter of circle
diameter = radius * 2
# TODO: Put in formula for circumference of circle
circumference = math.pi * (radius * radius)
# TODO: Print out the radius entered by user
print (f"Radius entered: {radius:.2f}")
# TODO: Print out the diameter
print (f"Diameter: {diameter:.2f}")
# TODO: Print out the circumference
print (f"Circumference: {circumference:.2f}")