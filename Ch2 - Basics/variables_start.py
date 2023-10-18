# 
# Example file for variables
# LinkedIn Learning Python course by Joe Marini
#


# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries
myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2)
mydict = {"one" : 1, "two" : 2}

# print(myint)
# print(myfloat)
# print(mystr)
# print(mybool)
# print(mylist)
# print(mytuple)
# print(mydict)

# re-declaring a variable works
# myint = "abc"
# print(myint)

# to access a member of a sequence type, use []
# print(mylist[1])
# print(mytuple[2])
#print(mydict[1])

# use slices to get parts of a sequence
mylist = [0, 1, 'two', 3.2, 'iiii', False, '666666']
print(mylist)
print(mylist[1:5])
print(mylist[1:7:1])
print(mylist[1:7:2])
print(mylist[0:7:3])
print(mylist[1:7:3])


# you can use slices to reverse a sequence
print(mylist[::-1])

# dictionaries are accessed via keys

# ERROR: variables of different types cannot be combined

# Global vs. local variables in functions

