import csv

def create_and_stock_shop():
    shop = {}
    with open('stock.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        first_row = next(csv_reader)
        shop ["cash"] = float(first_row[0])
        shop["products"] = []
        for row in csv_reader:
            product ={}

            product["name"] = row[0]
            product["price"] = float(row[1])
            product["quantity"] = int(row[2])

            shop["products"].append(product)

    return shop

    
# First customer
def read_customer():
    customer = {}
    with open('customer.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        first_row = next(csv_reader)
        customer ["name"] = first_row[0]
        customer ["cash"] = float(first_row[1])
        customer["products"] = []
        for row in csv_reader:
            product ={}

            product["name"] = row[0]
            product["quantity"] = int(row[1])

            customer["products"].append(product)

    return customer



def print_product(product):
    print (f'NAME:{product["name"]}, PRICE:{product["price"]}, QUANTITY:{product["quantity"]}')
    

def print_customer(customer):
    print(f'NAME:{customer["name"]}, CASH:{customer["cash"]} ')
    for product in customer["products"]:
        print(f'NAME:{product["name"]}, QUANTITY:{product["quantity"]}')

def process_order(shop, customer):
    for product in customer["products"]:
        for shop_product in shop["products"]:
            if product["name"] == shop_product["name"]:
                if product["quantity"] <= shop_product["quantity"]:
                    shop["cash"] += product["quantity"] * shop_product["price"]
                    shop_product["quantity"] -= product["quantity"]
                    print(f"Order processed for {product['name']} quantity: {product['quantity']}")
                else:
                    print(f"Not enough stock for {product['name']}")
                break
            
        
    print(f"Remaining cash in the shop: {shop['cash']}")    
    
# Second customer
def read_customer1():
    customer1 = {}
    with open('customertest.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        first_row = next(csv_reader)
        customer ["name"] = first_row[0]
        customer ["cash"] = float(first_row[1])
        customer["products"] = []
        for row in csv_reader:
            product ={}

            product["name"] = row[0]
            product["quantity"] = int(row[1])

            customer["products"].append(product)

    return customer1

def print_product(product):
    print (f'NAME:{product["name"]}, PRICE:{product["price"]}, QUANTITY:{product["quantity"]}')

def print_customer1(customer1):
    print(f'NAME:{customer["name"]}, CASH:{customer["cash"]} ')
    for product in customer["products"]:
        print(f'NAME:{product["name"]}, QUANTITY:{product["quantity"]}')
   

def process_order(shop, customer1):
    for product in customer["products"]:
        for shop_product in shop["products"]:
            if product["name"] == shop_product["name"]:
                if product["quantity"] <= shop_product["quantity"]:
                    shop["cash"] += product["quantity"] * shop_product["price"]
                    shop_product["quantity"] -= product["quantity"]
                    print(f"Order processed for {product['name']} quantity: {product['quantity']}")
                else:
                    print(f"Not enough stock for {product['name']}")
                break
    print(f"Remaining cash in the shop: {shop['cash']}")  

# Third customer
def read_customer2():
    customer2 = {}
    with open('customertest2.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        first_row = next(csv_reader)
        customer ["name"] = first_row[0]
        customer ["cash"] = float(first_row[1])
        customer["products"] = []
        for row in csv_reader:
            product ={}

            product["name"] = row[0]
            product["quantity"] = int(row[1])

            customer["products"].append(product)

    return customer2

def print_product(product):
    print (f'NAME:{product["name"]}, PRICE:{product["price"]}, QUANTITY:{product["quantity"]}')

def print_customer2(customer2):
    print(f'NAME:{customer["name"]}, CASH:{customer["cash"]} ')
    for product in customer["products"]:
        print(f'NAME:{product["name"]}, QUANTITY:{product["quantity"]}')
   

def process_order(shop, customer2):
    for product in customer["products"]:
        for shop_product in shop["products"]:
            if product["name"] == shop_product["name"]:
                if product["quantity"] <= shop_product["quantity"]:
                    shop["cash"] += product["quantity"] * shop_product["price"]
                    shop_product["quantity"] -= product["quantity"]
                    print(f"Order processed for {product['name']} quantity: {product['quantity']}")
                else:
                    print(f"Not enough stock for {product['name']}")
                break
    print(f"Remaining cash in the shop: {shop['cash']}")  


def print_shop(shop):
    print(f'INITIAL CASH: {shop["cash"]}')
    for product in shop["products"]:
     print_product(product)
    

shop = create_and_stock_shop()
print_shop(shop)

customer = read_customer()
print_customer(customer)
process_order(shop, customer)


customer1 = read_customer1()
print_customer1(customer1)
process_order(shop, customer1)

customer2 = read_customer2()
print_customer2(customer2)
process_order(shop, customer2)