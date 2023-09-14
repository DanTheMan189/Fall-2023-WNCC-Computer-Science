hotdog_cost = 8.99

def main():
    num_of_hotdogs = get_input()
    total_sale = calculate(num_of_hotdogs)
    display(total_sale)
    

def get_input():
    # TODO: Get user input for hotdogs sold
    number_of_hotdogs = int(input("Enter number of hotdogs: "))
    return number_of_hotdogs

def calculate(number_of_hotdogs):
    # TODO: Calculate cost of the hotdogs purchased
    total_cost = number_of_hotdogs * hotdog_cost
    return total_cost

def display(total_cost):
    # TODO: Display results
    print (f"Your meal was: ${total_cost:,.2f}")
    return total_cost


if __name__ == "__main__":
    main()