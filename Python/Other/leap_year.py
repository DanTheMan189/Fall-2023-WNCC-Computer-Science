# TODO: Get user input for year
year = int(input("Enter year: "))

# TODO: Give the restictions and requirements to say that it's / isn't a leap year
if (year % 4 == 0) or (year % 100 == 0 and year % 400 != 0):
    # TODO: Print that the year inputed  is a leap year
    print (f"{year} is a leap year")
else: 
    # TODO: Print out that it's not a leap year
    print (f"{year} is not a leap year")