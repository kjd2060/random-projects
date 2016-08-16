import math, textwrap

gMaxAllowed = 150

while True:
	max_num_str = input("How far into the sequence should I go? ")
	try:
		max_num = int(max_num_str)
		if(max_num <= gMaxAllowed and max_num >= 0):
			n = 1
			index = 0
			previous = 0
			ar = []
			ar.append(n)
			while True:
				if(index < max_num and max_num != n):
					temp = n
					n = n + previous # next = current + previous, or Fn+1 = Fn + Fn-1 or Fn = Fn-1 + Fn-2
					previous = temp
					index += 1
					ar.append(n)
				else:
					num_str = ""
					for num in ar:
						num_str += str(num)
						num_str += ", "
					print(textwrap.fill(num_str, 75), end="")
					print(" Done!")
					break
			break
		else:
			print("Please input a number between 0-" + str(gMaxAllowed))

	except ValueError:
		print("Please only enter a positive whole number")
	
