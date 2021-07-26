# name = "Ali Neaz"
# print(name)
# print(type(name))  # class str type string
# greeting = "Good Morning"
# c = greeting+" "+name
# print(c)
name = "Ali Neaz"
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[0:3])
# print(name[10])  # invalid cause lenth is 8 and it exceds 8
# print(name[0:10])
# print(len(name))
# name[4] = "A"  # cant be done this not changeable
# print(name)
# _______________until the lenth the [] doesnot includ the last value
# print(name[0:3])  # will pring 0 1 2 indeces
# print(name[-1])
# print(name[-6])  # index -5 is white space
# print(name[-8])


print(name[-1:-2])  # not working or garage wrong method
print(name[:8])  # first index will automatically be 0 though i havent specified
print(name[0:])  # first is specified last will be then lenth


c = name[-4:-1]  # is same as name[4:7]
print(c)

# _____________________slicing valu with skip value _____________________
name = "Ali Neaz"
# ______012345678
d = name[0:8:2]  # printing every second indeces
print(d)
d = name[0::2]
e = name[0::3]
print(d)
print(e)
