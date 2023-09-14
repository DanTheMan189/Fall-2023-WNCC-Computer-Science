from rich.console import Console
from rich.panel import Panel

console = Console()




# TODO: Create known constants
overtime_pay = 40
overtime_rate = 1.5
# TODO: Make title for program
console.print (
    Panel.fit(
        "     Payroll Calculator        ",
        style= "bold blue",
        subtitle= "By: Daniel Hernandez"
    )
)
# TODO: Get user input for: Name
name = input("What is your name?: ")
# TODO:     Hourly rate
hourly_rate = float(input("What is your hourly rate?: "))
# TODO:     Hours worked
hours_worked = int(input("How many hours did you work?: "))
# TODO:     If the user uses a bonus code
bonus_code = input("Enter bonus code (a, b or press ENTER if you do not have one): ")

# TODO: Calculate total pay
# TODO:     Calculate regular pay
total_pay = hourly_rate * hours_worked

bonus_pay_a = total_pay * .1
bonus_pay_b = total_pay * .05

# TODO:     Calculate overtime pay if hours worked are over 40  
if hours_worked >=41:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (hourly_rate * overtime_rate)
    overtime_total_pay = total_pay + overtime_pay
    overtime_bonus_a = overtime_total_pay * .1
    overtime_bonus_b = overtime_total_pay * .05

elif hours_worked <=40: 
    overtime_pay = 0
    total_pay = hourly_rate * hours_worked + overtime_pay


    

# TODO: Echo user inputs
# TODO:     Display results
console.print (f"Payroll Advice: [bold blue]{name}[/bold blue]")
console.print (f"Regular Pay: [bold blue]${total_pay:,.2f}[/bold blue]")
console.print (f"Overtime Pay: [bold blue]${overtime_pay:,.2f}[/bold blue]")
# Checking if bonus code input is a
if bonus_code == "a":
    # Checking if hours worked is over 40 hours, if so print out bonus pay with overtime
    if hours_worked >=41:
        console.print (f"Bonus: [bold blue]${overtime_bonus_a:,.2f}[/bold blue]") 
    # Checking if hours worked is under 40 if so print out the bonus pay without the overtime
    elif hours_worked <=40:
        console.print (f"Bonus Pay: [bold blue]${bonus_pay_a:,.2f}[/bold blue]")
# Checking if bonus code input is b
elif bonus_code == "b":
    # TODO:
    if hours_worked >= 41:
        console.print (f"Bonus Pay: [bold blue]${overtime_bonus_b:,.2f}[/bold blue]") 
    # TODO:
    elif hours_worked <=40: 
        console.print (f"Bonus Pay: [bold blue]${bonus_pay_b:,.2f}[/bold blue]")
# If user input was neither then program will print out bonus as $0
else:
    console.print ("Bonus: [bold blue]$0[/bold blue]")
# Checking if hours worked is over 40, if so it will check what the bonus code input was
if hours_worked >=41:
    # Checking if the bonus code is a
    if bonus_code == "a":
        # Calculate the overtime total pay with the overtime bonus a
        overtime_total_pay = overtime_total_pay + overtime_bonus_a
        # Printing out the Gross Pay with overtime pay and bonus a
        console.print (f"Gross Pay: [bold blue]${overtime_total_pay:,.2f}[/bold blue]")
    # Checking if the bonus code is b
    elif bonus_code == "b":
        # Calculate the overtime total pay with the overtime bonus b
        overtime_total_pay = overtime_total_pay + overtime_bonus_b
        # Printing out the Gross Pay with the overtime pay and bonus b
        console.print (f"Gross Pay: [bold blue]${overtime_total_pay:,.2f}[/bold blue]")
    # If neither of the options were pressed then program with just print out the overtime pay with no bonus
    else:
        console.print (f"Gross Pay: [bold blue]${overtime_total_pay:,.2f}[/bold blue]")
# Checking if hours worked is over 40 hours
elif hours_worked <=40:
    # Checking if the bonus code is a
    if bonus_code == "a":
        total_pay = total_pay + bonus_pay_a
        console.print (f"Gross Pay: [bold blue]${total_pay:,.2f}[/bold blue]")
    # Checking if the bonus code is b
    elif bonus_code == "b":
        total_pay = total_pay + bonus_pay_b
        console.print (f"Gross Pay: [bold blue]${total_pay:,.2f}[/bold blue]")
    # If neither of the options were pressed then program with just print out the total pay with no bonus or overtime pay:
    else:
        console.print (f"Gross Pay: [bold blue]${total_pay:,.2f}[/bold blue]")
