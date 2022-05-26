################ Built-in string functions + Methods #############

# length function counts like humans do - from 1
greet = 'hellloooo'
print(len('hellloooooooo')) 
print(greet[:])
print(greet[0:len(greet)])

###### String Methods ###############
## methods start with a . 

quote = 'to be or not to be'
print(quote.upper())
print(quote.capitalize())

# finds first occurence of be -- element 3 in strng
print(quote.find('be')) 

# replace - replaces be with me
print(quote.replace('be', 'me'))

# we see when we print quote out it has not changed -  # 
# strings are immutable.
# we can overwrite them if we want but we don'nt change them.
# we can create them or destroy them. 
# when we do the quote.replace it creats a new string.
# Now we are not assigning this new string to anything, so
# eventaulley it will be removed from memory.

print(quote)

# but if we do something like this
quote2 = quote.replace('be', 'me')
# a new string is created and assigned to quote2
print(quote2)