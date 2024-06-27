# a = "Wireless networking is interesting technology"
# b = 'Devnet is interesting technolgy too'
# c = """what about coding?...super fun!"""

# The values of a list are retrieved by referencing the index number : 
#1 
# vendors = ["Cisco", "Aruba", "mist", "meraki"]
# first= vendors[0]
# second = vendors[1]
# third = vendors [2]
# # print (first)

#2 
#Tuples are like lists, created by enclosing values in parentheses. 

# WLC = ("SJC1", "BLR1", "SF01")
# wlc1 = WLC [0]
# wlc2 = WLC [1]
# wlc3 = WLC [2]
# print(wlc3)

#3

#Some operations are common to all sequence types, such as returning an element by index. 

# a = 'wireless networking is interesting technology'
# b = a [1]
# c = a [0:3]
# print (c)
# d = len(a)
# print (d)

# 4
# There are also common functions that can be applied to sequence types by checking the number of elements
# and finding the min and max values among all elements. 

# b = [0,1,2,3,4]
# c = max(b)
# print(c)

# 4
# some more operations on elements 

# a = 'wireless is interesting technology'
# b = a.capitalize()
# print(b)
# c = a.upper()
# print(c)
# d = a.split()
# print (d)

# 5 - Dictionary
# The object in the dictionary value can also be another data type, such as list. As we have used
# square brackets for lists and round braces for tuples,
#  we use curly braces to create dictionary 

# wlc1 = {'AccessPoints1': ['AP1', 'AP2', 'AP3', 'AP4']}
# print(wlc1['AccessPoints1'])

# 6
# Sets 
#  A set is used to contain an unordered collection of objects. Sets are unordered and cannot 
#  be indexced by numbers. But there is one character that makes sets stand out.

# 6a
# a = "hello"
# # use the built-in funtion set() to convert the string to set. 
# b = set(a)
# print(b)

# 6b
# x = {1,2,3,4}
# x.add(5)
# # print(x)
# x.update(['a','a','b','b'])
# print(x)

############## Python Operators ######################################

# a = 1 + 2 # addition
# print(a) # addition

# a = 2 - 1  # substration
# print (a) # substration 

# a = 1 * 5 # multipication 
# print (a)

# a = 5/1 # division - returns float
# print(a)

# a = 5//2 # floor division
# print(a)

# a = 5%2 # modulo operator
# print(a)

################# Comparison Operators #####################################

# a = 1
# b = 2 
# if a == b:
#     print(True)
# else:
#     print(False)

# a = 1
# b = 2 
# print (a == b)
# print (a > b)
# print (a < b)
# print (a <= b)


################# Flow Control #####################################

# a = 10
# if a > 1:
#     print("a is larger than 1")
# elif a < 1:
#     print("a is smaller than 1")
# else:
#     print("a is equal to 1")


## While loop will continue to excute until condition is False, so be careful with this one, 
## if you dont want to continue to execute (and crash your process):

a = 10
b = 1 
while b < a:
    print(b)
    b+=1













