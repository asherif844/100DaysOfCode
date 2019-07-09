from collections import OrderedDict

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    jeep = cars['Jeep']
    return jeep


def get_first_model_each_manufacturer(cars=cars):
    first_model = []
    for k, v in cars.items():
        value1 = v[0]
        first_model.append(value1)

    return first_model


def get_all_matching_models(cars=cars, grep='TRAIL'):
    all_cars = []
    for key, value in cars.items():
        for v in value:
            v = v.lower()
            grep = grep.lower()
            if grep in v:
                all_cars.append(v.capitalize())
    return all_cars


# print([value for (key, value) in sorted(cars.items())])
# print('----------')
# print([key for (key, value) in sorted(cars.items())])


def sort_car_models(cars=cars):
    for i, j in sorted(cars.items()):
        print(i, sorted(j))


print(sort_car_models())

# for k in sorted(cars.keys()):
#     print(k)
# print('------------')
# for v in sorted(cars.values()):
#     print(v)
# print('------------')
# for i in sorted(cars.items()):
#     print(i)
# print('------------')
# for i, j in sorted(cars.items()):
#     print(i, sorted(j))
