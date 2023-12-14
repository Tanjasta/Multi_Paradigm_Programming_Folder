
# This imports a csv file
import csv

# Function that is creating and stocking the shop from a CSV file.
def create_and_stock_shop(filename='stock.csv'):
    shop = {'cash': 0.0, 'products': []}
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_row = next(csv_reader)
        shop["cash"] = float(first_row[0])
        for row in csv_reader:
            shop["products"].append({
                "name": row[0],
                "price": float(row[1]),
                "quantity": int(row[2])
            })
    return shop

# Function that reads customer data from a CSV file.
def read_customer(filename):
    customer = {'name': '', 'cash': 0.0, 'products': []}
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_row = next(csv_reader)
        customer["name"] = first_row[0]
        customer["cash"] = float(first_row[1])
        for row in csv_reader:
            customer["products"].append({
                "name": row[0],
                "quantity": int(row[1])
            })
    return customer

# Function that prints product details.
def print_product(product):
    print(f'NAME: {product["name"]}, PRICE: {product["price"]}, QUANTITY: {product["quantity"]}')

# Function that prints customer details.
def print_customer(customer):
    print(f'NAME: {customer["name"]}, CASH: {customer["cash"]}')
    for product in customer["products"]:
        print(f'NAME: {product["name"]}, QUANTITY: {product["quantity"]}')

# Function that processes an order.
def process_order(shop, customer):
    total_cost = 0
    order_items = []

    # Calculating total cost of the order and prossesing order items.
    for c_product in customer["products"]:
        for s_product in shop["products"]:
            if c_product["name"] == s_product["name"]:
                if c_product["quantity"] <= s_product["quantity"]:
                    total_cost += c_product["quantity"] * s_product["price"]
                    order_items.append(c_product)
                else:
                    print(f"Not enough stock for {c_product['name']}")
                break

    # Checking if customer has enough cash for the items.
    if customer["cash"] >= total_cost:
        # Processing the order.
        for c_product in order_items:
            for s_product in shop["products"]:
                if c_product["name"] == s_product["name"]:
                    s_product["quantity"] -= c_product["quantity"]
                    print(f"Order processed for {c_product['name']} quantity: {c_product['quantity']}")
                    break
        shop["cash"] += total_cost
        print(f"Total cost: {total_cost}. Remaining cash in the shop: {shop['cash']}")
    else:
        print(f"Customer {customer['name']} does not have enough cash for this order. Order not processed.")

# Function that is reading user input for live mode.
def read_user_input():
    product_name = input("Enter product name: ").strip()
    if product_name.lower() == "exit":
        return None
    quantity = int(input("Enter quantity: "))
    return {"name": product_name, "quantity": quantity}

# Function that operates in live mode
def operate_live_mode(shop):
    while True:
        customer_input = read_user_input()
        if customer_input is None:
            break
# Prints the customer order
        customer = {"name": "Live Customer", "cash": float("inf"), "products": [customer_input]}
        print("Customer order:")
        print_customer(customer)
        process_order(shop, customer)

# Running the shop simulation
shop = create_and_stock_shop()
print("Shop Inventory:")
print(f"Initial Cash: {shop['cash']}")
for product in shop["products"]:
    print_product(product)

# Prints customer order from the csv files
customer_files = ['customer.csv', 'customertest.csv', 'customertest2.csv']
for filename in customer_files:
    customer = read_customer(filename)
    print("\nCustomer Details:")
    print_customer(customer)
    process_order(shop, customer)

# Prints text to screen
print("\nEntering Live Mode:")
print("\nWelcome to my live shop")
print("\nI hope you enjoy your experience")
operate_live_mode(shop)
