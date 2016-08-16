import math

while True:
	digitsStr = input("How many digits to display? ")
	try:
		digits = int(digitsStr)
		if((digits > 0) and (digits < 49)):
			lengthString = "{0:." + str(digits) + "f}"
			print(lengthString.format(math.pi))
			break
		elif(digits > 48):
			print("Not accurate out to that many digits; here's the most we can guarantee")
			print("{0:.48f}".format(math.pi))
		else:
			print("Please enter a non negative number")
	except ValueError:
		print("Not a valid number! Please only enter whole, positive numbers")