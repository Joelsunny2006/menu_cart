cart = {}
sum = 0
cafe_menu = {
    "Chai": 12,
    "Tea": 10,
    "Masala Chai": 20,
    "Filter Coffee": 30,
    "Samosa": 15,
    "Vada Pav": 25,
    "Paneer Sandwich": 50,
    "Masala Dosa": 60,
    "Idli": 30,
    "Medu Vada": 35,
    "Pav Bhaji": 80,
    "Aloo Paratha": 40,
    "Poha": 25,
    "Upma": 30,
    "Lassi": 40,
    "Jalebi": 20,
    "Gulab Jamun": 20,
    "Pani Puri": 30,
    "Bhel Puri": 25,
    "Chole Bhature": 70,
    "Veg Biryani": 100,
    "Paneer Tikka": 120,
    "Rasgulla": 15,
}

def display_cart():
    total_sum = 0
    if cart:
        print("\n----- YOUR CART -----")
        for item, quantity in cart.items():
            item_total = cafe_menu[item] * quantity
            print(f"{item} : {quantity} x ₹{cafe_menu[item]} = ₹{item_total}")
            total_sum += item_total
        print(f"\nYour Total Bill: ₹{total_sum}")
    else:
        print("Your cart is empty")

show = input("Would you like to see our menu? (Yes/No): ")
if show.lower() == 'yes':
    print("\n----- MENU -----")
    for item, price in cafe_menu.items():
        print(f"{item}: ₹{price}")

    while True:
        selection = input("\nPlease select an item from the menu (or type 'Done' to finish): ").title()
        if selection.lower() == "done":
            break
        elif selection in cafe_menu:
            if selection in cart:
                cart[selection] += 1
            else:
                cart[selection] = 1
            print(f"{selection} has been added to your cart.")
        else:
            print("Item not found in the menu. Please select a valid item.")

    display_cart()

    while True:
        option = input("\nEnter 'D' to delete an item from your cart\nEnter 'A' to add more items to your cart\nEnter 'OK' to proceed to checkout: ").upper()
        if option == 'D':
            delete_item = input("Please enter the item you want to delete: ").title()
            if delete_item in cart:
                if cart[delete_item] > 1:
                    cart[delete_item] -= 1
                    print(f"One {delete_item} has been removed from your cart. Remaining: {cart[delete_item]}")
                else:
                    cart.pop(delete_item)
                    print(f"{delete_item} has been removed from your cart.")
            else:
                print(f"{delete_item} is not in your cart.")
        elif option == 'A':
            add_item = input("Please enter the item you wish to add to your cart: ").title()
            if add_item in cafe_menu:
                if add_item in cart:
                    cart[add_item] += 1
                else:
                    cart[add_item] = 1
                print(f"{add_item} has been added to your cart.")
            else:
                print("Item not found in the menu. Please select a valid item.")
        elif option == 'OK':
            print("Thank you for your purchase 😊")
            break
        else:
            print("Invalid option. Please enter 'D', 'A', or 'OK'.")

    display_cart()
else:
    print("Thank you. Have a great day!")
