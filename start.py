from order import FoodOrder, process_food_order

def display_order_result(result):
    if isinstance(result, list):
        order = FoodOrder(result)
        print('*' * 50)
        print(f"Food Order ID: {order.order_id}")
        print(f"Date: {order.order_date}")
        print(f"Items Ordered: {order.food_items}")
        print(f"Total Calories: {order.total_calories}")
        if order.order_accepted:
            print("Food Order accepted!")
            print(f"Total Price: {order.order_price} euros")
        else:
            print("Food Order refused!")
            print(f"Reason: {order.order_refused_reason}")
    else:
        print(result)

result = process_food_order()
display_order_result(result)
