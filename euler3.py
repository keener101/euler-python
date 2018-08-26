"""

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

start = 600851475143

test = 2

largest = None

while start != 1:
	if (start % test == 0):
		largest = test;
		start = start / test;
		test = 2;
	else:
		test += 1

print(largest)

#answer: 6857


