from cars import cars
from collections import defaultdict


def main():
    print(get_all_jeeps(cars))
    print(first_car(cars))
    print(name_contains_str(cars))
    sort_cars(cars)


def get_all_jeeps(file):
    jeeps = file['Jeep']
    return jeeps


def first_car(file):
    f_cars = []
    for manufacturer, car in file.items():
        f_cars.append(car[0])
    return f_cars


def name_contains_str(file):
    selected_cars = []
    for cars in file.values():
        for car in cars:
            if 'Trail' in car:
                selected_cars.append(car)
    return selected_cars


def sort_cars(file):
    new_dict = defaultdict(list)
    for maker, s_cars in file.items():
        new_dict[maker] = sorted(s_cars)
    print(new_dict)


if __name__ == '__main__':
    main()

# challenges
# Get all Jeeps
# Get the first car of every manufacturer.
# Get all vehicles containing the string Trail in their names (should work for other grep too)
# Sort the models (values) alphabetically
