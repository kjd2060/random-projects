import math

'''
I'll have one function to get input since each one is basically the same thing; a positive float.  A better way to do it would be to have width and
height ask for feet and inches (and have the ability to switch to metric) and go by that, but this is fine for a 'first draft' implementation.
'''

def get_positive_float(inputString, askingFor):
	while True:
		in_string = input(str(inputString))
		try:
			cost = float(in_string)
			if(cost < 0):
				print("Please enter a positive number for " + str(askingFor))
			else:
				return cost
		except ValueError:
			print("Please only a positive number for " + str(askingFor))

while True:
	cost = get_positive_float("What's the cost in $ per sq ft? ", "cost")
	width = get_positive_float("What's the width? ", "width")
	height = get_positive_float("What's the height? ", "height")
	area = width * height
	total_cost = area * cost
	waste_factor = .05 # waste factor is averaged at 5% normally, sometimes it's higher sometimes lower but we'll use this as an average
	total_cost_with_waste = (total_cost * waste_factor) + total_cost
	print("It would cost a total of $" + str(total_cost) + " for a floor of " + \
		str(width) + "x" + str(height) + " at $" + str(cost) + " per sq ft.\nWith waste factor" + \
		" of " + str((waste_factor * 100)) + "%, cost goes to $" + str(total_cost_with_waste))
	break