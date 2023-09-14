# TODO: Make title 
print (41 * "-")
print ("|----------- Speed converter -----------|")
print (41 * "-") 
# TODO: Get user input
mph = float(input("Enter the MPH: "))
# TODO: Echo user input
print (f"You entered {mph} MPH")
# TODO: Convert and display Miles to Kilometers
km = mph * 1.60934
print (f"Kilometers: {km:,.3f} ")
# TODO: Convert and display Miles to Barleycorns per day
bc = (mph * 189334.58824) * 24
print (f"Barleys per day: {bc:,.3f} ")
# TODO: Convert and display Miles to Furlongs per fortnight
fpf = mph * 2687.99
print (f"Furlongs per fortnight: {fpf:,.3f}")
# TODO: Convert and display Miles to Mach number 
mach = mph / 767.269
print (f"Mach number: {mach:.15f}")
# TODO: Convert and display Miles to Percentage of speed of light
psl = mph / 670616629
print (f"Percentage of speed of light: {psl:.15f}")
# TODO: Convert and display Miles to Days to reach the moon
moon_travel = 240000 / mph / 24.0
print (f"Days to reach the moon: {moon_travel:,.3f}")

