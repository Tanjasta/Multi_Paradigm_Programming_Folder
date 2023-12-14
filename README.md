# Multi_Paradigm_Programming_Folder
Multi_Paradigm_Programming_Folder
Description
This Python program simulates a basic shop operation. It processes orders by reading stock and customer data from CSV files. It also features a live mode for real-time order processing.
Requirements
* Python 3.x
* CSV files for stock (stock.csv) and customers (customer.csv, customertest.csv, customertest2.csv)
Usage
* 		Prepare CSV Files: Ensure stock.csv and customer CSV files are in the same directory as the script.
* 		Run the Script: Execute the script using Python.
* 		Live Mode: In live mode, input product names and quantities as prompted. Type 'exit' to end live mode.
Functions
create_and_stock_shop(filename='stock.csv')
Reads the stock.csv file to initialise the shop's inventory and cash.
* filename: Path to the stock CSV file.
read_customer(filename)
Reads a customer's data from a CSV file.
* filename: Path to the customer's CSV file.
print_product(product)
Prints details of a single product.
* product: A dictionary containing product details.
print_customer(customer)
Prints customer details, including their name, cash, and product list.
* customer: A dictionary containing customer information.
process_order(shop, customer)
Processes an order, updating shop inventory and cash based on the customer's order.
* shop: A dictionary representing the shop.
* customer: A dictionary representing the customer.
read_user_input()
Reads user input in live mode for product name and quantity.
operate_live_mode(shop)
Operates the shop in live mode, processing orders based on real-time user input.
* shop: A dictionary representing the shop.
