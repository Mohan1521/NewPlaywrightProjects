# it = 4
# while it:
#     print(it)
#     it = it-1
#     print('this is a loop')
#
# print('***************')
# it = 5
# while it>1:
#     print(it)
#     it = it-1
#     print('this is a loop')
#
# print('using if ***************')
# it = 5
# while it>1:
#     if it>4:
#         print(it)
#         it = it-1
#         print('this is a if loop')

# print('using if to break ***************')
# it = 5
# while it>1:
#     if it==3:
#         print(it)
#         break
#     print(it)
#     it = it-1
#     print('this is a if loop')

it =10
while it > 1:
    if it == 9:
        it = it-1
        continue
    if it == 4:
        break
    print(it)
    it = it-1
    print('this is a if loop')




# name = "Mohan"
# reverseds_text = reversed(name)
# print("ReverseString:", reverseds_text)