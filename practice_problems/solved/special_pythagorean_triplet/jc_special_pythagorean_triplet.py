# Special Pythagorean triplet
# Problem 9 
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Check if c is a square of a whole number
# We could write an algorithm for this, but c's upper bound is fairly low - at most sqrt(1000) = 50 or so
# let's just memoize 1 to 50's squares
perfectSquares = []
for x in range(1,1000):
  perfectSquares.append(x**2)

# Write a helper function to find if value is a perfect square

def isPerfectSquare(value, perfectSquares):
  try:
    return perfectSquares.index(value)+1
  except ValueError:
    return -1

def findMagicTriplet():
  for b in range(1,1000):
    for a in range(1,b):
      c = isPerfectSquare(a*a + b*b, perfectSquares);
      if c > -1 and a+b+c == 1000:
        print("a: {}, b: {}, c: {} is the magic pythagorean triplet. Their product is {}.".format(a,b,c,a*b*c))
        return

findMagicTriplet()