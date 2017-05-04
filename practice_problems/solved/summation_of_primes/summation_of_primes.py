import timeit
startTime = timeit.default_timer()

upperBound = 2000000

# Eratosthene's Sieve
def findPrimes():
        global upperBound
        isPrime = [True for numbers in range(upperBound+1)]
        isPrime[0] = isPrime[1] = False 

        for stepSize in range(2,int(upperBound/2)):
                crossOut(isPrime, stepSize)

        return filter(lambda n: isPrime[n], range(upperBound+1))

def crossOut(isPrime, stepSize):
        global upperBound
        for nonPrime in range(stepSize*2,upperBound,stepSize):
                isPrime[nonPrime] = False

primes = findPrimes()
print("The sum of all primes below {} is {}.".format(upperBound, sum(primes)))

stopTime = timeit.default_timer()
print("This program took {:.3f} seconds to run.".format(stopTime-startTime)) 