import math

gMaxDigitsAllowed = 49

'''
I'll use string formatting to do this.
'''
while True:
	digitsStr = input("How many digits to display? ")
	try:
		digits = int(digitsStr)
		if((digits > 0) and (digits < gMaxDigitsAllowed)): # we're only accurate to a trail of so many digits, so stop after that
			lengthString = "{0:." + str(digits) + "f}" # create the initial string object that we can attach the num to
			print(lengthString.format(math.e))
			break
		elif(digits > gMaxDigitsAllowed - 1):
			print("Not accurate out to that many digits; here's the most we can guarantee")
			temp = "{0:." + str(gMaxDigitsAllowed - 1) + "f}"
			print(temp.format(math.e))
		else:
			print("Please enter a non negative number")
	except ValueError:
		print("Not a valid number! Please only enter whole, positive numbers")
