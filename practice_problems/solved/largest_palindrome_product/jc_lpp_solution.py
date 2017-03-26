# Problem: Find the largest palindrome made from the product of two 3-digit numbers.
# I'm using python for this problem for more practice in this language
# You can run this code with the command:
# python jc_lpp_solution.py

def isPalindrome(numStr):
  #Use two iterators to test for palindromic number
  left = 0;
  right = len(numStr)-1;
  while (right > left):
    if numStr[right] != numStr[left]:
      #not a palindromic number
      return False;
    right -= 1;
    left += 1;

  #numStr is a palindromic number
  return True;

# Main Code Begins here

# Simple iterative brute force solution: start at 500*500 (arbritary starting point), and work up until the limit of 999*999

largestPalindromicNumber = -1;
for x in range(500,999):
  for y in range(500,999):
    if x*y > largestPalindromicNumber:
      if isPalindrome(str(x*y)):
        largestPalindromicNumber = x*y

print(largestPalindromicNumber,' is the solution to Project Euler Problem #4.');

# Thoughts:
# This code was fast enough to work up to 999x999, but is too slow for variants involving larger factors

# Ideas on how to improve performance:
# 1) Find the upper limit (factorMax^2), and generate palindromic numbers less than that. Check to see if are composite numbers
# Benefit: Skip the vast majority of unfeasible answers by checking only palindromes from the largest end, then going down
# Caveat: Also a brute force solution, checking for primes is very expensive, prime factoration may not guarantee that a given number has two N-digit factors

# 2a) If a given product is less than the current largest palindromic number, don't check
# 2b) If factor_A or factor_B is less than largestPalindromicNumber/factor_MAX, increase said factor
# Benefit: reduces a lot of checking on clearly wrong answers
# Caveat: nothing? Might not be fast enough still

# Complexity Analysis

# Time Requirement
# O(N^2) numbers to check, O(log N) time to check each number
# Upper bound time complexity is thus O(N^2 log N)
# Not checking as many numbers will greatly improve performance
# Final thought: There should be some way to check from the tail end (start from 999x999, work toward 1x1), and stop at the first palindromic number found. Some sort of zig-zag starting from that corner? This should be a much faster way.

# Space Requirement
# O(1) for two int iterators, O(log N) to store a number up to N as a string (technically speaking)
# Python integers max out at 9223372036854775807, so the maximum space required tops out at around 2 ints and 30 chars
# Therefore, space is not a concern, O(1) space complexity is closer to the reality of the situation
