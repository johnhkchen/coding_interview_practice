# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# Forethought: This one seems incredibly easy. I wonder what the gotcha is? Lets try to do this in very few lines
sumOfSquares = 0;
for x in range(100+1):
  sumOfSquares += pow(x,2)

squareOfSums = pow(sum(range(100+1)),2)

print("Squares: {}, Square of Sums: {}, Difference: {}".format(sumOfSquares, squareOfSums, squareOfSums - sumOfSquares))


# Nope, that was it. Super easy.