

import random
# induvidual Scores
iScores = [" "] * 23

# added scores
aScores = [" "] * 11

# total Scores
tScores = ["   "] * 12
totalScore = 0

frame = 1

def printScoreBoard():
  print("-------------------------------------------------------------")
  print(F"|{iScores[1]}|{iScores[2]}|{aScores[1]}|{iScores[3]}|{iScores[4]}|{aScores[2]}|{iScores[5]}|{iScores[6]}|{aScores[3]}|{iScores[7]}|{iScores[8]}|{aScores[4]}|{iScores[9]}|{iScores[10]}|{aScores[5]}|{iScores[11]}|{iScores[12]}|{aScores[6]}|{iScores[13]}|{iScores[14]}|{aScores[7]}|{iScores[15]}|{iScores[16]}|{aScores[8]}|{iScores[17]}|{iScores[18]}|{aScores[9]}|{iScores[19]}|{iScores[20]}|{aScores[10]}|")
  print(F"| {tScores[1]} | {tScores[2]} | {tScores[3]} | {tScores[4]} | {tScores[5]} | {tScores[6]} | {tScores[7]} | {tScores[8]} | {tScores[9]} | {tScores[10]} | {tScores[11]} |")
  print("-------------------------------------------------------------")

firstRoll = 0
secondRoll = 0
thirdRoll = 0

isStrike = False
isSecondStrike = False
isSpare = False

# ask for first roll
# check if its 10
#     roll go to next turn but add those scores on to this turns total
# ask for second roll if its not a strike
# check if first and second roll add up to 10
#     if they do count the next roll in this total aswell

# Plays until frame 10
while not frame >= 12:

  firstRoll = random.randrange(1, 11)

  if not int(firstRoll) == 10:
    if not frame == 12 and not isSpare:
      secondRoll = random.randrange(1, 11)
      while firstRoll + secondRoll > 10:
        secondRoll = random.randrange(1, 11)


  if isStrike:
    totalScore += int(firstRoll)
    totalScore += int(secondRoll)
    tScores[frame - 1] = int(tScores[frame - 1]) + int(firstRoll) + int(secondRoll)
    #print(F"Adding first and second roll to frame {frame - 1}")


  if isSecondStrike:
    tScores[frame - 2] = int(tScores[frame - 2]) + int(firstRoll)
    totalScore += int(firstRoll)
    #print(F"Adding first roll to frame {frame - 2}")
    tScores[frame - 1] = int(tScores[frame - 1]) + int(firstRoll)
    #print(F"Adding first roll to frame {frame - 1}")
    isSecondStrike = False


  elif isSpare:
    totalScore += int(firstRoll)
    tScores[frame - 1] = int(tScores[frame - 1]) + int(firstRoll)
    isSpare = False
  

  if isStrike and int(firstRoll) == 10:
    isSecondStrike = True

  isStrike = False

  if int(firstRoll) == 10:
    isStrike = True
  
  elif int(firstRoll) + int(secondRoll) == 10:
    isSpare = True

  totalScore += int(firstRoll)
  totalScore += int(secondRoll)

  tScores[frame] = totalScore

  if len(str(tScores[frame])) == 1:
    tScores[frame] = " " + str(totalScore) + " "
  elif len(str(tScores[frame]))== 2:
    tScores[frame] = " " + str(totalScore)
  else:
    tScores[frame] = str(totalScore)


  if int(firstRoll) == 10:
    iScores[(frame * 2) - 1] = "x"
  #elif int(firstRoll) == 0:
  # iScores[(frame * 2) - 1] = " "
  else:
    iScores[(frame * 2) - 1] = firstRoll

  #if int(secondRoll) == 0:
  #  iScores[(frame * 2)] = " "
  #else:
  iScores[(frame * 2)] = secondRoll

  if frame == 10:
    if not isStrike and not isSpare:
      frame = frame + 1
  
  # Checking for correct spacing (each total score on the bottom has to be 3 long)
  for i in range (0, 12):
    #print(len(str(tScores[i])))
    if len(str(tScores[i])) != 3:
      if len(str(int(tScores[i]))) == 1:
        tScores[i] = " " + str(int(tScores[i])) + " "
      elif len(str(int(tScores[i]))) == 2:
        tScores[i] = " " + str(int(tScores[i]))
      else:
        tScores[i] = int(tScores[i])


  frame = frame + 1
  firstRoll = 0
  secondRoll = 0
  thirdRoll = 0

printScoreBoard()