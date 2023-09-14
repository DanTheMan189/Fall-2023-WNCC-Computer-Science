while True:
	try:
		age = int(input("Enter your age:" ))
	except Exception as e:
		print (e)
		print ("Please use a whole number.")

		continue 

	if age < 1:
		print ("Please enter a positive.")
		continue 

	else: 
		break 
print (f"Your age is: {age}")
