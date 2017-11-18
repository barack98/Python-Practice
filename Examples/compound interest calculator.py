# compound interest calculation
Investment = input('Enter your Investment: ')
Interest_rate = input('Enter your Interest_rate: ')

Investment = float(Investment)
Interest_rate = float(Interest_rate) * .01

for i in range(10):
	Investment = Investment + (Investment * Interest_rate)

print("Total Investment is: {:.2f}".format(Investment))

