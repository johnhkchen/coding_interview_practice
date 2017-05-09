def main():
        print(sum(amicableNumbers(range(1, 10000+1))))

def amicableNumbers(span):
        divisors = dict(map(lambda n: (n, sumDivisors(n)), span))
        return filter(lambda n: isAmicable(n, divisors), span)

def sumDivisors(n):
        return sum(filter(lambda i: (n%i == 0), range(1,n)))

def isAmicable(x, divisors):
        return x == sumDivisors(divisors[x]) and not x == divisors[x]

main() 