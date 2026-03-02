#conditions
from enum import unique

marks = 70
if marks >= 90:
    print("a grade")
elif marks >= 60:
    print("B grade")
else:
    print("C grade")

#function
def GreetMe(name):
    print(name)
GreetMe("mohan")

#lambda
square = lambda x, y: x*y
print(square(3, 5))


#class
class bike:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def display(self):
        return self.name, self.price
obj = bike("mohan", 100)
obj.display()

#reverse
text = "Hello"
print(text[::-1])

#length number
num = [1, 2, 3]
print(len(num))

nums = [1, 1, 2, 2, 2, 3]
unique = list(set(nums))
print(unique)

#swap two number
a, b = 10, 20
a, b = b, a
print(a, b)

#largest numbers
numbers = [10, 25, 3, 45, 9]
largest = max(numbers)
print(largest)


s = "AABBCC"
result = "".join(dict.fromkeys(s))
print(result)

ss = "AABBCC"
unique = list(set(ss))
print(unique)

age = 20
if age >= 28:
    print("elder")
elif age >= 25:
    print("minor")
else:
    print("major")

for i in range(5):
    print(i)

count = 6
while count >= 5:
    print(count)
    count -= 4
    for i in range (3):
        print(i)

count = 1
while count <= 3:
    print(count)
    count += 1

    for i in range(5):
     if i == 3:
        break


name = "mohan"
print(type(name))


def add(a, b):
    print(a + b)

add(2, 4)
# print(add(2, 4))

var = [1, 2, 3]
print(var)
var.append(4)
print(var)
var.extend([5, 6])
print(var)

a, b = 10, 15
a, b = b, a
print(a, b)

text = "Python"
reversed_text = text[::-1]
print("Reversed String:",reversed_text)

text = "madam"
if text == text[::-1]:
    print(f"{text} is palidrom")
else:
    print(f"{text} is not palidrom")

num = [10, 20, 30, 40, 50]
largest = max(num)
print(largest)

num = 7
if num  == 2:
    print("even")
else:
    print("odd")

lst = [1,2,3,2,4,1]
print(set(lst))
