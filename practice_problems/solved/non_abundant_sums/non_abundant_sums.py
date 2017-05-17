from math import sqrt

maxValue = 28123+1

def main():
    print(sum(nonAbundantSums()))

def nonAbundantSums():
    abundantSums = getAbundantSums()
    return [i for i in range(1,maxValue) if i not in abundantSums]

def getAbundantSums():
    abundantNums = findAbundantNumbers()
    abundantSums = dict()
    for i in range(len(abundantNums)):
        for j in range(i, len(abundantNums)):
            abundantSum = abundantNums[i]+abundantNums[j]
            if abundantSum < maxValue:
                abundantSums[abundantSum] = True
            else:
                break
    return abundantSums

def findAbundantNumbers():
    return [i for i in range(1,maxValue) if sum(divisorsOf(i)) > i]

def divisorsOf(n):
    lowerDivisors = set([i for i in range(1,int(sqrt(n)+1)) if n%i == 0])
    upperDivisors = [int(n/i) for i in lowerDivisors if not i == 1]
    return lowerDivisors.union(upperDivisors)

main()

#4179871