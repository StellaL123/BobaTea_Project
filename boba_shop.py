# Make our own boba tea shop
menu = {
    "Black Sugar Boba Tea" : 3.50,
    "Taro Boba Tea" : 4.00,
    "Thai Milk Tea" : 3.75,
    "Regular Bubble Tea" : 3.00
}

# Shopowner Functions
    # 1. Add item to the menu
    # 2. Delete item from the menu
    # 3. Update item on the menu (price, name)

# def add_item(menu, item, value):
#     if type(item) == "int" or type(item) == "float":
#         print("What you have entered for item is not a word!")
#     elif type(value) == "str":
#         print("What you have entered for price is not a number!")
#     else:
#         item = str(item)
#         item = item.title() # reformat values
#         value = int(value) # reformat values
#         menu[item] = value
#     return menu

def delete_item(menu):
    print("This is all of the tea in our current menu: ")
    for tea in menu:
        print(tea)
    y_or_n = input("Do you want to delete anything from the menu? (Please answer yes or no): ")
    while y_or_n.upper() == "YES":
        deleted_tea = input("Which boba tea would you like to take off from the menu?: ").title()
        if deleted_tea in menu:
            del menu[deleted_tea]
        else:
            print(deleted_tea + " is not on our menu.")
        y_or_n = input("Do you want to take anything else off the menu? (Please answer yes or no): ")
    if y_or_n.upper() == "NO":
        print("OK! We won't delete anything.")
    else:
        print("You have not entered yes or no. Please answer the question again!")
        return delete_item(menu)
    return menu

def add_item(menu):
    print("This is our current menu: ")
    for tea in menu:
        print(tea)
    y_or_n = input("Do you want to add anything to the current menu? (Please answer yes or no): ")
    if y_or_n.upper() == "YES":
        added_tea = input("What would like to add?: ").title()
        new_price = input("What will be the price of " + added_tea + "?: ")
        if type(added_tea) == int or type(added_tea) == float: #I don't think we need the ""
            print("What you have entered for item is not a word!")
        elif type(new_price) == str:
            print("What you have entered for price is not a number!")
            answer = input("Do you want to re-enter?(Please answer yes or no): ")
            if answer.upper() == "YES":
                return add_item(menu)
            elif answer.upper() == "NO":
                print("OK!")
            else:
                print("I am lowkey disappointed... You did not enter yes or no.")
        else:
            if added_tea in menu:
                print("What you have entered is already in the menu")
            else:
                menu[added_tea.title()] = float(new_price)
                print("OK! We have added " + added_tea + " to the menu." )
                more = input("Do you want to add anything else? (Please enter yes or no): ")
                while more.upper() == "YES":
                    added_tea = input("What would like to add?: ")
                    new_price = input("What will be the price of " + added_tea + "?: ")
                    if type(added_tea) == 'int' or type(added_tea) == 'float':
                        print("What you have entered for item is not a word!")
                    elif type(new_price) == "str":
                        print("What you have entered for price is not a number!")
                    else:
                        if added_tea in menu:
                            print("What you have entered is already in the menu")
                        else:
                            menu[added_tea.title()] = float(new_price)
                            print("OK! We have added " + added_tea + "to the menu." )
                            more = input("Do you want to add more? (Please answer yes or no): ")
    elif y_or_n.upper() == "NO":
        print("OK! We will not add anything to the menu")
    else:
        print("You have not entered yes or no. Please answer the question again!")
        return add_item(menu)
    return menu

def update_item(menu):
    print("This is our current menu: ")
    print(menu)
    y_or_n = input("Do you want to update the price for certain items on our current menu? (Please answer yes or no): ")
    if y_or_n.upper() == "YES":
        tea = input("Which tea?: ").title()
        new_price = input("What is the new price of " + tea + "?: ")
        if type(tea) == int or type(tea) == float:
            print("What you have entered for the name of the tea is not a word!")
        elif type(new_price) == str:
            print("What you have entered for price is not a number!")
        elif tea.title() not in menu:
            print("What you have entered is not on the menu!")
        else:
            menu[tea.title()] = float(new_price)
    elif y_or_n.upper() == "NO":
        print("OK! We won't change the prices.")
        return menu
    else:
        print("You have not entered yes or no. Please answer the question again!")
        return update_item(menu)
    return(menu)

# Customer Functions
    # 1. Order drinks (variable amount of drinks)
    # 2. Function to calculate discounts for the total order

# No limit on number of parameters
def order_now(menu):
    order_list = []
    print("This is our current menu: ")
    print(menu)
    order = input("What would you like to order?(One drink at a time): ").title()
    if order not in menu:
            print("What you have ordered is not on the menu!")
            y_or_n = input("Do you want to re-order?(Please answer yes or no): ")
            if y_or_n.upper() == "YES":
                print("OK! We will show you the menu again.")
                return order_now(menu) #Why does this not work
            elif y_or_n.upper() == "NO":
                print("OK! Hope you have a nice day :)")
                exit()
            else:
                print("You have entered yes or no. We will just show you the menu again just in case")
                return order_now(menu)
    order_list.append(order)
    price = menu[order]
    more = input("Do you want anything else? 30% off if you buy 3 or more boba tea and 15% for 2 boba tea (Please answer yes or no): ")
    while more.upper() == "YES":
        new_order = input("What would you like to order?(One drink at a time): ")
        if new_order not in menu:
            print("What you have ordered is not on the menu!")
            y_or_n = input("Do you want to re-order?(Please answer yes or no): ")
            if y_or_n.upper() == "YES":
                print("OK! We will show you the menu again.")
                return order_now(menu)
            elif y_or_n.upper() == "NO":
                print("OK!")
            else:
                print("Sorry, I don't quite get that. You did not enter yes or no.")
        if new_order in menu:
            order_list.append(new_order)
            price += menu[new_order]
            more = input("Do you want anything else?(Please answer yes or no): ")
    number_of_drinks = 0
    for items in order_list:
        number_of_drinks += 1
    if number_of_drinks >= 3:
        total_price = price * 0.7
    elif number_of_drinks == 2:
        total_price = price * 0.85
    else:
        total_price = price
    print("OK, here's your order:")
    for item in order_list:
        print(item)
    print("and the total price is " + str(total_price))
    return menu, number_of_drinks, price, total_price

# def price(number_)
# def buy_items(*argv):
#     for item in argv:
#         print(menu[item]) # printing prices of menu items

# buy_items("Black sugar boba tea (M)", "Black sugar boba tea (L)")
# buy_items(1, 2)
# buy_items()
def main():
    print("Shopowner perspective")
    delete_item(menu)
    add_item(menu)
    update_item(menu)
    print("Customer perspective")
    order_now(menu)

main()
