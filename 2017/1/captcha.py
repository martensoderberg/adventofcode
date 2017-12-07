import sys

def calculateDuplicatesSum(line):
  max = len(line)
  sum = 0
  for i in range(0, max):
    thisChar = line[i]
    nextChar = line[(i + 1) % max] # loop-around when nextChar is the last
    if thisChar == nextChar:
      sum += int(thisChar)
  return sum

if __name__ == "__main__":
  inputFile = open("input.txt", "r")
  line = inputFile.readline()
  sum = calculateDuplicatesSum(line)
  print(str(sum))
