"""

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""

import math

vals = list(range(1,1000))

vals_sq = list(map(lambda x: x**2, vals))

for sq1 in vals_sq:
	for sq2 in vals_sq:
		check = sq1+sq2
		if check in vals_sq:
			#print("{} and {}".format(sq1, sq2))
			addends = [math.sqrt(sq1), math.sqrt(sq2), math.sqrt(check)]

			if sum(addends) == 1000:
				print(addends)
				print(addends[0]*addends[1]*addends[2])
				

#[200.0, 375.0, 425.0]


			

