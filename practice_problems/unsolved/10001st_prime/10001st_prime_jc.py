def sieve(table, factor, maxNum):
  # Designates all multiples of factor as nonprimes in table
  if(factor > maxNum):
    return;
  for i in range(factor*2,maxNum,factor):
    table[i] = False;
  return;

def primesEratosthenesSieve(maxNum):

  # 0 and 1 are not prime, and I'm in no mood to deal with off-by-two bugs
  primesTable = [True for i in range(maxNum+1)];
  primesTable[0] = primesTable[1] = False; 

  # use sieve of Eratosthenes (dynamic programming/memoization, in CS lingo) to calculate primes up to max
  for x in range(2,maxNum):
    sieve(primesTable, x, maxNum);

  # table built - return the primes
  primes = [];
  for i in range(2,maxNum):
    if(primesTable[i]):
      primes.append(i);

  return primes;

# We'll reuse the Sieve of Eratosthenes method
nthPrime = 10001

# Since we don't know what the upper bound is, set arbritary upper bound and double the bound until we have enough primes.
tryMax = 100000

while len(listPrimes) < nthPrime:
  tryMax = tryMax * 2
  print("Trying up to {}...".format(tryMax))
  # Try finding primes below our current upper bound
  listPrimes = primesEratosthenesSieve(tryMax)

print("Found {} primes...".format(len(listPrimes)))
print("The first five primes are: {}, {}, {}, {}, {}".format(listPrimes[0], listPrimes[1], listPrimes[2], listPrimes[3], listPrimes[4]))
print("The {}th prime is {}".format(nthPrime, listPrimes[nthPrime-1]))