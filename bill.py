# Define a function named calculate_total_bill.
# This function should take two arguments: item_price and quantity.

def calculate_total_bill(item_price, quantity=1):
    """
    Calculate the total cost for an item or multiple items.

    Args:
        item_price (float): The price of one item.
        quantity (int, optional): The quantity of items (default is 1).

    Returns:
        float: The total cost after applying discounts.
    """
    # Calculate the total cost without any discounts
    total_cost=item_price*quantity#todo1

    # Apply a discount for bulk purchases
    # If the quantity is 10 or more, apply a 10% discount
    if quantity >= 10:
        # Apply the discount here
        total_cost=item_price*quantity - ((10/100)*(item_price*quantity))# TODO 2:

    # Apply a 5% discount for items priced above ₹100
    if item_price > 100:
        # Apply the discount here
        total_cost=item_price*quantity-((5/100)*(item_price*quantity))# TODO 3

    # Return the total cost after applying discounts
    return total_cost

# Create a shopping cart with item prices and quantities
shopping_cart = [
    {"item_price": 25.0, "quantity": 3},
    {"item_price": 120.0, "quantity": 2},
    {"item_price": 8.0, "quantity": 12},
]

# Calculate the total bill for the shopping cart using a loop
total_bill = 0.0

for item in shopping_cart:#for loop
    item_price = item["item_price"]
    quantity = item["quantity"]
    # Calculate the total cost for the current item
    item_total = calculate_total_bill(item_price, quantity)
    # Add the item total to the overall bill
    total_bill=item_total+total_bill# TODO 5: Remove this line and fill in the total_bill addition

# Print the total bill for the customer
print(f"Total Bill: {total_bill}")

