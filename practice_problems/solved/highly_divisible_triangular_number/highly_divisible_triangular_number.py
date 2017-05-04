# Question: What is the value of the first triangle number to have over five hundred possible divisors?

from math import sqrt

def countDivisors(number):
        isDivisor = lambda x: (number % x == 0)
        quotientOf = lambda divisor: int(number / divisor)

        potentialDivisors = range(1,int(sqrt(number))+1)
        divisors = set(filter(isDivisor, potentialDivisors))
        quotients = set(map(quotientOf, divisors))

        divisors = divisors.union(quotients)

        return len(divisors)

minimumDivisors = 500

currentTriangleNumber = 0;
nextNumberToAdd = 1

while countDivisors(currentTriangleNumber) < minimumDivisors:
        currentTriangleNumber += nextNumberToAdd
        nextNumberToAdd += 1

print("{} has {} divisors.".format(currentTriangleNumber, countDivisors(currentTriangleNumber)))