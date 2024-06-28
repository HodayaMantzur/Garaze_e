
from servises.problems import menu_problems


def add_car(cars):
    new_num_car = int(input("Enter number car: "))
    menu_problems()
    fix_choice = input("Would you like to fix the car? (yes/no): ").lower()
    if fix_choice == "yes":
        total_cost = menu_problems()
        print(f"Total cost for car {new_num_car}: {total_cost} NIS")
        print(f"Adding car {new_num_car} to the list.")
    elif fix_choice == "no":
        print(f"Car {new_num_car} added without fixing.")
    else:
        print("Invalid input. Car not added.")