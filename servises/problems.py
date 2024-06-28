def menu_problems():

    total_price = 0

    while True:
        print("My problem")
        print("1 - Engine - 2,000 NIS")
        print("2 - Breaks - 1,000 NIS")
        print("3 - 5000 km treatment - 500 NIS")
        print("4 - 10,000 km treatment - 1000 NIS")
        print("5 - Filters + Oil - 250 NIS")
        print("6 - Gear - 1000 NIS")
        print("7 - Price quote")
        print("0 - exit")
        choice = input("please enter the car problem:")
        if choice == "1":
            total_price += 2000
        elif choice == "2":
            total_price += 1000
        elif choice == "3":
            total_price += 500
        elif choice == "4":
            total_price += 1000
        elif choice == "5":
            total_price += 250
        elif choice == "6":
            total_price += 1000
        elif choice == "7":
            print(f"Total price quote: {total_price} NIS")
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 7.")

    print("Final total cost:", total_price)
    return total_price

# total_cost = menu_problems()
