"""
File: weather_master.py
Name: 卓晉逸
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

EXIT = -100		# quit code


def main():
	"""
	This function will help us to know the max temperature, min temperature, and average temperature
	"""
	print('stanCode \"Weather Master 4.0\"!')
	t = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))		# the first ask
	sum = 0		# initial sum
	x = 0		# initial x (number of data)
	c = 0		# initial c (number of cold days)
	if t == EXIT:		# No data
		print('No Temperatures were entered.')
	else:
		x += 1		# number of data
		max = t		# initial max
		min = t		# initial min
		sum = sum + t		# calculate sum
		if t < 16:
			c += 1		# calculate c
		avg = sum / x		# calculate avg

		while True:
			t = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
			if t == EXIT:		# quit
				break
			else:
				x += 1		# number of data
				if t > max:		# pk max
					max = t
				if t < min:		# pk min
					min = t
				sum = sum + t		# calculate sum
				if t<16:
					c += 1		# calculate c
				avg = sum / x		# calculate avg
	if x != 0:
		print('Highest Temperature = ' + str(max))
		print('Lowest Temperature = ' + str(min))
		print('Average = ' + str(avg))
		print(str(c) + ' cold day(s)')






###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
