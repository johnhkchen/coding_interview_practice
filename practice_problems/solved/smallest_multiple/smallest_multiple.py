# Problem: What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# After bungling around using a brute force solution, I believe this closed-form solution is somewhat close
#  product(primesOnly(range(minFa ctor,maxFactor)))*leastCommonMultiple(evensOnly(range(minFactor,maxFactor)))

def isEvenlyDivisble(num, minDivisor, maxDivisor):
  # Checks to see if a number is a common multiple of all numbers in [minDivisor, maxDivisor]
  for i in range(minDivisor, maxDivisor):
    if(num % i != 0):
     return False;
  return True;

def product(list):
  # returns the products of all the elements of list
  total = 1;
  for x in list:
    total *= x;
  return total;

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

minDiv = 1;
maxDiv = 128;

resultantPrimes = primesEratosthenesSieve(maxDiv);
resultProd = product(resultantPrimes);
print("The primes less than {} are: {}. Their product is: {}.".format(maxDiv,resultantPrimes,resultProd));

# Calculate the smallest multiple 
factor = 1;
while(not isEvenlyDivisble(resultProd*factor,minDiv,maxDiv)):
  factor+=1;

print("The smallest positive number that is evenly divisible by all of the numbers from {} to {} is {}".format(minDiv,maxDiv,resultProd*factor));


# Thoughts
# Success! We cut down the calculation time for 1 to 20 from over 5 minutes to nearly instantaneous.
# This code ran well on my laptop up to 128
# Smallest multiple of 1 to 128 is 6676878045498705789701874602220118271269436344024536000

# Further improvements
# I've only optimized the left size of the proposed closed-form solution, because I wasn't sure if the right side was correct.
# For even better performance, make sure the right side of closed-form solution is correct and implement least common multiple

# 1) Optimize right side of closed form solution
# 2) Use map/reduce functions over iterative solutions, because the compiler can optimize those better

# Food for Thought
# 1) What if the maximum divisor is much larger, say, over 100000?
#   - We'll need to use a special data type for holding ultra-large integers
#     - Will need to implement custom product, sum, modulo functions, so it'd be its own class, perhaps something like VeryLongInteger()
#     - Linked lists could work?
#   - Optimize the right side as we did the left
# 2) What if the numbers range from, say, 40 to 100?
#   - This method will still work. Maybe the right side would need to be designed more carefully when optimizing?
# 3) What is it's not a range, but a list?
#   - Seems like a pretty standard LCM through prime factorization problem


























