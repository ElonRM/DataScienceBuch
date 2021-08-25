class CountingClicker:
    """Eine Klasse sollte wie jede Funktion auch einen Dicstring haben"""

    def __init__(self, count=0):
        self.count = count

    def __repr__(self):
        return f"CountingClicker(count={self.count})"

    def click(self, num_times=1):
        """Den Zähler num_times mal drücken"""
        self.count += num_times

    def read(self):
        return self.count

    def reset(self):
        self.count = 0


clicker1 = CountingClicker()
clicker2 = CountingClicker(100)
clicker3 = CountingClicker(count=100)

clicker = CountingClicker()
assert clicker.read() == 0, "clicker should start with 0"
clicker.click()
clicker.click()
assert clicker.read() == 2, "brr"
clicker.reset()
assert clicker.read() == 0, "brr"


class NoResestClicker(CountingClicker):
    # Diese Klasse übernimmt alle Methoden der übergeordneten Klasse

    # Jedoch hat sie eine Reset Klasse, die nichts tut
    def reset(self):
        pass


clicker2 = NoResestClicker()
assert clicker2.read() == 0
clicker2.click()
clicker2.reset()
assert clicker2.read() == 2
