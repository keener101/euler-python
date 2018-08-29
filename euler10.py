"""

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""


#using the nth prime (n) upper range estimate:
# n * log(n*log(n)) = 2000001, finds n = 139,673.25
# therefore, finding the first 139,673 primes should include those up to
# 2 million and not much more

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

prime_list = nth_prime(139673)

primes_filtered = list(filter(lambda x: x <2000000, prime_list))

print(sum(primes_filtered))

#answer: 142913828922