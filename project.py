# Mini Project Week 2

# Initialize lists to store products and orders
products = ["anime", "manga", "coke"]
orders = []

print("\nWelcome to the store.｡･ﾟﾟ･(＞_＜)･ﾟﾟ･｡.python is cool...")

def print_main_menu():
    print("\n~Main menu~")
    print("1. Products menu")
    print("2. Orders menu")
    print("0. Exit\n")

# Function to print the product menu options
def print_product_menu():
    print("\n~~Product Menu~")
    print("1. View products")
    print("2. Add product")
    print("3. Update product")
    print("4. Delete product")
    print("0. Return to main menu")
    print("")

# Function to print the order menu options
def print_order_menu():
    print("~Order Menu~")
    print("1. View orders")
    print("2. Add order")
    print("3. Update order status")
    print("4. Update order")
    print("5. Delete order")
    print("0. Return to main menu")

# Main function to run the application
    while True:
        print_main_menu()
        main_menu_choice = int(input("Enter your choice: "))

        if main_menu_choice == 0:
            break

        elif main_menu_choice == 1:
            while True:
                print_product_menu()
                product_menu_choice = int(input("Enter your choice: "))

                if product_menu_choice == 0:
                    break
                elif product_menu_choice == 1:
                    print("\nProducts List:")
                    for product in products:
                        print(product)
                elif product_menu_choice == 2:
                    new_product_name = input("Enter product name: ")
                    products.append(new_product_name)
                    print(f"Product '{new_product_name}' added.")
                    print("\nNew product list:")
                    for product in products:
                        print(product)
                elif product_menu_choice == 3:
                    print("Products List:")
                    for index, product in enumerate(products):
                        print(f"{index + 1}: {product}")
                    product_index = int(input("Enter product index to update: "))
                    new_product_name = input("Enter new product name: ")
                    products[product_index] = new_product_name
                    print("Product updated.")
                elif product_menu_choice == 4:
                    print("Products List:")
                    for index, product in enumerate(products):
                        print(f"{index}: {product}")
                    product_index = int(input("Enter product index to delete: "))
                    products.pop(product_index)
                    print("Product deleted.")

        elif main_menu_choice == 2:
            while True:
                print_order_menu()
                order_menu_choice = int(input("Enter your choice: "))

                if order_menu_choice == 0:
                    break
                elif order_menu_choice == 1:
                    print("Orders List:")
                    for order in orders:
                        print(order)
                elif order_menu_choice == 2:
                    customer_name = input("Enter customer name: ")
                    customer_address = input("Enter customer address: ")
                    customer_phone = input("Enter customer phone number: ")
                    order = {
                        "customer_name": customer_name,
                        "customer_address": customer_address,
                        "customer_phone": customer_phone,
                        "status": "preparing"
                    }
                    orders.append(order)
                    print("Order added.")
                elif order_menu_choice == 3:
                    print("Orders List:")
                    for index, order in enumerate(orders):
                        print(f"{index}: {order}")
                    order_index = int(input("Enter order index to update status: "))
                    print("Order Status List:")
                    print("0: preparing")
                    print("1: shipped")
                    print("2: delivered")
                    status_index = int(input("Enter updated status: "))
                    status_list = ["preparing", "shipped", "delivered"]
                    orders[order_index]["status"] = status_list[status_index]
                    print("Order status updated.")
                elif order_menu_choice == 4:
                    print("Orders List:")
                    for index, order in enumerate(orders):
                        print(f"{index}: {order}")
                    order_index = int(input("Enter order index to update: "))
                    for key in orders[order_index]:
                        new_value = input(f"Enter new value for {key} (leave blank to keep current value): ")
                        if new_value:
                            orders[order_index][key] = new_value
                    print("Order updated.")
                elif order_menu_choice == 5:
                    print("Orders List:")
                    for index, order in enumerate(orders):
                        print(f"{index}: {order}")
                    order_index = int(input("Enter order index to delete: "))
                    orders.pop(order_index)
                    print("Order deleted.")