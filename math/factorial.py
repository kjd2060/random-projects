import math

gMaxAllowed = 100

def factorial(n):
	if(n == 1):
		return 1
	else:
		return n * factorial(n-1)

while True:
	input_str = input("What should I compute the factorial of? ")
	try:
		n = int(input_str)
		if(n <= gMaxAllowed and n > 0):
			fact = factorial(n)
			print(fact)
			break
		else:
			print("Please enter a positive number no greater than" + str(gMaxAllowed) + "...gets large fast otherwise")
	except ValueError:
		print("Please only enter a positive number")
