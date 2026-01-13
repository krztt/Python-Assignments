###list methods###

grades = [ '96', '97', '98', '99']
# append

print("this list uses append method:")
grades.append('75')
print(grades)

#clear

print('this list uses clear method ')
grades.clear()
print(grades)

grades = [ '96', '97', '98', '99']
#copy
print('this list uses copy method')
grades2= grades.copy()
print(grades2)

#count
print('this is the count of a value')
x = grades.count('99')
print('number of student/s that recieve a 99 grades are:', x )

#extend 
print('this uses extend method')
grades.extend(grades2)
print(grades)

grades = [ '96', '97', '98', '99']

#index
print('this method finds the location of a number in a list:')
x = grades.index('98')
print('the grade 98 is located at', x )



#insert
print('this list uses the insert method')
grades.insert(2, "98")
print(grades)

#pop 
print('this list uses the pop method')
grades.pop(2)
print(grades)

#remove
print('this list uses the remove method')
grades.remove("96")
print(grades)

#reverse
print('this list uses the reverse method')
grades.reverse()
print(grades)

#sort
print('this list uses the sort method')
grades.sort()
print(grades)

###LIST PROGRAM###
import os

class Groceries:
    def __init__(self):
        self.file_name = "groceries.txt"
        self.grocery = []
        self.load_task()

    def load_task(self):
        if os.path.exists(self.file_name):
            file = open(self.file_name, "r")
            self.grocery = file.read().splitlines()
            file.close()
    def save_tasks(self):
        file = open(self.file_name, "w")
        for grocery in self.grocery:
            file.write(grocery + "\n")
        file.close()
    def add_grocery(self, grocery):
        self.grocery.append(grocery)
        self.save_tasks()
        print('grocery added', grocery)

    def view_grocery_list(self):
        if len(self.grocery) == 0:
            print('you have no list')
        else:
            print('your grocery list:')
            for i in range(len(self.grocery)):
                print(str(i + 1) + '. ' + self.grocery[i])

    def delete_grocery(self, grocery_number):
        if grocery_number >= 1 and grocery_number <= len(self.grocery):
            removed_grocery = self.grocery.pop(grocery_number -1)
            self.save_tasks()
            print('you deleted:', grocery_number)
        elif grocery_number == 'all':
            self.grocery.clear()
            print('you deleted all list')

        else:
            print('invalid grocery choice')
    def view_all(self):

        print('\nYour grocery list:')
        for i in range(len(self.grocery)):
            print(str(i + 1) , ". " , self.grocery[i])

    def menu(self):
        while True:
            print("\ngrocery list program")
            print("1. Add to the grocery list")
            print("2. delete a grocery list")
            print("3. view your grocery list")

            choice = input("Enter your choice(1-3): ")

            if choice == "1":
                grocery = input("enter a grocery: ")
                self.add_grocery(grocery)
            elif choice == "2":
                grocery_number = input("enter the grocery number you want to delete: ")
                if grocery_number.isdigit():
                    self.delete_grocery(int(grocery_number))
                else:
                    print("Please enter a valid number.")
            elif choice == "3":
                self.view_grocery_list()

if __name__ == "__main__":
    app = Groceries()
    app.menu()