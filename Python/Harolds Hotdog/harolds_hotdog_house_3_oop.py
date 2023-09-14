hotdog_cost = 8.99


class HaroldsHotdog:
    def __init__(self):
        pass
        

    def get_input(self):
        # TODO: Get user input for hotdogs sold
        self.number_of_hotdogs = int(input("Enter number of hotdogs: "))
        return self.number_of_hotdogs

    def calculate(self):
        # TODO: Calculate cost of the hotdogs purchased
        self.total_cost = self.number_of_hotdogs * hotdog_cost
        

    def display(self):
        # TODO: Display results
        print (f"Your meal was: ${self.total_cost:,.2f}")
        


harolds_hotdogs = HaroldsHotdog()
harolds_hotdogs.get_input()
harolds_hotdogs.calculate()
harolds_hotdogs.display()
