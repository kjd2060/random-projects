import math

while True:
	max_num_str = input("How far into the sequence should I go? ")
	try:
		max_num = int(max_num_str)
		n = 1
		index = 0
		previous = 0
		ar = []
		ar.append(n)
		while True:
			if(index < max_num or max_num == n):
				temp = n
				n = n + previous # next = current + previous, or Fn+1 = Fn + Fn-1 or Fn = Fn-1 + Fn-2
				previous = temp
				index += 1
				ar.append(n)
			else:
				for num in ar:
					print("{:d}, ".format(num), end="")
				print("Done!")
				break
		break
	except ValueError:
		print("Please only enter a positive whole number")