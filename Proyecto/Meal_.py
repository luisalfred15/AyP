from Food_ import Food

class Meal(Food):
    def __init__(self, name, quantity, price, is_packaged):
        super().__init__(name, quantity, price)
        self.is_packaged = is_packaged