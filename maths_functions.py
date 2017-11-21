import math

#Access methods by referencing the module
print("ceil(4.5) = ", math.ceil(4.5))
print("floor(4.4) = ", math.floor(4.4))
print("fabs(-4.4) = ", math.fabs(-4.4))

# factorial = 1*2*3*4
print("factorial(4) = ", math.factorial(4))

#return remainder of division 
print("fmod(5,4) = ", math.fmod(5,4))

#receiving a float and returning an int
print("trunc(4.2) = ", math.trunc(4.2))

#return x^y (power)
print("pow(2,2) = ", math.pow(2,2))

#return the square root
print("sqrt(4) = ", math.sqrt(4))

#special values
print("math.e = ", math.e)
print("math.pi = ", math.pi)

#return e^x
print("exp(4) = ", math.exp(4))

#return the natural logarithm e * e * e ~= 20 so log(20) tells
#you that e^3 ~= 20
print("log(20) = ", math.log(20))

#you can define the base of 10^3 + 1000
print("log(1000,10) = ", math.log(1000, 10))

#You can also use base 10 like this
print("log10(1000) = ", math.log10(1000))

#Convert radian to degree and vice versa
print("degrees(1.5708) = ", math.degrees(1.5708))
print("radians(90) = ", math.radians(90))
