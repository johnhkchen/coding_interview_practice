from functools import reduce
#Find the sum of the digits in the number 100! = 100x99x98x...x2x1
print(sum(map(int, (str(reduce(lambda x, y: x * y, range(1,100+1)))))))