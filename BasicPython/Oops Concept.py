#Class are user defined blueprint or prototype.
#Class will have methods, class variables, instance variable, Constructor etc...

class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num1 - num2

obj = Calculator()
obj.add(1, 2)
print(obj.add(1, 2))
obj.sub(4, 5)
print(obj.sub(4, 5))
print('Example 1********************')

class Calculator:
    num = 10
    #default Constructor
    def __init__(self):
        print('hello world')
    def add(self, num1, num2):
        print(num1 + num2)
obj=Calculator()
obj.add(1, 2)
print(obj.num)
print('Example 2********************')

class Calculator:
    num = 100
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self, num1, num2):
        print(num1 + num2)
    def Summation(self):
        return self.a + self.b + self.num

obj=Calculator(5., 6)
obj.add(1, 2)
print(obj.Summation())
print('Example 2********************')




















