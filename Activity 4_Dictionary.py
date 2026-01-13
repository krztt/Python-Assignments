
gadgets = {}

def load_gadgets():
    try:
        with open("gadgets.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                name, gadget_type, price, brand = line.strip().split(", ")
                gadgets[name] = {
                    "type": gadget_type,
                    "price": price,
                    "brand": brand
                }
    except FileNotFoundError:
        print("No gadget available\n")

def save_gadgets():
    with open("gadgets.txt", "w") as file:
        for name, details in gadgets.items():
            file.write(f"{name}, {details['type']}, {details['price']}, {details['brand']}\n")
    print("Gadgets saved successfully!\n")

def add_new_gadget():

    name = input("Enter gadget name: ")
    gadget_type = input("Enter gadget type (e.g., phone, laptop, tablet): ")
    price = input("Enter gadget price: ")
    brand = input("Enter gadget brand: ")

    gadgets[name] = {
        "type": gadget_type,
        "price": price,
        "brand": brand
    }
    print(f"{name} added successfully!\n")
    save_gadgets()

def get_gadget_detail():

    name = input("Enter the gadget name to get details: ")
    if name in gadgets:
        print(f"{name}: {gadgets[name]}\n")
    else:
        print("Gadget not found!\n")

def display_all_gadgets():
    ###Display gadgets
    if not gadgets:
        print("No gadgets available.\n")
    else:
        print("All Gadgets:")
        for name, details in gadgets.items():
            print(f"{name}: {details}")
        print()

def search_gadget_by_type():

    gadget_type = input("Enter the gadget type to search for (e.g., phone, laptop, tablet): ")
    found = {name: details for name, details in gadgets.items() if details["type"] == gadget_type}

    if found:
        print(f"Gadgets of type '{gadget_type}':")
        for name, details in found.items():
            print(f"{name}: {details}")
    else:
        print(f"No gadgets found for type '{gadget_type}'.")
    print()

def main():
    global gadgets
    load_gadgets()
    """Main function to display the menu and handle user input."""
    while True:
        print("\nGadget Management System")
        print("1. Add a new gadget")
        print("2. Get gadget details")
        print("3. Display all gadgets")
        print("4. Search gadgets by type")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_new_gadget()
        elif choice == "2":
            get_gadget_detail()
        elif choice == "3":
            display_all_gadgets()
        elif choice == "4":
            search_gadget_by_type()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")


if __name__ == "__main__":
    main()

