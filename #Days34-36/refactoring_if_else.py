# refactoring

workouts = {
    'Monday': 'Chest+biceps',
    'Tuesday': 'Back+triceps',
    'Wednesday': 'Core',
    'Thursday': 'Legs',
    'Friday': 'Shoulders',
    'Saturday': 'Rest',
    'Sunday': 'Rest',
}

days = 'Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split()
routines = 'Chest+biceps Back+triceps Core Legs Shoulders Rest Rest'.split()

workouts2 = dict(zip(days, routines))

# print(workouts2)


def get_a_workout(day):
    routine = workouts2.get(day)
    if routine is None:
        return 'Error: This is not a day'
    else:
        return routine


print(get_a_workout('Saturdays'))
