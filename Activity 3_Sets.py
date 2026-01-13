import os

class Favorite:
    def __init__(self):
        self.file_name = "food.txt"
        self.food = []
        self.drink = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_name):
            file = open(self.file_name, "r")
            self.food = file.read().splitlines()
            file.close()

    def save_tasks(self):
        file = open(self.file_name, "w")
        for food in self.food:
            file.write(food + "\n")
        file.close()

    def add_favorite_food(self, food):
        self.food.append(food)
        self.save_tasks()
        print('food added' , food)

    def add_favorite_drink(self, drink):
        self.drink.append(drink)
        self.save_tasks()
        print('drink added' , drink)

    def view_all_favorite_food(self):
        if len(self.food) == 0:
            print("No food in the list.")
        else:
            print("\nYour favorite foods:")
            for i in range(len(self.food)):
                print(str(i + 1) + ". " + self.food[i])

    def view_all_favorite_drink(self):
        if len(self.drink) == 0:
            print("No drink in the list.")
        else:
            print("\nYour favorite drink:")
            for i in range(len(self.drink)):
                print(str(i + 1) + ". " + self.drink[i])

    def delete_drink(self, drink_number):
        if drink_number >= 1 and drink_number <= len(self.drink):
            removed_drink = self.drink.pop(drink_number -1)
            self.save_tasks()
            print('you deleted:', removed_drink)
        elif drink_number == 'all':
            self.drink.clear()
            print('you deleted all drinks')

        else:
            print('invalid drink choice')

    def delete_food(self, food_number):
        if food_number >= 1 and food_number <= len(self.food):
            removed_food = self.food.pop(food_number -1)
            self.save_tasks()
            print('you deleted:', removed_food)
        elif food_number == 'all':
            self.food.clear()
            print('you deleted all foods')
        else:
            print('invalid food choice')

    def view_all(self):

        print('\nYour favorite food:')
        for i in range(len(self.food)):
            print(str(i + 1) , ". " , self.food[i])


        print('\nYour favorite drink:')
        for i in range(len(self.drink)):
            print(str(i + 1) , ". ", self.drink[i])

    def view_unique_food(self):
        unique_food = set(self.food)
        print('\nYour unique favorite Foods:')
        for i, food in enumerate(unique_food, start=1):
            print(f"{i}. {food}")
    def view_unique_drink(self):
        unique_drink = set(self.drink)
        print('\nYour unique favorite drink:')
        for i, drink in enumerate(unique_drink, start=1):
            print(f"{i}. {drink}")



    def menu(self):
        while True:
            print("\nFavorite food and drinks in Rinconada Area")
            print("1. Add favorite food")
            print("2. Add favorite drinks")
            print("3. view all favorite food")
            print("4. view all favorite drink")
            print("5. View unique favorite foods")
            print("6. View unique favorite drink")
            print("7. Remove Favorite food")
            print("8. Remove Favorite drink")
            print("9. View all favorites")

            print("10. Exit")

            choice = input("Enter your choice (1-10): ")
            if choice == "1":
                food = input("Enter the food: ")
                self.add_favorite_food(food)
            elif choice == "2":
                drink = input("Enter the drink: ")
                self.add_favorite_drink(drink)
            elif choice == "3":
                self.view_all_favorite_food()
            elif choice == "4":
                self.view_all_favorite_drink()
            elif choice == "7":
                food_number = input("Enter the food number to delete: ")
                if food_number.isdigit():
                    self.delete_food(int(food_number))

                else:
                    print("Please enter a valid number.")
            elif choice == "8":
                drink_number = input("Enter the drink number to delete: ")
                if drink_number.isdigit():
                    self.delete_drink(int(drink_number))
                else:
                    print("Please enter a valid number.")
            elif choice == "9":
                self.view_all()
            elif choice == "5":
                self.view_unique_food()

            elif choice == "6":
                self.view_unique_drink()


            elif choice == "10":
                print("Exiting the app. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = Favorite()
    app.menu()