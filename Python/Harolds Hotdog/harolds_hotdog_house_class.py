HOTDOG_COST = 8.99

class HaroldsHotdogs:
    def __init__(self):
        pass

    def calculate(self, number_of_hotdogs):
        # TODO: Calculate cost of the hotdogs purchased
        self.number_of_hotdogs = number_of_hotdogs
        self.total_cost = number_of_hotdogs * HOTDOG_COST