"""

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""
import math

def nth_prime(n):
	max = int(n * math.log(n*math.log(n)))
	vals = [True] * max
	primes = []

	vals[0] = False
	vals[1] = False

	for (index, flag) in enumerate(vals):
		if flag:
			primes.append(index)
			for num in range(index, max, index):
				vals[num] = False 


	return primes

tenkand1 = (nth_prime(10001))

print(tenkand1[10000])

#answer 104743





