
from servises.add import add_car


def get_cars(cars):
    for car in cars:
        print(car)



def delete_car(cars):
    car_select = int(input("choose car number: "))
    cars.pop(car_select)
    return print("car deleted")


def search_car(cars):
    print("*search entered*")
    search = input("Please enter a car number or problem number to search:").lower()
    found = False
    for car in cars:
        if (
            search.lower() in str(car["Car number"]).lower()  
            or search.lower() in str(car["Problem"]).lower()):
            print(f"car:{car["Car number"]}. Problem:{car["Problem"]}.")
            found = True
    if not found:
       print("not found!")

def edit_cars(cars):
        # delete_car(cars)
        cars_to_edit = int(input("Please enter the car number in the array to edit: "))
        cars.pop(cars_to_edit)
        add_car(cars)