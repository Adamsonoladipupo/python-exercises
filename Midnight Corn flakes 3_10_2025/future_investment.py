def future_investment(P, R, T):

	future_investment_value = P * (1 + R) ** T
	return future_investment_value


docstring = """
	This is a future investment app that
	helps you calculate your investment value. 

	where:	P = investment amount
		R = Annual rate (%)
		T = Time in terms of years(annum)

"""
print(docstring)

investment_amount = int(input("Enter P: "))
yearly_interest_rate = int(input("Enter R: ")) / 100
year = int(input("Enter T: "))

my_interest_value = future_investment(investment_amount, yearly_interest_rate, year)

print("Your future investment value is: $", my_interest_value)