import csv

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Shop:
    def __init__(self):
        self.cash = 0
        self.products = []

    def stock_shop(self, filename):
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            first_row = next(csv_reader)
            self.cash = float(first_row[0])
            for row in csv_reader:
                product = Product(row[0], float(row[1]), int(row[2]))
                self.products.append(product)

    def print_shop(self):
        print(f'INITIAL CASH: {self.cash}')
        for product in self.products:
            print(f'NAME: {product.name}, PRICE: {product.price}, QUANTITY: {product.quantity}')
    
    def process_order(self, customer):
        for customer_product in customer.products:
            for shop_product in self.products:
                if customer_product.name == shop_product.name:
                    if customer_product.quantity <= shop_product.quantity:
                        self.cash += customer_product.quantity * shop_product.price
                        shop_product.quantity -= customer_product.quantity
                        print(f"Order processed for {customer_product.name} quantity: {customer_product.quantity}")
                    else:
                        print(f"Not enough stock for {customer_product.name}")
                    
                    break
            else:
                print(f"Product {customer_product.name} not found in the shop")
    
        
        print(f"Remaining cash in the shop: {self.cash}")

class Customer:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.products = []

    def read_customer(self, filename):
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            first_row = next(csv_reader)
            self.name = first_row[0]
            self.cash = float(first_row[1])
            for row in csv_reader:
                product = Product(row[0], 0, int(row[1]))  # price is not needed for customers
                self.products.append(product)

    def print_customer(self):
        print(f'NAME: {self.name}, CASH: {self.cash}')
        for product in self.products:
            print(f'NAME: {product.name}, QUANTITY: {product.quantity}')


# Usage
shop = Shop()
shop.stock_shop('stock.csv')
shop.print_shop()

customer = Customer("", 0)
customer.read_customer('customer.csv')
customer.print_customer()

shop.process_order(customer)

customer1 = Customer("", 0)
customer1.read_customer('customertest.csv')
customer1.print_customer()

shop.process_order(customer1)

customer2 = Customer("", 0)
customer2.read_customer('customertest2.csv')
customer2.print_customer()

shop.process_order(customer2)


