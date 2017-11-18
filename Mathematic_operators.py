#prompt user to enter two numbers
num1, num2 = input('Enter 2 Number: ').split()

#convert string to integer
num1 = int(num1)
num2 = int(num2)

#Sum
Sum = (num1 + num2)

#Difference
difference = (num1 - num2)

#Multiplication
product = (num1 * num2)

#Division
quotient= (num1 / num2)

#modulus
reminder = (num1 % num2)

print("{} + {} = {}".format(num1, num2, Sum))
print("{} + {} = {}".format(num1, num2, difference))
print("{} + {} = {}".format(num1, num2, product))
print("{} + {} = {}".format(num1, num2, quotient))
print("{} + {} = {}".format(num1, num2, reminder))


   # Example - converting miles to kilometers

#prompt user to enter a digit
miles = input('Enter Miles: ')

#converts strings to integer
miles= int(miles)

#calculate miles to kilometers
Kilometers = miles * 1.60934

print("{} miles equals to {} kilometers".format(miles, Kilometers))

