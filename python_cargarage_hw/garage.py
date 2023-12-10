from enum import Enum
import json
import os

cars = []

class Actions(Enum):
    PRINT = 1
    ADD = 2
    SEARCH = 3
    DELETE = 4
    EXIT = 5

my_data_file = "cars.json"

def main():
    load_data()
    os.system("clear")
    
    while True:
        user_input = menu()
        if user_input == Actions.EXIT:
            exit_fun()
        elif user_input == Actions.PRINT:
            print_cars()
        elif user_input == Actions.ADD:
            add()
        elif user_input == Actions.DELETE:
            dele()
        elif user_input == Actions.SEARCH:
            search()

def dele():
    license_plate = input("Enter the license plate of the car to delete: ")
    for car in cars:
        if "license" in car and car["license"] == license_plate:
            cars.remove(car)
            print(f"Car with license plate {license_plate} deleted.")
            return
    print(f"No car found with license plate {license_plate}.")

def search():
    license_plate = input("Enter the license plate of the car to search: ")
    for car in cars:
        if "license" in car and car["license"] == license_plate:
            print("Car found:")
            print_car_info(car)
            return
    print(f"No car found with license plate {license_plate}.")

def print_car_info(car):
    print(f"Model: {car.get('model')}")
    print(f"Color: {car.get('color')}")
    print(f"Brand: {car.get('brand')}")

def add():
    model = input("Please enter your car model: ")
    color = input("Please enter your car color: ")
    brand = input("Please enter your car brand: ")
    license_plate = input("Please enter your car license plate: ")

    cars.append({
        "model": model,
        "color": color,
        "brand": brand,
        "license": license_plate
    })

def print_cars():
    for car in cars:
        print_car_info(car)

def menu():
    for action in Actions:
        print(f'{action.value} - {action.name}')
    return Actions(int(input("Please enter your selection: ")))

def load_data():
    global cars
    try:
        with open(my_data_file, "r") as file:
            json_string = file.read()
            cars = json.loads(json_string)
    except:
        pass

def exit_fun():
    json_string = json.dumps(cars)
    with open(my_data_file, "w") as file:
        file.write(json_string)
    print("Goodbye.")
    exit()

if __name__ == "__main__":
    main()
