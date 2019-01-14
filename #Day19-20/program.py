from time import sleep
import itertools
import random

colors = 'red green yellow'.split()

rotation = itertools.cycle(colors)

# for i in rotation:
#     print(i)


def random_time():
    return random.randint(3, 7)


def light_rotation(rotation):
    for color in rotation:
        if color == 'yellow':
            print('Caution, the light is {} color'.format(color))
            sleep(random_time())
        elif color == 'red':
            print('Stop, the light is {} color'.format(color))
            sleep(random_time())
        else:
            print('Go, the light is {} color'.format(color))
            sleep(random_time())


if __name__ == '__main__':
    light_rotation(rotation)
