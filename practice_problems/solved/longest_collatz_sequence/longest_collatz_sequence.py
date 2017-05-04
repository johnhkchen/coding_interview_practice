import timeit
startTime = timeit.default_timer()

def nextCollatzNumber(num):
        if (num % 2 == 0):
                return int(num/2)
        else:
                return int(3*num+1)

def chainLength(num):
        if num not in chainLengths:
                nextNum = nextCollatzNumber(num)
                if nextNum not in chainLengths:
                        chainLengths[nextNum] = chainLength(nextNum)
                chainLengths[num] = chainLengths[nextNum]+1
        return chainLengths[num]

maxValue = 1000000
chainLengths = {1:0}
longestChainStartValue = 1
longestChainLength = 0

for value in range(1, maxValue+1):
        if(chainLength(value) > longestChainLength):
                longestChainLength = chainLength(value)
                longestChainStartValue = value

print("Longest chain starts at {} and has {} iterations.".format(longestChainStartValue, longestChainLength))

stopTime = timeit.default_timer()
print("This program took {:.4f} seconds to run.".format(stopTime-startTime)) 