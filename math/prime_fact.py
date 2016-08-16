import math

gMaxAllowed = 10000000000

'''
Get input for what to factor and validate the input - this is n.  Then, start dividing n by the smallest non-1 prime (2).
Store this new value in n if it divides evenly.  Continue dividing by 2 until we find a point where it no longer divides
evenly.  This will get rid of any multiples of 2.  Once we find this point, increment the factor until we find one where 
it does divide evenly.  Continue doing this until the factor is equal to n.
'''

while True: # do this until the user enters a valid input (or ctrl-c's out of the command prompt...)
	in_str = input("Enter a number, I'll find the prime factors ")
	try:
		n = int(in_str)
		if(n < gMaxAllowed): # don't go over a prespecified number or else it can take way too long (10 bil. is a good compromise)
			factors = []
			currentFactor = 2
			while True: # passivly do this, we'll break when done rather than having an end condition
				if(n == currentFactor):
					if currentFactor not in factors:
						factors.append(currentFactor)
					break
				else:
					quotient = int(n / currentFactor)
					remainder = n % currentFactor
					if(remainder == 0): # n divides evenly by the factor?
						n = quotient
						if currentFactor not in factors: # don't want duplicate values
							factors.append(currentFactor)
					else:
						currentFactor += 1 # if it doesn't divide evenly, increment by 1
			print(factors)
			break
		else:
			print("Please enter a number less than " + str(gMaxAllowed))
	except ValueError:
		print("Please only enter a positive integer")