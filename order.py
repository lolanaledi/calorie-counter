import uuid
from datetime import datetime
from counters import calculate_calories, calculate_price
from load_data import load_data

class FoodOrder:
    def __init__(self, items, date=None):
        self.order_id = str(uuid.uuid4().hex)[:6]
        self.order_accepted = False
        self.order_refused_reason = ""
        self.order_date = date if date else datetime.now()
        self.food_items = items

    @property
    def total_calories(self):
        total_calories = calculate_calories(self.food_items)
        if total_calories <= 2000:
            self.order_accepted = True
        else:
            self.order_refused_reason = "Your food order exceeds the maximum calories allowed"
        return total_calories

    @property
    def order_price(self):
        return calculate_price(self.food_items)

def display_food_menu(dishes, combinations):
    dish_names = ', '.join(dish['name'] for dish in dishes)
    combo_names = ', '.join(combo['name'] for combo in combinations)
    print(f"Name of the meals: {dish_names}, and {combo_names}.")

def get_customer_food_orders():
    print("Order your food: ")
    return input()

def process_food_order():
    all_dishes = load_data("data/meals.json")['meals']
    all_combinations = load_data("data/combos.json")['combos']

    display_food_menu(all_dishes, all_combinations)

    user_orders = get_customer_food_orders()
    result = food_order_checker(user_orders)

    return result

def food_order_checker(order):
    items = [item.strip() for item in order.split(',')]
    dishes_data = load_data("data/meals.json")
    combos_data = load_data("data/combos.json")

    dish_names = {dish['name'] for dish in dishes_data['meals']}
    combo_names = {combo['name'] for combo in combos_data['combos']}

    invalid_items = [item for item in items if item not in dish_names and item not in combo_names]

    if invalid_items:
        return f"Wrong item in the order: {', '.join(invalid_items)}."
    
    return items