from servises.actions import get_cars, delete_car, search_car, edit_cars
from servises.add import add_car
from json_helper import read_json, save_json
from icecream import ic


cars = [{"Car number":222555, "Problems":5}]

def menu(cars):
     read_json()
     while True:
        ic("My Garaze")
        print("1 - Get all cars")
        print("2 - add car")
        print("3 - delete car")
        print("4 - edit car")
        print("5 - search car")
        print("6 - exit")
        choice = input("please enter command: ")
        if choice == "1":
            get_cars(cars)
        elif choice == "2":
            add_car(cars)
        elif choice == "3":
            delete_car(cars)
        elif choice == "4":
            edit_cars(cars)
        elif choice == "5":
            search_car(cars)
        elif choice == "6":
            exit()
        save_json(cars)

if __name__ == "__main__":
    menu(cars)