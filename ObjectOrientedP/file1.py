class CountingClicker:
    def __init__(self, count = 0):
        self.count = count

    def __repr__(self):
        return f"CountingClicker(count={self.count})"
    
    def click(self, num_times = 1):
        """Click the clicker some number of times"""
        self.count+=num_times
    def read(self):
        return self.count
    def reset(self):
        self.count = 0


clicker = CountingClicker()
assert clicker.read() == 2
clicker.click()
clicker.click()
clicker.read()
clicker.reset()
# clicker2 = CountingClicker(100)
# clicker3 = CountingClicker(count = 100)

class NoResetClicker(CountingClicker):
    def reset(self):
        pass

clicker2 = NoResetClicker()
assert clicker2.read() == 0
clicker2.click()
clicker2.click()
clicker2.read()
clicker2.reset()
clicker2.__repr__()
clicker2.__init__()