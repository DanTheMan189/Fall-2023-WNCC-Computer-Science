import harolds_hotdog_house_class as hotdog


def get_input():
    # TODO: Get user input for hotdogs sold
    number_of_hotdogs = int(input("Enter number of hotdogs: "))
    return number_of_hotdogs


def display():
    # TODO: Display results
    number_of_hotdogs = harolds_hotdogs.number_of_hotdogs
    total_cost = harolds_hotdogs.total_cost

    print (f"Number of hotdogs: {number_of_hotdogs}")
    print (f"Your meal total: ${total_cost:,.2f}")


number_of_hotdogs = get_input()

harolds_hotdogs = hotdog.HaroldsHotdogs()

harolds_hotdogs.calculate(number_of_hotdogs)

display()
