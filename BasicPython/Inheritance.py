class Calculator:
    pass


class ChildImpl(Calculator):
    num3 = 100
    def __init__(self):
        Calculator.__init__(self)   #child constructor used for pass the arguments

    def calc(self):
        return self.num3

obj = ChildImpl()
print(obj.num3)
obj.calc()