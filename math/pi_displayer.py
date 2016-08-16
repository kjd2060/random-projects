import math

gMaxDigitsAllowed = 49

'''
I'll use string formatting to do this.
'''
while True:
	digitsStr = input("How many digits to display? ")
	try:
		digits = int(digitsStr)
		if((digits > 0) and (digits < gMaxDigitsAllowed)): # don't go above where we're accurate to
			lengthString = "{0:." + str(digits) + "f}" # combine the string formatting with the num of digits we want
			print(lengthString.format(math.pi))
			break
		elif(digits > gMaxDigitsAllowed - 1):
			print("Not accurate out to that many digits; here's the most we can guarantee")
			temp = "{0:." + str(gMaxDigitsAllowed-1) + "f}"
			print(temp.format(math.pi))
		else:
			print("Please enter a non negative number")
	except ValueError:
		print("Not a valid number! Please only enter whole, positive numbers")
