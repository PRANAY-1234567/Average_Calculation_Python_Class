class Numbers:
    def __init__(self):
        self.n1 = 14
        self.n2 = 62
        self.n3 = 53

    def average(self):
        a = (self.n1 + self.n2 + self.n3) / 3.0
        print("Average :", a)


# Main program (same as Constructor1)
obj = Numbers()
obj.average()