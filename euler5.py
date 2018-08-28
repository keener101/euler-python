'''

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''

def gcd(a,b):
	while b != 0:
		c = b
		b = a % b
		a = c
	return a

def lcm(a,b):
	return a * b / gcd(a,b)


def lmc_rec(a,b,n):
	if n==21:
		return a
	else:
		cur = a * b / gcd(a,b)
		return lmc_rec(cur, n+1, n+1)

print(lmc_rec(1,2,1))

#answer: 232792560








		





