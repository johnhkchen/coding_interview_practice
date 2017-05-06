from functools import reduce

print(reduce(lambda s, d: int(s) + int(d), str(pow(2,1000))))