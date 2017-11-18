
#prompt user to enter digits
num1, operator, num2 = input('Enter calculation : ')

#convert string to integer
num1 = int(num1)
num2 = int(num2)

#if + then provide output based on addiction
if operator == "+":
	print("{} + {} = {}".format(num1, num2, num1+num2))

elif operator == "-":
	print("{} - {} = {}".format(num1, num2, num1-num2))

elif operator == "*":
	print("{} * {} = {}".format(num1, num2, num1*num2))

elif operator == "/":
	print("{} / {} = {}".format(num1, num2, num1/num2))

elif operator == "%":
	print("{} % {} = {}".format(num1, num2, num1%num2))

else:
	print('Math error')