print(type("hi"))
username = 'supercoder'
password = 'supersecret'

long_string = '''
WOW
0 0
---
'''

print(long_string)

first_name = 'Andrei'
last_name = 'Neagoie'
full_name = first_name + ' ' + last_name

print(full_name)

# string concatenation
print('hello' + 'Andrei')


# Type conversion - converting 100 into type string
print(type(str(100)))
#
a = str(100) # converts 100 to string and assign to a
b = int(a)   # converts string a back to int
c = type(b)  # display type of b (back to type int )
print(c)

print(type(int(str(100))))

######### Escape sequences #####################

# lets python know whatever comes after \ is a string
weather = "It\'s \"kind of\" sunny"
print(weather)
# if we want an actual backlash - use 2 \\
print("Directory = c:\\windows")
# if we want a tab
print("\t <---- a tab was created with \\t")
# To create a newline in a string
print("Hope you have a good day\nThankyou you too")

############# Formatted Strings - f strings ####

# we want to display this with formatted strings
name = 'Mark'
age = 35
# This way is a little cumbersome
print('hi ' + name + ' you are ' + str(age) + ' years old')

# we add an f to the beginning of the string to make it a #formatted string. We then wrap in braces the variables we 
# want to print
print(f'hi {name}. You are {age} years old')

# there is also the format method
print('hi {}. You are {} years old'.format('Johnny', '55'))
# we can also do it this way
print('hi {}. You are {} years old'.format(name, age))
# What if we want a specific order ?
print('hi {1}. You are {0} years old'.format(name, age))
#finally we can just create our own variables if we want to
print('hi {new_name}. You are {age} years old'.format(new_name='sally', age = 100))

############# string indexes #######################
# strings in memory are stored as an ordered sequence of characters. Imagine 01234567 is the start (0) and end (7) memory location for string 'me me me'

selfish = 'me me me'
        #  ||||||||
        #  01234567  
print(selfish[0])
print(selfish[7])
 # Imagine computer saying ok Iam going to grab from the   
 # bookshelf index of 0 all the way to 7
print(selfish)

# [start:stop] this is called string slicing
selfish = '01234567'
print(selfish[0:2]) # start at zero and end when get to 2

print(selfish[0:7]) # start at 0 and end when get to 7

# get the full string
print(selfish[0:8])

# stepover - stepover says hey start here and here and then stepover a few things. so the default is one because wwe are going one by #one. [0:8:1] but if we add 2 it steps over by 2

print(selfish[0:8:2])

print(selfish[0:])#start at zero and the default is go to end

print(selfish[:5])#start at default zero and go to 5

# starts at default 0 goes to default end and stepsover by 1
print(selfish[::1])

# what if we do [-1]?
print(selfish[-1]) # negative index means start at the end

# a neat trick we can do here 
print(selfish[::-1]) # reverse the order
# skip by 2
print(selfish[::-2])

############# Immutability ###########################
# Strings in python are immutable - They cannot be changed
# what do we mean by that. Now that we have applied this string to selfish - '01234567' we can say:
selfish = 100
print(selfish)
selfish = '01234567'
# but if we try:
selfish[0] = '8'
print(selfish)
# we get an error saying 'str' object does not support item # assignment - This is because strings are immutable. That is we cannot #change the value of the string once it is
# created. The only way we can change it is to completey reassign the value. so that in memory python removes all 
# of the string '01234567' from memory and then just 
# assigns 8.
# if we do this :
selfish = selfish + '8'
# the whole string was recreated and the previous one does 
# not exist
