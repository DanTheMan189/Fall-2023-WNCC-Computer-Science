import math
import random

print (45 * "-")
print ("-------------   Fun With Math   -------------")
print (45 * "-")

print ("Modulus of 45: ", end="")
print (45 % 2)

print ("Integer division 65 // 9: ", end="")
print (65 // 2)

print ("Max of 3 and 5: ", end="")
print (max(3, 5))

print ("Min of 3 and 5: ", end="")
print (min(3, 5))

print ("Value of pi in Python: ", end="")
print (math.pi)

print ("Square root of 4: ", end="")
print (math.sqrt(4))

print ("4 to the power of 10: ", end="")
print (4**10)

print ("Absolute value of -5: ", end="")
absolute_value = abs(-5)
print (absolute_value)

print ("Rounded to 2 decimal points: ", end="")
print (round(20.0 / 3.0, 2))

print ("Rounded up to int: ", end="")
print (math.ceil(20.0 / 3.0))

print ("Rounded down to int: ", end="")
print (math.floor(20.0 / 3.0))

print ("Rounded to 4 decimal points: ", end="")
rounded = round((20.0 * 10.0 / 3.0) / 100.0, 4)

print ("Random integers between 1 and 6 inclusive: ", end="")
print (random.randint(1,6))