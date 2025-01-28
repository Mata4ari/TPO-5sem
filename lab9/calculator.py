class Calculator:
    def __init__(self, count=0):
        self.count = count

    def plus(self, x):
        self.count+=x
        return self

    def minus(self, x):
        self.count-=x
        return self



