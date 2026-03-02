file = open('test.txt')
# print(file.read())    # read all the lines
# print(file.read(5))       # read 5 letters only
# print(file.readline())   #read single line
# print(file.readline())
# file.close()

#print the line by line using readline method
# line = file.readline()
# while line!='':
#     print(line)
#     line = file.readline()
# file.close()

# for line in file.readlines():
#     print(line)



# Read the content from the file
# with open('test.txt', 'r') as reader:
#     obj = reader.read()
#
# # Write the same content back (or modify if needed)
# with open('test.txt', 'w') as writer:
#     writer.write(obj)


# Read the content from the file
# with open('test.txt', 'r') as reader:
#     content = reader.read()
#
# # Reverse the content
# reversed_content = content[::-1]
#
# # Write the reversed text back to the same file
# with open('test.txt', 'w') as writer:
#     writer.write(reversed_content)





with open('test.txt', 'r') as reader:
    content = reader.read()

with open('test.txt', 'w') as writer:
    writer.write(content[::-1])


