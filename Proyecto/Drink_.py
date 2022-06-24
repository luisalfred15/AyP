from Food_ import Food

class Drink(Food):
    def __init__(self, name, quantity, price, is_alcoholic):
        super().__init__(name, quantity, price)
        self.is_alcoholic = is_alcoholic