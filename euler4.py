"""

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

num1 = num2 = 999

pals = []

while num1 > 0:
	num2 = 999
	while num2 > 0:
		ans = num1 * num2
		test = str(ans)
		if (test[::1] == test[::-1]):
			pals.append(ans)

		num2 -= 1
	num1 -= 1
		

print(max(pals))
