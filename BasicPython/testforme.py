# def simpleint(principal, time, rate):
#     si = (principal * time * rate) / 100
#     return si
#
# def compint(principal, time, rate):
#     ci = principal * ((1 + rate / 100) ** time - 1)
#     return ci
#
#
# principal = float(input("Enter principal: "))
# time = float(input("Enter time: "))
# rate = float(input("Enter rate: "))
#
# si = simpleint(principal, time, rate)
# ci = compint(principal, time, rate)
#
# print("Simple interest is %8.2f" % si)
# print("Compound interest is %8.2f" % ci)
#
# diffint = si - ci
# print("Difference is %8.2f" % diffint)
import collections
from multiprocessing.reduction import duplicate

from pygments.util import duplicates_removed

from BasicPython.mytest import reversed_text, count

# name = "Mohan"
# reverseds_text = "".join(reversed(name))
# print("ReverseString:", reverseds_text)
#
#
# name = "Mohan"
# reversed_text = (name[::-1])
# print(reversed_text)

name = "Mohan"
arr = list(name)
arr.reverse()
print("".join(arr))


list = [1, 2, 3]
list.reverse()
print(list)

name = "madam"
if name == "madam":
    print("palidrome")
else:
    ("not palidrome")

s = "banana"
freq = collections.Counter(s)
print(freq)

lst = [1, 2, 3, 2, 4, 1]
name = duplicates_removed(lst)
print(name)

lst = [1, 2, 3, 2, 4, 1]
unique = set(lst)
print(unique)

a, b = 0, 1
for i in range(5):
    a, b = b, a + b
print(a, b)

num = 7
if num%2 == 0:
    print("even")
elif num%2 == 1:
    print("odd")

user = [1, 3, 4, 5]
for i in user:
    if i % 2 == 0:
        print("add")
    else:
        print("even")

s = "python is easy"
words = s.split()
print(len(words))


l1 = [1, 2, 3]
l2 = [2, 3, 4]
common = set(l1) & set(l2)
print(common)

arr = [1, 3, 5, 6]
full_Set = set(range(arr[0], arr[1]+1))
print(full_Set)


add = lambda x, y: x + y
print(add(1, 2))


text = "Hello World"
print(text.split())
print("".join(text.split()))

nums = [1,2,2,3,3,4]
unique = set(nums)
print(unique)


n = "aabbcc"
# remove = duplicates_removed(n)
# print(remove)


result = "".join(dict.fromkeys(n))
print(result)

user = [1, 2, 3, 4, 5]
for i in user:
    if i % 2 == 0:
        print("even")
    else:
        print("odd")

test = "hello"
reversed_text = test[::-1]
print(reversed_text)

text = "Hello World"
print(text.split())
print("".join(['Hello', 'World']))


arr = [1, 2, 3, 5, 6]

n = len(arr) + 1  # since one number is missing
expected_sum = n * (n + 1) // 2
actual_sum = sum(arr)

missing = expected_sum - actual_sum
print(missing)


list = [1, 2, 2, 3]
unique = set(list)
print(unique)

text = "AABBCC"
result = "".join(dict.fromkeys(text))
print(result)

nums = [1, 2, 3]
print(2 in nums)

n = 10
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

list = [1, 2, 3, 4, 5]
for item in list:
    if item % 2 == 0:
        print(f"{item} is even")
    else:
        print(f"{item} is odd")

arr = [1, 2, 3, 5, 6]
n = len(arr) + 1
expected_sum = n * (n + 1) // 2
actual_sum = sum(arr)
missing = expected_sum - actual_sum
print(f"The missing number is: {missing}")


n = 10
a, b = 0, 1
for i in range(n):
    print(a, end="")
    a, b = b, a + b