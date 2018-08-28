"""

The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

"""

vals = list(range(1,101))

sums = sum(vals)

vals_sq = list(map(lambda x: x**2, vals))

sq_sums = sum(vals_sq)

print(sums**2 - sq_sums)

#answer: 25164150