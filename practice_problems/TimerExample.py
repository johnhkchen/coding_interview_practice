import timeit
startTime = timeit.default_timer()

#...

stopTime = timeit.default_timer()
print("This program took {:.3f} seconds to run.".format(stopTime-startTime)) 