# todo: convert input grid into one-D string
fo = open("input_grid.txt", "r")

print("Read file {}".format(fo.name))

# Read file into 2D array of ints

rawInput = fo.readlines()
grid = []
width = len(rawInput)
for y in range(0, len(rawInput)):
  line = rawInput[y].split()
  row = []
  for x in range(0, len(line)):
    row.append(int(line[x]))
  grid.append(row)

# Look for largest product
sequenceLength = 4

def checkRight(row, col):
  product = 1;
  for i in range(0, sequenceLength):
    if(row+i < width):
      product = product * grid[row+i][col]
    else:
      return 0
  return product

def checkLeft(row, col):
  product = 1;
  for i in range(0, sequenceLength):
    if(row-i >= 0):
      product = product * grid[row-i][col]
    else:
      return 0
  return product

def checkUp(row, col):
  product = 1;
  for i in range(0, sequenceLength):
    if(col+i < width):
      product = product * grid[row][col+i]
    else:
      return 0
  return product

def checkDown(row, col):
  product = 1;
  for i in range(0, sequenceLength):
    if(col-i >= 0):
      product = product * grid[row][col-i]
    else:
      return 0
  return product

def checkDiagonalUL(row, col):
  product = 1;
  for i in range(0, sequenceLength):
    if(row-i >= 0 and col-i >= 0):
      product = product * grid[row-i][col-i]
    else:
      return 0
  return product

def checkDiagonalUR(row, col):
  product = 1;
  for i in range(0, sequenceLength):
    if(row-i >= 0 and col+i < width):
      product = product * grid[row-i][col+i]
    else:
      return 0
  return product

def checkDiagonalDL(row, col):
  product = 1;
  for i in range(0, sequenceLength):
    if(row+i < width and col-i >= 0):
      product = product * grid[row+i][col-i]
    else:
      return 0
  return product

def checkDiagonalDR(row, col):
  product = 1;
  for i in range(0, sequenceLength):
    if(row+i < width and col+i < width):
      product = product * grid[row+i][col+i]
    else:
      return 0
  return product

def checkAdjacentNumbers(row, col):
  # return the largest of the three sequences - horizontal, vertical, diagonal
  return max(checkLeft(row, col), checkRight(row, col), checkUp(row, col), checkDown(row, col), checkDiagonalUL(row, col), checkDiagonalUR(row, col), checkDiagonalDL(row, col), checkDiagonalDR(row, col));

largestSequence = -1
for row in range(0, width):
  for col in range(0, width):
    largestSequence = max(largestSequence, checkAdjacentNumbers(row, col))

print("The largest sequence is: {}".format(largestSequence))
