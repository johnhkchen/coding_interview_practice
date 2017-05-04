# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

f = open("input.txt", "r")
longNumbers = []
for line in f:
        longNumbers.append(int(line))
# Python3's integers have no upper limit - easy solution here!
print(sum(longNumbers))