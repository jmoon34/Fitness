import json


class Food(dict):
    def __init__(self, name, calories, unit, amount):
        dict.__init__(self, name=name, calories=calories, unit=unit, amount=amount)
        self.name = name
        self.calories = calories
        self.unit = unit
        self.amount = amount
        # Ingredients structure => {ingredient_i: amount_i}
        #self.ingredients = {}
        # Recipe is a list that contains the steps for preparation in order
        #self.recipe = []

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

    #def add_ingredients(self, ingredient):
        #self.ingredients.append(ingredient)

    def calculate_amount_calories(self):
        return (self.amount * self.calories) / self.unit

    @staticmethod
    def create_food():
        food_name = str(input("Enter food name: "))
        food_calorie = int(input("Enter calories: "))
        food_unit = int(input("Enter unit: "))
        food_amount = int(input("Enter amount: "))
        return Food(food_name, food_calorie, food_unit, food_amount)




