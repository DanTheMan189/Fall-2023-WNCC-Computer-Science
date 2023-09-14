print ("===============================")
print ("|       Is it positive?       |")
print ("===============================")

num = float(input("Input a number: "))

if num > 0:
    result = "is a positive number"
elif num == 0:
    result = "is zero"
else:
    result = "is a negative number"

print (f"{num} {result}")