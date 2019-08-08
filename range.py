import csv

f = open('clean.csv')
inf = csv.reader(f)
data = []
prices = []
new_prices = []
with open('clean.csv','rb') as f:
	reader = csv.reader(f)
	data = list(reader)

for i in range(0, len(data)):
	print(data[i][10])
	prices.append(int(data[i][10]))

for i in range(0, len(prices)):
	if(prices[i] < 100000):
		new_prices.append("0-100000")
	elif(prices[i] > 100000 and prices[i] < 124999):
		new_prices.append("100001 - 124999")	
	elif(prices[i] > 124999 and prices[i] < 149999):
		new_prices.append("125000-149999")
	elif(prices[i] > 150000 and prices[i] < 174999):
		new_prices.append("150000-175000")
	elif(prices[i] > 175000 and prices[i] < 199999):
		new_prices.append("175000-200000")
	elif(prices[i] > 199999 and prices[i] < 224999):
		new_prices.append("200000-224999")
	elif(prices[i] > 225000 and prices[i] < 249999):
		new_prices.append("22500-250000")
	elif(prices[i] > 250000 and prices[i] < 274999):
		new_prices.append("250000-275000")
	elif(prices[i] > 275000 and prices[i] < 299999):
		new_prices.append("275000-300000")
	else:
		new_prices.append("300000+")
	print("\"" + new_prices[i] +"\"")
