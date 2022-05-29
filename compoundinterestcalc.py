p = 10000.0 # Principle
n = 12  # number of times the interset rate is compounded per year
r = 0.08  # interest rate
t = 0.0    # number of years money will be compounded for


t = int(input("Please enter the number of years the money will be compounded for "))
final_amount = 10000*(1 + r/n)**(n*t)
print(final_amount)