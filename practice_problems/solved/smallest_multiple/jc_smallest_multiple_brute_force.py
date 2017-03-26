# Problem: What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# I'm using python for this problem for more practice in this language
# You can run this code with the command:
# python jc_smallest_multiple.py

def isEvenlyDivisble(num, minDivisor, maxDivisor):
  for i in range(minDivisor, maxDivisor):
    if(num % i != 0):
     return False;
  return True;

def modCheck(num, minDivisor, maxDivisor):
  for i in range(minDivisor, maxDivisor):
    print(num," mod ",i," = ",(num % i));
  return;

x = 12252000; # lower bound determined through experimentation
minDiv = 1;
maxDiv = 20;
while(not isEvenlyDivisble(x,minDiv,maxDiv)):
  x += 2;

print("The smallest positive number that is evenly divisible by all of the numbers from ",minDiv," to ",maxDiv," is ", x)



# Thoughts While Solving:

# Try #1) Lets just brute force this one? Given a number, check for remainders (modulo) when divided by 1 to 20. If any of them fail, try the next number.
# Result) Okay, so brute-force is taking a while... let's think about this while we wait?

# Our upper bound is 20! = 2432902000000000000
# Seems like we won't reach that number anytime soon. Lets try to run this code with lesser divisors
# 1 to 10: 2520
# 1 to 11: 2520
# 12: 27720 = 2520 * 11
# 13: 27720
# 14: 360360 = 27720 * 13
# 15: 360360
# 16: 360360
# 17: 720720 = 360360 * 2? what's going on?
# 18: 12252240 = 720720*17 okay so primes are coming back again...
# 19: 12252240 Well, that took a while but it's definitely divisible by 20 so perhaps we're done?

# modCheck(2520,1,12);
# modCheck(27720,1,15);
# modCheck(360360,1,17);
# modCheck(720720,1,18);
# modCheck(12252240,1,20); 12252240 % 19 != 0


# Aha, semi-manual checking shows that 12252240 % 19 = 14. Lets just multiply it by 19 and see if that's correct.
# That was correct! 12252240 * 19 = 232792560, which passes the test from 1 to 22.

# Mistakes made:
# Forgot to use "not" keyword when negating (python is more wordy than C and Java)
# didn't capitalize True and False (idk what that's about)
# Brute force solution takes a long time - should've thought about it a bit more before trying to just have the computer do the work for me.

# How to do better next time: 
# 1) I probably could've let this run for 5 minutes to get the solution, but that's probably the largest number I could reasonably calculate using brute force. 1..23 would take at least an hour, 1..29 over a day, 1..31 over a month
# 2) There's a shortcut involving primes. If I multiple all the primes between minFactor and maxFactor, that's a "step size" I could use to cut down testing significantly - a millionfold or more when maxFactor reaches 20
# 3) This is only a guess, but perhaps the closed form solution to this problem is:
#     product(primesOnly(range(minFactor,maxFactor)))*leastCommonMultiple(evensOnly(range(minFactor,maxFactor)))
# I'll try to write a fast version to test it out
