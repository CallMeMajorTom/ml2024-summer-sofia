class NumberList:
    def __init__(self):
        self.numbers = []

    def insert(self, num):
        self.numbers.append(num)

    def search(self, x):
        for i, num in enumerate(self.numbers, 1):
            if num == x:
                return i
        return -1
