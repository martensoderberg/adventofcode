import sys

inputFile = open("input.txt", "r")
line = inputFile.readline()

max = len(line)
sum = 0
for i in range(0, max):
  thisChar = line[i]
  nextChar = line[(i + 1) % max] # loop-around when nextChar is the last
  if thisChar == nextChar:
    print(thisChar)
    sum += int(thisChar)

print(str(sum))
