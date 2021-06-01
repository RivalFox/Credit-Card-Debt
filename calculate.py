






def cal_monthly_interest(apr, statementBal):
	
	daily_interest_rate = apr / 365
	daily_interest = statementBal * daily_interest_rate
	monthly_interest = daily_interest * 31
	#print("Monthly Interest Charged: $" + str(monthly_interest))
	return monthly_interest


def how_long_are_you_paying(data):
	apr = float(data[0])
	bal = float(data[1])
	pymnt = float(data[2])

	#index = 0
	counter = 0
	
	while bal >= 0:
		#print(bal)
		monthly_int = cal_monthly_interest(apr,bal)
		bal = (bal + monthly_int) - pymnt
		
		counter += 1
	return counter