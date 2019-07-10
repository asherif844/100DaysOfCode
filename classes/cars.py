class Car:
    runs = True

    def start(self, name):
        self.name = name
        if self.runs:
            print(f'{name} car is started')
        else:
            print(f'{name} car is broken. Oh no!')
