def main():   
    names = sorted(map(lambda dirtyName: dirtyName[1:-1], open('names.txt').readline().split(','))) 
    atoi = dict(map(lambda x: (chr(ord('A')+x), x+1), range(26)))
    print(sum(map(lambda i: (i+1)*sum(map(lambda c: atoi[c], names[i])), range(len(names)))))

import timeit
startTime = timeit.default_timer()

main()

stopTime = timeit.default_timer()
print("This program took {:.5f} seconds to run.".format(stopTime-startTime)) 