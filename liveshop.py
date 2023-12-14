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
    

def read_user_input():
    product_name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    return {"name": product_name, "quantity": quantity}

def operate_live_mode(shop):
    while True:
        customer_input = read_user_input()
        if customer_input["name"].lower() == "exit":
            break

        customer = {"name": "Live Customer", "cash": float("inf"), "products": [customer_input]}
        print("Customer order:")
        print_customer(customer)
        process_order(shop, customer)

def print_shop(shop):
    print(f'INITIAL CASH: {shop["cash"]}')
    for product in shop["products"]:
     print_product(product)
    

shop = create_and_stock_shop()
print_shop(shop)

operate_live_mode(shop)
