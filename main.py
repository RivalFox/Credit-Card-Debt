# Calculation for how much to pay on a credit card 
# Given the APR, the balance, and how much you are 
# paying how long will it take


def cal_monthly_interest(apr, statementBal):
	
	daily_interest_rate = apr / 365
	daily_interest = statementBal * daily_interest_rate
	monthly_interest = daily_interest * 31
	#print("Monthly Interest Charged: $" + str(monthly_interest))
	return monthly_interest


def how_long_are_you_paying(apr, bal, pymnt):
	#index = 0
	counter = 0
	
	while bal >= 0:
		print(bal)
		monthly_int = cal_monthly_interest(apr,bal)
		bal = (bal + monthly_int) - pymnt
		
		counter += 1
	return counter




def main():
	# .1999
	# 6453.28
	# 250


	print("What is the APR? ")
	apr = input("Enter here as (decimal): ")
	print("What is the balance on the Account? ")
	bal = input("Enter: ")
	print("What is the most you can pay?")
	monthly_pymnt = input("Enter: ")

	monthly_int = cal_monthly_interest(float(apr),float(bal))
	num_months = how_long_are_you_paying(float(apr),float(bal),float(monthly_pymnt))
	num_yrs = num_months / 12

	print(str(num_months) + " months left")
	print(str(num_yrs) + " years left")

	

if __name__ == "__main__":
    main()
