############## Type conversion #######################

## input converts the inputed year to a string
birth_year = input('what year where you born?') 

# int will convert the string birth_year into an integer
# so that we can subtract it from 2022

your_age = 2022 - int(birth_year) 
print(f'your age is: {your_age}')