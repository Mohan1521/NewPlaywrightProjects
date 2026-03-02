str = 'RahulShettyAcademy.com'
str1 = 'Consulting firm'
str2 = 'Rahul Shetty'

print(str)
print(str + str1)   #concatenation
print(str + str1 + str2)

print(str[1])       #a
print(str[0:5])      #want substring in python
print(str2 in str)   #substring check

var = str.split(".")
print(var)
print(var[0])

str3 = ' Hello World '
print(str3.strip())
print(str3.lstrip())
print(str3.rstrip())