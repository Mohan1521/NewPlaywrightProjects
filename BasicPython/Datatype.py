#1. Numeric  2. String 3. List 4. Tuple

#String
a = "hi"
b = "Good Morning"
print(a,b)
print(type(a))
print(type(b))
# we can concatenate with same datatype but not in different datatype

#List
#List is [] bracket
print("*******************************")
Values = [1, 2, "hello", 5.9 ]
print(Values)
print(type(Values))
print(Values[0])
print(Values[3])
print(Values[-1])
print(Values[1:3])
Values.insert(1,"world")
print(Values)
Values.append("hii")
print(Values)
Values.remove("hello")
print(Values)
Values[2] = "Morning"
print(Values)


#Tuples,   tuple is () bracket
print("Tuple************************************")
Tuples = (1, 2, "hello", 5.9 )
print(Tuples)
print(type(Tuples))
print(Tuples[0])
print(type(Tuples[1]))
# same as List datatype but immutable


