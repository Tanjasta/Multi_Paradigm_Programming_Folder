# This imports a csv file.

import csv

# Product class representing each product whith its name, price and quantity.
class Product:
    def __init__(self, name, price=0.0, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
 # String representation of a product.
    def __str__(self):
        return f'NAME: {self.name}, PRICE: {self.price}, QUANTITY: {self.quantity}'

# Shop class representing the shop.
class Shop:
    def __init__(self, cash=0.0):
        self.cash = cash
        self.products = []
# Adding product to the shop.
    def add_product(self, product):
        self.products.append(product)
# Process a customer order.Checking if product is in stock and calculating total cost.
    def process_order(self, customer):
        total_cost = 0
        for c_product in customer.products:
            for s_product in self.products:
                if c_product.name == s_product.name:
                    if c_product.quantity <= s_product.quantity:
                        total_cost += c_product.quantity * s_product.price
                    else:
                        print(f"Not enough stock for {c_product.name}")
                    break

# Checking if customer has enough cash for the order. Updating shop inventory.
        if customer.cash >= total_cost:
            for c_product in customer.products:
                for s_product in self.products:
                    if c_product.name == s_product.name:
                        s_product.quantity -= c_product.quantity
                        print(f"Order processed for {c_product.name}, quantity: {c_product.quantity}")
                        break
            self.cash += total_cost
            print(f"Total cost: {total_cost}. Remaining cash in the shop: {self.cash}")
        else:
            print(f"Customer {customer.name} does not have enough cash. Order not processed.")

# String representation of the shop.
    def __str__(self):
        shop_str = "Shop Inventory\n"
        shop_str += f'Initial Cash: {self.cash}\n'
        shop_str += '\n'.join(str(product) for product in self.products)
        return shop_str

 # Customer class representing each customer.
class Customer:
    def __init__(self, name, cash=float('inf')):
        self.name = name
        self.cash = cash
        self.products = []

# Adding a product to the order.
    def add_product(self, product):
        self.products.append(product)

 # String representation of a customer.
    def __str__(self):
        customer_str = f'NAME: {self.name}, CASH: {self.cash}\n'
        customer_str += '\n'.join(f'NAME: {product.name}, QUANTITY: {product.quantity}' for product in self.products)
        return customer_str

# Loading data from CSV files.
def load_data(filename, is_shop=True):
    with open(filename) as file:
        csv_reader = csv.reader(file, delimiter=',')
        first_row = next(csv_reader)

# Creating shop or customer. 
        if is_shop:
            entity = Shop(cash=float(first_row[0]))
        else:
            entity = Customer(name=first_row[0], cash=float(first_row[1]))
# Adding product to the shop or customer.
        for row in csv_reader:
            name = row[0]
            if is_shop:
                price, quantity = float(row[1]), int(row[2])
                entity.add_product(Product(name, price, quantity))
            else:
                quantity = int(row[1])
                entity.add_product(Product(name, quantity=quantity))

    return entity

# Function that operates in live mode.
def operate_live_mode(shop):
    while True:
        product_name = input("Enter product name: ")
        if product_name.lower() == 'exit':
            break
        quantity = int(input("Enter quantity: "))
        live_customer = Customer("Live Customer")
        live_customer.add_product(Product(product_name, quantity=quantity))
        print("Customer order:")
        print(live_customer)
        shop.process_order(live_customer)

# Loading data and processing orders for customers from CSV files
shop = load_data('stock.csv', is_shop=True)
print(shop)

customer_filenames = ['customer.csv', 'customertest.csv', 'customertest2.csv']
for filename in customer_filenames:
    customer = load_data(filename, is_shop=False)
    print("\nCustomer Details:")
    print(customer)
    shop.process_order(customer)

# Prints text to screen
print("\nEntering Live Mode:")
print("\nWelcome to my live shop")
print("\nI hope you enjoy your experience")
operate_live_mode(shop)
