def welcome_screen():
    print("Welcome to Arnold's Amazing Eats!")
    print("------------------------------------")
    print("The program is designed to inform about the ordering process for delicious food delivery in Waterloo.")
    print("You can place your order by contacting our staff member via call or text.")
    print("We promise you to bring the best meals delivered right to your door.")
    print("Thank you for choosing Arnold's Amazing Eats!")
    print("-------------------------------------------------\n")

# Call the welcome_screen function
welcome_screen()

def studentconfirmation():
    student_status = ""
    while student_status.lower() not in ["y", "n"]:
        student_status = input("Are you a student? (Y/N): ")
        if student_status.lower() not in ["y", "n"]:
            print("Invalid input. Please enter 'Y' or 'N'.")
        
    if student_status.lower() == "y":
        print("A student discount of 10% is applied on your purchase.")
        return 0.10
    else:
        return 0

# Define the function for customer details
def customerdetails():
    first_name = input("Please Enter your first name:")
    last_name = input("Please Enter your last name:")
    street_number = input("Please Enter the street number:")
    street_name = input("Please Enter the street name:")
    unit = input("Please Enter your unit number(if applicable):")
    city = input("Please Enter your city:")
    province = input("Please Enter your province:")
    postal_code = input("Please Enter postal code:")
    delivery_instructions = input("Please provide any special deliveries instructions (if possible):")
    phone_no = input("Please enter your phone number:")
    return {
        "first_name": first_name,
        "last_name": last_name,
        "street_number": street_number,
        "street_name": street_name,
        "unit": unit,
        "city": city,
        "province": province,
        "postal_code": postal_code,
        "delivery_instructions": delivery_instructions,
        "phone_no": phone_no
    }

def calculate_total_cost_with_hst(totalcost_after_discount):
    # Applying HST (Harmonized Sales Tax)
    hst_percentage = 0.13
    totalcost_with_hst = totalcost_after_discount * (1 + hst_percentage)
    return totalcost_with_hst

def order_dinner(customer_info):
    # Prompt for user to pick which of the two dinner items they want to purchase
    print("\nPlease select a dinner item:")
    print("1. Chicken Momo $6")
    print("2. Veg Burger $5")

    # User picks the meal they wish to purchase
    select_item = input("\nEnter the meal you wish to buy for the dinner (1 or 2): ")

    # Validate user input
    while select_item not in ["1", "2"]:
        print("Invalid input. Please select either 1 or 2.")
        select_item = input("\nEnter the meal you wish to buy for the dinner (1 or 2): ")

    # Inform them about what dinner did they choose
    if select_item == "1":
        meals_ordered = input("How many Chicken Momos would you like to purchase?: ")
        print("You have selected", meals_ordered, "Chicken Momos for your dinner")
        item_price = 6
        
    elif select_item == "2":
        meals_ordered = input("How many Veg Burgers would you like to purchase?: ")
        print("You have selected", meals_ordered, "Veg Burger for your dinner")
        item_price = 5

    # Confirmation
    confirmation = ""
    while confirmation.lower() not in ["y", "n"]:
        confirmation = input("Is this order correct? (Y/N): ")
        if confirmation.lower() not in ["y", "n"]:
            print("Invalid input. Please enter 'Y' or 'N': ")
    #if user confirms order incorrect then restart the process again
    if confirmation.lower() == "n":
        print("\n*******\n\nPlease go through the ordering process again to make any necessary changes...")
        order_dinner(customer_info)
        return

    # Display confirmation message
    print("Your order has been confirmed. Thank you for choosing Arnold's Amazing Eats!")

    discount_percentage = studentconfirmation()
    totalcost_before_discount = item_price * int(meals_ordered)
    totalcost_after_discount = totalcost_before_discount * (1 - discount_percentage)
    #applying HST
    totalcost_with_hst = calculate_total_cost_with_hst(totalcost_after_discount)
    
    # Print receipt
    print("\nReceipt:")
    print("\nCustomer Information:")
    print("Name:", customer_info["first_name"] + " " + customer_info["last_name"])
    print("Address:", customer_info["street_number"] + " " + customer_info["street_name"] + " " + customer_info["unit"])
    print("City, Province, Postal Code:", customer_info["city"] + ", " + customer_info["province"] + ", " + customer_info["postal_code"])
    print("Delivery Instructions:", customer_info["delivery_instructions"])
    print()  # Add a blank line
    
    # Print ordered items
    print("Order".ljust(20) + "Item".ljust(15) + "Item".ljust(15))
    print(" ".ljust(20) + "Amt".ljust(15) + "Price".ljust(15) + "Total".ljust(15))
    print("-" * 10 + "          " + "-" * 4 + "           " + "-" * 5 + "          " + "-" * 6)

    if select_item == "1":
        print("Chicken Momos:".ljust(20) + meals_ordered.ljust(15) + str(meals_ordered).ljust(15) + f"${totalcost_before_discount:.2f}".ljust(15))
    elif select_item == "2":
        print("Veg Burgers:".ljust(20) + meals_ordered.ljust(15) + str(meals_ordered).ljust(15) + f"${totalcost_before_discount:.2f}".ljust(15))

    # Calculate student savings
    student_savings = totalcost_before_discount * discount_percentage
    subtotal = totalcost_before_discount - student_savings
    tax_amount = subtotal * 0.13
    total_cost_with_hst = subtotal + tax_amount

    # Print discounts and total cost information
    print("\n" + "10% student savings".ljust(50) + f"-${student_savings:.2f}".ljust(15))
    print("Sub Total".rjust(40) + "          "+f"${subtotal:.2f}".ljust(20))
    print("Tax (13%)".rjust(40) + "          "+ f"${tax_amount:.2f}".ljust(20))
    print(" " * 10 + "          " + " " * 4 + "           " + " " * 5 + "          " + "-" * 6)
    print("TOTAL".rjust(40)  + "          "+f"${total_cost_with_hst:.2f}".ljust(20))

# Call the function to start the ordering process
customer_info = customerdetails()
order_dinner(customer_info)
