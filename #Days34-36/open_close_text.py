# f = open('text', 'w')
# f.write('hello+\n')
# f.close()


routines = 'chest+biceps back+triceps core legs shoulders'.split()
timings = '45 45 30 55 45'.split()

workout_times = dict(zip(routines, timings))

# print(workout_times)

max_routines = None
max_timings = 0

for routine, timing in workout_times.items():
    timing = int(timing)
    if timing > max_timings:
        max_timings = timing
        max_routines = routine

print(max_routines, max_timings)
