import random
import os

squaresUncovered = 0;

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def mineStateToString(state):
  if state == -1 or state == 9: return '?';
  elif state == 0: return ' ';
  else: return state;

def drawMinefield(minefield, fieldWidth, fieldHeight):
  # Print a guide row on top
  print("    ", end='')
  for x in range(fieldWidth):
    print(" {:^3} ".format(x), end='')
  print()
  for y in range(fieldHeight):
    print("{:^3} ".format(y),end='')
    for x in range(fieldWidth):
      # print guide on left
      print("[{:^3}]".format(mineStateToString(minefield[x][y])), end='')
    print()
  return

def initMinefield(fieldWidth, fieldHeight, numMines):
  # minefield states: 
  # -1 = undiscovered
  # 0-8 = landmines nearby?
  # 9 = landmine
  field = [[-1 for x in range(fieldHeight)] for y in range(fieldWidth)]

  # randomly place landmines
  if(numMines > fieldWidth*fieldHeight):
    print("Too many mines!")
    numMines = fieldHeight*fieldWidth

  while(numMines > 0):
    # roll random x and y
    rx = random.randint(0,fieldWidth-1);
    ry = random.randint(0,fieldHeight-1);

    if(field[rx][ry] == -1):
      #plop a mine
      field[rx][ry] = 9
      numMines -= 1
  return field

def sweepSpot(minefield, fieldWidth, fieldHeight, x, y):
  if fieldWidth <= x or x < 0 or fieldHeight <= y or y < 0:
    return True;
  else:
    if minefield[x][y] == 9:
      # hit a mine
      print("Kaboom! You hit a mine!")
      return False
    elif minefield[x][y] == -1:
      # no mines, count surrounding mines
      numSurroundingMines = countSurroundingMines(minefield, fieldWidth, fieldHeight, x, y)
      #print("({},{}) has {} mines nearby.".format(x,y,numSurroundingMines))
      minefield[x][y] = numSurroundingMines;
      global squaresUncovered
      squaresUncovered += 1;
      if numSurroundingMines == 0:
        for lookX in range(-1,2):
          for lookY in range(-1,2):
            if not (lookX == 0 and lookY == 0):
              sweepSpot(minefield, fieldWidth, fieldHeight, x+lookX, y+lookY);
      return True
    else:
      #print("You already sweeped this spot.");
      return True
  print("Unusual case error")
  return False

def countSurroundingMines(minefield, fieldWidth, fieldHeight, x, y):
  numSurroundingMines = 0
  for xOffset in range(-1,2):
    for yOffset in range(-1,2):
      if 0 <= x+xOffset < fieldWidth and 0 <= y+yOffset < fieldHeight:
        if minefield[x+xOffset][y+yOffset] == 9 and not (yOffset == 0 and xOffset == 0):
          #print("Swept mine at {},{}".format(x+xOffset, y+yOffset))
          numSurroundingMines += 1
  return numSurroundingMines

fieldWidth = int(input('How wide should the minefield be? >'))
fieldHeight = int(input('How tall should the minefield be? >'))
numMines = int(input('How many mines? >'))
minefield = initMinefield(fieldWidth,fieldHeight,numMines)

# Play minesweeper
keepPlaying = True
squaresUncovered = 0;
while keepPlaying:
  cls()
  drawMinefield(minefield,fieldWidth,fieldHeight)

  # Get user X
  while True:
    try:
      userInputX = int(input('Where to sweep X ({}/{})>'.format(squaresUncovered, fieldWidth*fieldHeight-numMines)))
    except ValueError:
      print("That was not a valid input. Try again.")
      continue
    break

  # Get user Y
  while True:
    try:
      userInputY = int(input('Where to sweep Y ({}/{})>'.format(squaresUncovered, fieldWidth*fieldHeight-numMines)))
    except ValueError:
      print("That was not a valid input. Try again.")
      continue
    break

  import pdb
  pdb.set_trace()

  keepPlaying = sweepSpot(minefield, fieldWidth, fieldHeight, userInputX, userInputY) and (squaresUncovered < fieldWidth*fieldHeight-numMines)

if squaresUncovered == fieldWidth*fieldHeight-numMines:
  print("You won! All {} mines have been discovered.".format(numMines))
else:
  print("You lose.")
print("Game Over.")
