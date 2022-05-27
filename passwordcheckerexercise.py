### Exercise Password Checker ###

user_name = input("Please enter your username ")
password = input("please enter your passord ")

password_len = len(password)
hidden_password = '*' * password_len
print(password_len)


print(f'{user_name} you password {hidden_password} is {password_len} letters long')
