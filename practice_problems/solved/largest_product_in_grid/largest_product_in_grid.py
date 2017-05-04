import numpy as np

grid = []
sequenceLength = 4

def main():
        loadGrid("input_grid.txt")
        startPoints = np.ndindex(len(grid), len(grid[0]))
        maxProduct = max(map(maxSeqProd, startPoints))
        print("The largest product sequence in this grid is: {}".format(maxProduct))

def loadGrid(fileName):
        global grid
        f = open(fileName, "r")
        for line in f:
                grid.append(list(map(int, line.split())))

def maxSeqProd(origin):
        return  max(    left(origin), right(origin), 
                        up(origin), down(origin),
                        upLeft(origin), upRight(origin),
                        downLeft(origin), downRight(origin)     );

def left(origin):
        return seqProd(origin, ( 0,-1))
def upLeft(origin):
        return seqProd(origin, (-1,-1))
def up(origin):
        return seqProd(origin, (-1, 0))
def upRight(origin):
        return seqProd(origin, (-1, 1))
def right(origin):
        return seqProd(origin, ( 0, 1))
def downRight(origin):
        return seqProd(origin, ( 1, 1))
def down(origin):
        return seqProd(origin, ( 1, 0))
def downLeft(origin):
        return seqProd(origin, ( 1,-1))

def seqProd(origin, offsets):
        offsetValue = lambda n: getGridValue(origin[0] + n*offsets[0], origin[1] + n*offsets[1])
        values = list(map(offsetValue, range(0, sequenceLength)))
        return np.prod(values)

def getGridValue(row, col):
        if (row >= len(grid) or row < 0) or (col >= len(grid) or col < 0):
                return 0
        else:
                return grid[row][col]

main()