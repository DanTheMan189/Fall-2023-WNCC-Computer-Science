DASHES = "-----------------------------------"

print (f"{DASHES}")
print ("Number\tSquare\tCube")
print (f"{DASHES}")

for i in range (1, 11):
	square = i * i
	cube = i * i * i
	print (f"{i}\t{square}\t{cube}")
print (f"{DASHES}")
