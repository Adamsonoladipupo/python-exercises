print("Welcome! This app help you calculate your investment return after nth year with 7% rate")
amount = int(input("Enter the invested amount: "))
number_of_years = int(input("Enter number of years: "))

investment_return = amount*(1 + 0.07)**number_of_years
print("Your investment return after ", number_of_years, "years is $",investment_return)

