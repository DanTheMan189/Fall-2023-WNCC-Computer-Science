age = int(input("Enter your age: "))

movie_rating = input("Enter movie rating (PG-13 or R): ").upper()

if (age >= 13 and movie_rating == "PG-13") or (age <= 17 and movie_rating == "R"):
    print ("You can watch this movie")

else:
    print ("Sorry, you are not eligible to watch this movie.")